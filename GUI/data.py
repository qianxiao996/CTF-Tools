# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_data(object):
    def setupUi(self, data):
        data.setObjectName("data")
        data.resize(528, 181)
        self.textEdit = QtWidgets.QTextEdit(data)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 491, 141))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"        border: 1px solid rgb(45, 45, 45);\n"
"        background: rgb(255, 255, 255);\n"
"    /* 边框颜色 */  \n"
"    border-color:rgb(10,45,110);  \n"
" \n"
"    /* 边框倒角 */  \n"
"    border-radius:5px;\n"
"    font:20px;    \n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(data)
        QtCore.QMetaObject.connectSlotsByName(data)

    def retranslateUi(self, data):
        _translate = QtCore.QCoreApplication.translate
        data.setWindowTitle(_translate("data", "在线网站"))

