# -*- coding: utf-8 -*-
# @Time : 2022/3/25 8:46
# @Author : Cary
# @File : test.py
# @Software: PyCharm

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class Demo(QWidget):

    def __init__(self, parent=None):

        super(Demo, self).__init__(parent) # 调用父类的初始化方法

        self.initUI() #初始化UI界面

    def initUI(self):
        grid = QGridLayout()
        label1 = QLabel()
        label1.setText('用户名：')
        text1 = QLineEdit()
        label2 = QLabel()
        label2.setText('密  码：')
        text2 = QLineEdit()
        grid.addWidget(label1, 0, 0, QtCore.Qt.AlignLeft)
        grid.addWidget(label2, 1, 0, QtCore.Qt.AlignLeft)
        grid.addWidget(text1, 0, 1, QtCore.Qt.AlignLeft)
        grid.addWidget(text2, 1, 1, QtCore.Qt.AlignLeft)

        btn1 = QPushButton()
        btn1.setText('登录')
        btn2 = QPushButton()
        btn2.setText('退出')
        grid.addWidget(btn1, 2, 0, QtCore.Qt.AlignCenter)
        grid.addWidget(btn2, 2, 1, QtCore.Qt.AlignCenter)
        self.setLayout(grid)

if __name__ == '__main__':
     app = QApplication(sys.argv)
     demo =Demo()
     demo.show()
     sys.exit(app.exec_())


