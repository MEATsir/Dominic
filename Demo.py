import sys
import GUI
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    # 向主窗口添加控件
    ui = GUI.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
