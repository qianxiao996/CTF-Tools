# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KEY.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KEY(object):
    def setupUi(self, KEY):
        KEY.setObjectName("KEY")
        KEY.resize(419, 106)
        self.Key1 = QtWidgets.QLineEdit(KEY)
        self.Key1.setGeometry(QtCore.QRect(76, 20, 241, 31))
        self.Key1.setText("")
        self.Key1.setObjectName("Key1")
        self.Key2 = QtWidgets.QLineEdit(KEY)
        self.Key2.setGeometry(QtCore.QRect(76, 60, 241, 31))
        self.Key2.setObjectName("Key2")
        self.layoutWidget = QtWidgets.QWidget(KEY)
        self.layoutWidget.setGeometry(QtCore.QRect(16, 20, 50, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.enter = QtWidgets.QPushButton(KEY)
        self.enter.setGeometry(QtCore.QRect(330, 20, 71, 31))
        self.enter.setObjectName("enter")
        self.quxiao = QtWidgets.QPushButton(KEY)
        self.quxiao.setGeometry(QtCore.QRect(330, 60, 71, 31))
        self.quxiao.setObjectName("quxiao")

        self.retranslateUi(KEY)
        self.quxiao.clicked.connect(KEY.close)
        QtCore.QMetaObject.connectSlotsByName(KEY)

    def retranslateUi(self, KEY):
        _translate = QtCore.QCoreApplication.translate
        KEY.setWindowTitle(_translate("KEY", "KEY"))
        self.label.setText(_translate("KEY", "Keys 1"))
        self.label_2.setText(_translate("KEY", "Keys 2"))
        self.enter.setText(_translate("KEY", "确定"))
        self.quxiao.setText(_translate("KEY", "取消"))

