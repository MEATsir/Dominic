import pkuseg
import math
import random
from tqdm import tqdm,trange
import codecs
from pathlib import Path
label_map = { # 标签映射
        '财经':0,
        '房产':1,
        '教育':2,
        '科技':3,
        '军事':4,
        '汽车':5,
        '体育':6,
        '游戏':7,
        '娱乐':8,
        '其他':9
    }
def read_corpus(file_path):
    """读取语料
    :param file_path:
    :param type:
    :return:
    """
    src_data = []
    labels = []
    seg = pkuseg.pkuseg()
    with codecs.open(file_path,'r',encoding='gbk',errors='ignore' ) as fout:
        for line in tqdm(fout.readlines(),desc='reading corpus'):
            if line is not None:
                pair = line.strip().split('\t')
                if len(pair) != 2:
                    print(pair)
                    continue
                src_data.append(seg.cut(pair[0]))
                labels.append(pair[1])

    return (src_data, labels)

def pad_sents(sents,pad_token):
    """pad句子"""
    sents_padded = []

    lengths = [len(s) for s in sents]
    max_len = max(lengths)
    for sent in sents:
        sent_padded = sent + [pad_token] * (max_len - len(sent))
        sents_padded.append(sent_padded)
    return sents_padded
def batch_iter(data, batch_size, shuffle=False):
    """
        batch数据
    :param data: list of tuple
    :param batch_size:
    :param shuffle:
    :return:
    """
    batch_num = math.ceil(len(data) / batch_size)
    index_array = list(range(len(data)))
    if shuffle:
        random.shuffle(index_array)

    for i in trange(batch_num,desc='get mini_batch data'):
        indices = index_array[i*batch_size:(i+1)*batch_size]
        examples = [data[idx] for idx in indices]
        examples = sorted(examples,key=lambda x: len(x[1]),reverse=True)
        src_sents = [e[0] for e in examples]
        labels = [int(e[1]) for e in examples]

        yield src_sents, labels
def text_write(filename,data):
    with open(filename,'w') as fw:
        for sentence,target in tqdm(data,desc = 'write data to disk'):
            target  = str(target)
            line = '\t'.join([sentence,",".join(target)])
            fw.write(line +'\n')


def init_logger(log_name,log_dir):
    if not isinstance(log_dir,Path):
        log_dir = Path(log_dir)
    if not log_dir.exists():
        log_dir.mkdir(exist_ok=True)
    if log_name not in Logger.manager.loggerDict:
        logger  = logging.getLogger(log_name)
        logger.setLevel(logging.DEBUG)
        handler = TimedRotatingFileHandler(filename=str(log_dir / f"{log_name}.log"),when='D',backupCount = 30)
        datefmt = '%Y-%m-%d %H:%M:%S'
        format_str = '[%(asctime)s]: %(name)s %(filename)s[line:%(lineno)s] %(levelname)s  %(message)s'
        formatter = logging.Formatter(format_str,datefmt)
        handler.setFormatter(formatter)
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
        console= logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)
        logger.addHandler(console)

        handler = TimedRotatingFileHandler(filename=str(log_dir / "ERROR.log"),when='D',backupCount= 30)
        datefmt = '%Y-%m-%d %H:%M:%S'
        format_str = '[%(asctime)s]: %(name)s %(filename)s[line:%(lineno)s] %(levelname)s  %(message)s'
        formatter = logging.Formatter(format_str,datefmt)
        handler.setFormatter(formatter)
        handler.setLevel(logging.ERROR)
        logger.addHandler(handler)
    logger = logging.getLogger(log_name)
    return logger
