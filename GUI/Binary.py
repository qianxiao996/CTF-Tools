# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Binary.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Binary(object):
    def setupUi(self, Binary):
        Binary.setObjectName("Binary")
        Binary.resize(330, 69)
        self.enter = QtWidgets.QPushButton(Binary)
        self.enter.setGeometry(QtCore.QRect(220, 20, 93, 31))
        self.enter.setObjectName("enter")
        self.splitter_2 = QtWidgets.QSplitter(Binary)
        self.splitter_2.setGeometry(QtCore.QRect(10, 20, 109, 31))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        self.label.setObjectName("label")
        self.Source = QtWidgets.QLineEdit(self.splitter_2)
        self.Source.setObjectName("Source")
        self.splitter = QtWidgets.QSplitter(Binary)
        self.splitter.setGeometry(QtCore.QRect(130, 20, 77, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.result_label = QtWidgets.QLabel(self.splitter)
        self.result_label.setObjectName("result_label")
        self.result = QtWidgets.QLineEdit(self.splitter)
        self.result.setObjectName("result")

        self.retranslateUi(Binary)
        QtCore.QMetaObject.connectSlotsByName(Binary)

    def retranslateUi(self, Binary):
        _translate = QtCore.QCoreApplication.translate
        Binary.setWindowTitle(_translate("Binary", "Binary"))
        self.enter.setText(_translate("Binary", "确定"))
        self.label.setText(_translate("Binary", "From"))
        self.result_label.setText(_translate("Binary", "To"))

