import torch
import pkuseg
import codecs
import tqdm
import random
import numpy as np
from model import CNN
from vocab import Vocab
import math
from tqdm import trange, tqdm
label_to_id = {  # 标签映射
    0: '财经',
    1:'房产',
    2:'教育',
    3:'科技',
    4:'军事',
    5:'汽车',
    6:'体育',
    7:'游戏',
    8:'娱乐',
    9:'其他'
}
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
def read_test_corpus(file_path):
    """读取语料
    :param file_path:
    :param type:
    :return:
    """
    src_data = []
    seg = pkuseg.pkuseg()
    with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as fout:
        for line in tqdm(fout.readlines(), desc='reading corpus'):
            if line is not None:
                src_data.append(seg.cut(line))
    return src_data
def cut_corpus(string):
    src_data = []
    seg = pkuseg.pkuseg()
    lst = string.split('\n')
    for line in lst:
        if line:
           src_data.append(seg.cut(line))
    return src_data
def test_batch_iter(data, batch_size, shuffle=False):
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
        src_sents = [e for e in examples]
        yield src_sents
def set_seed():
    random.seed(3344)
    np.random.seed(3344)
    torch.manual_seed(3344)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(3344)
vocab = Vocab.load('./vocab.json')
label_map = vocab.labels
set_seed()
cnn_model = CNN(len(vocab.vocab), 300, 100, [2, 3, 4], len(label_map),
                dropout=0.2)
cnn_model.load_state_dict(torch.load('classifa-best-CNN.th',map_location={'cuda:6':'cuda:0'}))
cnn_model.to(device)
cnn_model.eval()
if __name__ == '__main__':
    pass
