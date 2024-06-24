import sys    #訪問命令行參數和控制Python執行環境
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
                             #應用程式類      #窗口類   #按鈕類

class MyWidget(QWidget):
    #定義主窗口類
    def __init__(self):       # MyWidget 初始化
        super().__init__()    # QWidget 初始化 (調用父類)
        self.initUI()         # initUI 方法來初始化用戶界面

    #初始化用戶界面
    def initUI(self):
        self.setWindowTitle('my window')     # 窗口標題
        self.setGeometry(50, 50, 200, 150)   # 窗口的位置和大小 (x, y, 寬, 高)

        #創建一個按鈕，顯示文本為 "button"，並設置為窗口的子部件
        self.customButton = QPushButton('button', self)     
        self.customButton.move(60, 50)                          #按鈕相對於窗口的位置
        self.customButton.clicked.connect(self.onButtonClick)   #按鈕點擊連接到 onButtonClick

    def onButtonClick(self):
        self.customButton.setText('hello world')   #按鈕的文本設置


#主程式執行入口
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
