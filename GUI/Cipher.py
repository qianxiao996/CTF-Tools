# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cipher.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cipher(object):
    def setupUi(self, Cipher):
        Cipher.setObjectName("Cipher")
        Cipher.resize(584, 252)
        self.gridLayout = QtWidgets.QGridLayout(Cipher)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit_source = QtWidgets.QPlainTextEdit(Cipher)
        self.plainTextEdit_source.setObjectName("plainTextEdit_source")
        self.gridLayout.addWidget(self.plainTextEdit_source, 0, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_key1 = QtWidgets.QLabel(Cipher)
        self.label_key1.setObjectName("label_key1")
        self.horizontalLayout_2.addWidget(self.label_key1)
        self.lineEdit_key1 = QtWidgets.QLineEdit(Cipher)
        self.lineEdit_key1.setMinimumSize(QtCore.QSize(234, 0))
        self.lineEdit_key1.setObjectName("lineEdit_key1")
        self.horizontalLayout_2.addWidget(self.lineEdit_key1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_key2 = QtWidgets.QLabel(Cipher)
        self.label_key2.setObjectName("label_key2")
        self.horizontalLayout_3.addWidget(self.label_key2)
        self.lineEdit_key2 = QtWidgets.QLineEdit(Cipher)
        self.lineEdit_key2.setMinimumSize(QtCore.QSize(234, 0))
        self.lineEdit_key2.setObjectName("lineEdit_key2")
        self.horizontalLayout_3.addWidget(self.lineEdit_key2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_key3 = QtWidgets.QLabel(Cipher)
        self.label_key3.setObjectName("label_key3")
        self.horizontalLayout.addWidget(self.label_key3)
        self.lineEdit_key3 = QtWidgets.QLineEdit(Cipher)
        self.lineEdit_key3.setObjectName("lineEdit_key3")
        self.horizontalLayout.addWidget(self.lineEdit_key3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_enter = QtWidgets.QPushButton(Cipher)
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.horizontalLayout_4.addWidget(self.pushButton_enter)
        self.pushButton_close = QtWidgets.QPushButton(Cipher)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_4.addWidget(self.pushButton_close)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.retranslateUi(Cipher)
        QtCore.QMetaObject.connectSlotsByName(Cipher)

    def retranslateUi(self, Cipher):
        _translate = QtCore.QCoreApplication.translate
        Cipher.setWindowTitle(_translate("Cipher", "KEY3"))
        self.plainTextEdit_source.setPlaceholderText(_translate("Cipher", "在这里输入密文"))
        self.label_key1.setText(_translate("Cipher", "Key1"))
        self.lineEdit_key1.setPlaceholderText(_translate("Cipher", "可选字段"))
        self.label_key2.setText(_translate("Cipher", "Key2"))
        self.lineEdit_key2.setPlaceholderText(_translate("Cipher", "可选字段"))
        self.label_key3.setText(_translate("Cipher", "key3"))
        self.lineEdit_key3.setPlaceholderText(_translate("Cipher", "可选字段"))
        self.pushButton_enter.setText(_translate("Cipher", "确定"))
        self.pushButton_close.setText(_translate("Cipher", "取消"))
