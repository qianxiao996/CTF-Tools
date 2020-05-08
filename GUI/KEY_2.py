# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KEY_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KEY2(object):
    def setupUi(self, KEY2):
        KEY2.setObjectName("KEY2")
        KEY2.resize(419, 106)
        self.Key1 = QtWidgets.QLineEdit(KEY2)
        self.Key1.setGeometry(QtCore.QRect(76, 20, 241, 31))
        self.Key1.setText("")
        self.Key1.setObjectName("Key1")
        self.Key2 = QtWidgets.QLineEdit(KEY2)
        self.Key2.setGeometry(QtCore.QRect(76, 60, 241, 31))
        self.Key2.setObjectName("Key2")
        self.layoutWidget = QtWidgets.QWidget(KEY2)
        self.layoutWidget.setGeometry(QtCore.QRect(16, 20, 50, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.key_1 = QtWidgets.QLabel(self.layoutWidget)
        self.key_1.setObjectName("key_1")
        self.verticalLayout.addWidget(self.key_1)
        self.keyl_2 = QtWidgets.QLabel(self.layoutWidget)
        self.keyl_2.setObjectName("keyl_2")
        self.verticalLayout.addWidget(self.keyl_2)
        self.enter = QtWidgets.QPushButton(KEY2)
        self.enter.setGeometry(QtCore.QRect(330, 20, 71, 31))
        self.enter.setObjectName("enter")
        self.quxiao = QtWidgets.QPushButton(KEY2)
        self.quxiao.setGeometry(QtCore.QRect(330, 60, 71, 31))
        self.quxiao.setObjectName("quxiao")

        self.retranslateUi(KEY2)
        self.quxiao.clicked.connect(KEY2.close)
        QtCore.QMetaObject.connectSlotsByName(KEY2)

    def retranslateUi(self, KEY2):
        _translate = QtCore.QCoreApplication.translate
        KEY2.setWindowTitle(_translate("KEY2", "KEY"))
        self.key_1.setText(_translate("KEY2", "Keys 1"))
        self.keyl_2.setText(_translate("KEY2", "Keys 2"))
        self.enter.setText(_translate("KEY2", "确定"))
        self.quxiao.setText(_translate("KEY2", "取消"))

