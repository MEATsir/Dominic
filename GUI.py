from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
import qtawesome
import pandas as pd
test_net = True
if test_net:
    print("初始化中...")
    from test2 import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 加入并设置控件
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 496)
        MainWindow.setMinimumSize(QtCore.QSize(1061, 496))
        MainWindow.setMaximumSize(QtCore.QSize(1061, 496))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 20, 1061, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 400, 311, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 20, 421, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.layoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 61, 1021, 331))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.textEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout.addWidget(self.textEdit_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        # 给按钮添加槽
        self.pushButton_2.clicked.connect(self.loadFile)
        self.pushButton_3.clicked.connect(self.processFile)
        self.pushButton_4.clicked.connect(self.connection4)
        self.pushButton.clicked.connect(self.connection)
        # 美化
        MainWindow.setWindowOpacity(0.97)  # 设置透明度
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def changeButtonStyle(self, btn):
        spin_icon = qtawesome.icon('fa5s.microphone-alt', color='white')
        btn.setIcon(spin_icon)  # 设置图标
        btn.setIconSize(QtCore.QSize(50, 50))
        btn.setStyleSheet('''QPushButton{border:none;}
                QPushButton:hover{color:white;
                            border:2px solid #F3F3F5;
                            border-radius:35px;
                            background:darkGray;}''')
    def test_file(self, file_path):
        self.textEdit_2.append("reading corpus:")
        QApplication.processEvents()
        test_data = read_test_corpus(file_path)
        test_data = [text for text in test_data]
        with torch.no_grad():
            for src_sents in test_batch_iter(test_data, 8):
                src_sents_id = vocab.vocab.to_input_tensor(src_sents, device)
                logits = cnn_model(src_sents_id)
                lables = [list(i).index(max(i)) for i in list(logits.cpu().numpy())]
                for id in range(len(src_sents)):
                    news = '新闻：' + ''.join(src_sents[id])
                    results = '分类结果:' + label_to_id[lables[id]]
                    self.textEdit_2.append(results)
                    QApplication.processEvents()
    def connection4(self):
        # 调用预测函数test，与按钮“开始预测”连接
        string = self.textEdit.toPlainText()
        if test_net:
            if not string:
                self.textEdit_2.append("检测到输入为空！")
            else:
                self.textEdit_2.clear()
                test_data = cut_corpus(string)
                test_data = [text for text in test_data]
                with torch.no_grad():
                    for src_sents in test_batch_iter(test_data, 8):
                        src_sents_id = vocab.vocab.to_input_tensor(src_sents, device)
                        logits = cnn_model(src_sents_id)
                        lables = [list(i).index(max(i)) for i in list(logits.cpu().numpy())]
                        for id in range(len(src_sents)):
                            news = '新闻：' + ''.join(src_sents[id])
                            results = '分类结果:' + label_to_id[lables[id]]
                            self.textEdit_2.append(results)
                            QApplication.processEvents()
    def connection(self):
        # 清空两个文本框，与按钮“清空”连接
        self.textEdit.clear()
        self.textEdit_2.clear()
    def loadFile(self):
        # 显示选择文件路径的对话框，与“选择文件”按钮连接
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(caption="选择文件", directory='.', filter="*.txt")
        if fileName:
            self.textEdit.setText(fileName)
    def processFile(self):
        # 处理文件，与“开始处理”按钮连接
        fileName = self.textEdit.toPlainText()
        if fileName:
            self.test_file(fileName)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "选择文件"))
        self.pushButton_3.setText(_translate("MainWindow", "开始处理文件"))
        self.pushButton_4.setText(_translate("MainWindow", "开始预测"))
        self.pushButton.setText(_translate("MainWindow", "清空"))
        self.radioButton.setText(_translate("MainWindow", "显示概率"))