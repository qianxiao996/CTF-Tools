# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(328, 65)
        self.keyenter = QtWidgets.QPushButton(Form)
        self.keyenter.setGeometry(QtCore.QRect(222, 20, 93, 31))
        self.keyenter.setObjectName("keyenter")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(15, 20, 195, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.key = QtWidgets.QLineEdit(self.splitter)
        self.key.setObjectName("key")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Key"))
        self.keyenter.setText(_translate("Form", "确定"))
        self.label.setText(_translate("Form", "Key"))

