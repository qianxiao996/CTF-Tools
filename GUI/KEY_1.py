# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KEY_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KEY1(object):
    def setupUi(self, KEY1):
        KEY1.setObjectName("KEY1")
        KEY1.resize(328, 65)
        self.keyenter = QtWidgets.QPushButton(KEY1)
        self.keyenter.setGeometry(QtCore.QRect(222, 20, 93, 31))
        self.keyenter.setObjectName("keyenter")
        self.splitter = QtWidgets.QSplitter(KEY1)
        self.splitter.setGeometry(QtCore.QRect(15, 20, 195, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.key = QtWidgets.QLineEdit(self.splitter)
        self.key.setObjectName("key")

        self.retranslateUi(KEY1)
        QtCore.QMetaObject.connectSlotsByName(KEY1)
        KEY1.setTabOrder(self.key, self.keyenter)

    def retranslateUi(self, KEY1):
        _translate = QtCore.QCoreApplication.translate
        KEY1.setWindowTitle(_translate("KEY1", "Key"))
        self.keyenter.setText(_translate("KEY1", "确定"))
        self.label.setText(_translate("KEY1", "Key"))

