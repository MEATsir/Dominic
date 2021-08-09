# Multi_Model_Classification
##多模型中文新闻文本分类 py3.8

_*注：由于使用pkuseg程序包，导致整个文件无法打包成exe文件使用，请各位评委谅解。_

pkuseg包安装时可能会遇到报错，请您尝试使用如下命令安装，并切换到python3.8：

使用pip :
* pip3 install pkuseg
* pip3 install -U pkuseg
* pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pkuseg

使用conda：
* conda install pkuseg

或者直接访问 https://pypi.org/project/pkuseg/0.0.25/#files 下载对应版本的pkuseg，直接pip安装whl文件即可。
感谢您的谅解！

### 注意事项
* 在预测测试集B前要保证，测试集B的格式与测试集A相匹配，即要包含表头，每个部分分成四列，第一列为编号，第二列为
分类，第三列为新闻标题，第四列为新闻正文。如果格式不匹配，请将文件变为相匹配的格式，再进行操作，感谢理解！

* 运行程序前，请确保安装了对应版本的程序包。对应程序包的需求整理在当前文件夹的requirement.txt文件内。

* 运行 <font color=#008000 >测试数据B用.py</font> 后将生成一个新文件 <font color=#008000 >测试集B结果.xlsx</font>，其形式与测试集A是一致的，在标签处填满了。

<font size=1 >_PS：本次训练是在服务器第六块GPU上训练的，在程序中已经做好了基本的处理，应该不会碰到问题。但是如果运气不好碰到GPU不匹配的情况，请参考load_state_dict中的map_location参数进行
device投射。_</font>

### 使用说明

<font color=#FF000 >如果有讲的不清楚的地方可以参考视频中的检测方法</font>

1、__前端界面的展示__：前端界面可以直接运行Demo.py获得。

2、__校验数据与测试B__：重新测试数据 及 测试数据B可以直接运行 测试数据B用.py。在程序运行后输入测试集的路径即可。
（推荐直接将测试集放入当前目录，直接输入文件名即可预测）。 预测完毕后将生成结果文件“测试集B结果.xlsx”。
