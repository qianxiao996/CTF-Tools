# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 679)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777188))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/19190/.designer/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_11 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_11.setGeometry(QtCore.QRect(377, 391, 167, 31))
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.Source_tihuan_result = QtWidgets.QLineEdit(self.centralwidget)
        self.Source_tihuan_result.setGeometry(QtCore.QRect(414, 2, 113, 31))
        self.Source_tihuan_result.setStyleSheet("QLineEdit {\n"
"        border-radius: 4px;\n"
"        height: 25px;\n"
"        border: 1px solid rgb(100, 100, 100);\n"
"        background: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit:enabled {\n"
"        color: rgb(175, 175, 175);\n"
"}\n"
"QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color:rgb(255, 85, 255)\n"
"}\n"
"QLineEdit:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}")
        self.Source_tihuan_result.setObjectName("Source_tihuan_result")
        self.source_text = QtWidgets.QLabel(self.centralwidget)
        self.source_text.setGeometry(QtCore.QRect(8, 10, 72, 15))
        self.source_text.setStyleSheet("\n"
"   color:rgb(170, 85, 255);\n"
"   font:bold 20px;  ")
        self.source_text.setObjectName("source_text")
        self.Source_tihuan_source = QtWidgets.QLineEdit(self.centralwidget)
        self.Source_tihuan_source.setGeometry(QtCore.QRect(229, 2, 113, 31))
        self.Source_tihuan_source.setStyleSheet("QLineEdit {\n"
"        border-radius: 4px;\n"
"        height: 25px;\n"
"        border: 1px solid rgb(100, 100, 100);\n"
"        background: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit:enabled {\n"
"        color: rgb(175, 175, 175);\n"
"}\n"
"QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color: rgb(255, 85, 255)\n"
"}\n"
"QLineEdit:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}")
        self.Source_tihuan_source.setObjectName("Source_tihuan_source")
        self.label2_5 = QtWidgets.QLabel(self.centralwidget)
        self.label2_5.setGeometry(QtCore.QRect(348, 2, 66, 31))
        self.label2_5.setStyleSheet("      font: 17px;  \n"
"   color:rgb(170, 85, 255);\n"
"")
        self.label2_5.setObjectName("label2_5")
        self.Source_text = QtWidgets.QTextEdit(self.centralwidget)
        self.Source_text.setGeometry(QtCore.QRect(1, 35, 861, 291))
        self.Source_text.setStyleSheet("QTextEdit {\n"
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
        self.Source_text.setObjectName("Source_text")
        self.result_text = QtWidgets.QLabel(self.centralwidget)
        self.result_text.setGeometry(QtCore.QRect(10, 335, 72, 21))
        self.result_text.setStyleSheet("\n"
"   color:rgb(170, 85, 255);\n"
"   font:bold 20px;  ")
        self.result_text.setObjectName("result_text")
        self.Result_text = QtWidgets.QTextEdit(self.centralwidget)
        self.Result_text.setGeometry(QtCore.QRect(1, 361, 861, 291))
        self.Result_text.setStyleSheet("QTextEdit {\n"
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
        self.Result_text.setObjectName("Result_text")
        self.Result_tihuan_source = QtWidgets.QLineEdit(self.centralwidget)
        self.Result_tihuan_source.setGeometry(QtCore.QRect(230, 328, 113, 31))
        self.Result_tihuan_source.setStyleSheet("QLineEdit {\n"
"        border-radius: 4px;\n"
"        height: 25px;\n"
"        border: 1px solid rgb(100, 100, 100);\n"
"        background: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit:enabled {\n"
"        color: rgb(175, 175, 175);\n"
"}\n"
"QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color: rgb(255, 85, 255)\n"
"}\n"
"QLineEdit:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}")
        self.Result_tihuan_source.setObjectName("Result_tihuan_source")
        self.Result_tihuan_result = QtWidgets.QLineEdit(self.centralwidget)
        self.Result_tihuan_result.setGeometry(QtCore.QRect(414, 328, 113, 31))
        self.Result_tihuan_result.setStyleSheet("QLineEdit {\n"
"        border-radius: 4px;\n"
"        height: 25px;\n"
"        border: 1px solid rgb(100, 100, 100);\n"
"        background: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit:enabled {\n"
"        color: rgb(175, 175, 175);\n"
"}\n"
"QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color:rgb(255, 85, 255)\n"
"}\n"
"QLineEdit:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}")
        self.Result_tihuan_result.setObjectName("Result_tihuan_result")
        self.label2_6 = QtWidgets.QLabel(self.centralwidget)
        self.label2_6.setGeometry(QtCore.QRect(348, 328, 66, 31))
        self.label2_6.setStyleSheet("      font: 17px;  \n"
"   color:rgb(170, 85, 255);\n"
"")
        self.label2_6.setObjectName("label2_6")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(533, 328, 328, 31))
        self.splitter_2.setStyleSheet("\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为10点*/\n"
"    font-size:10pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(170, 170, 255);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:8px;\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"")
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.Result_tihuan_Button = QtWidgets.QPushButton(self.splitter_2)
        self.Result_tihuan_Button.setStyleSheet("")
        self.Result_tihuan_Button.setObjectName("Result_tihuan_Button")
        self.Result_clear_Button = QtWidgets.QPushButton(self.splitter_2)
        self.Result_clear_Button.setStyleSheet("")
        self.Result_clear_Button.setObjectName("Result_clear_Button")
        self.Result_Copy_Button = QtWidgets.QPushButton(self.splitter_2)
        self.Result_Copy_Button.setStyleSheet("")
        self.Result_Copy_Button.setObjectName("Result_Copy_Button")
        self.Result_Paste_Button = QtWidgets.QPushButton(self.splitter_2)
        self.Result_Paste_Button.setStyleSheet("")
        self.Result_Paste_Button.setObjectName("Result_Paste_Button")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(533, 2, 328, 31))
        self.splitter.setStyleSheet("\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为10点*/\n"
"    font-size:10pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(170, 170, 255);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:8px;\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"")
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.Source_tihuan_Button = QtWidgets.QPushButton(self.splitter)
        self.Source_tihuan_Button.setStyleSheet("\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为10点*/\n"
"    font-size:10pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(170, 170, 255);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:8px;\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"")
        self.Source_tihuan_Button.setObjectName("Source_tihuan_Button")
        self.Source_clear_Button = QtWidgets.QPushButton(self.splitter)
        self.Source_clear_Button.setStyleSheet("")
        self.Source_clear_Button.setObjectName("Source_clear_Button")
        self.Source_Copy_Button = QtWidgets.QPushButton(self.splitter)
        self.Source_Copy_Button.setStyleSheet("")
        self.Source_Copy_Button.setObjectName("Source_Copy_Button")
        self.Source_Paste_Button = QtWidgets.QPushButton(self.splitter)
        self.Source_Paste_Button.setStyleSheet("")
        self.Source_Paste_Button.setObjectName("Source_Paste_Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 861, 441))
        self.label.setStyleSheet("    background-color:white;")
        self.label.setObjectName("label")
        self.label.raise_()
        self.splitter_11.raise_()
        self.Source_tihuan_result.raise_()
        self.source_text.raise_()
        self.Source_tihuan_source.raise_()
        self.label2_5.raise_()
        self.Source_text.raise_()
        self.result_text.raise_()
        self.Result_text.raise_()
        self.Result_tihuan_source.raise_()
        self.Result_tihuan_result.raise_()
        self.label2_6.raise_()
        self.splitter_2.raise_()
        self.splitter.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 864, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuEncode = QtWidgets.QMenu(self.menuBar)
        self.menuEncode.setObjectName("menuEncode")
        self.menuDecode = QtWidgets.QMenu(self.menuBar)
        self.menuDecode.setObjectName("menuDecode")
        self.menuEncrypt = QtWidgets.QMenu(self.menuBar)
        self.menuEncrypt.setObjectName("menuEncrypt")
        self.menuDecrypt = QtWidgets.QMenu(self.menuBar)
        self.menuDecrypt.setObjectName("menuDecrypt")
        self.menuBinary = QtWidgets.QMenu(self.menuBar)
        self.menuBinary.setObjectName("menuBinary")
        self.menuOthers = QtWidgets.QMenu(self.menuBar)
        self.menuOthers.setObjectName("menuOthers")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionURL_UTF8 = QtWidgets.QAction(MainWindow)
        self.actionURL_UTF8.setObjectName("actionURL_UTF8")
        self.actionURL_GB2312 = QtWidgets.QAction(MainWindow)
        self.actionURL_GB2312.setObjectName("actionURL_GB2312")
        self.actionUnicode = QtWidgets.QAction(MainWindow)
        self.actionUnicode.setObjectName("actionUnicode")
        self.actionEscape_U = QtWidgets.QAction(MainWindow)
        self.actionEscape_U.setObjectName("actionEscape_U")
        self.actionHtmlEncode = QtWidgets.QAction(MainWindow)
        self.actionHtmlEncode.setObjectName("actionHtmlEncode")
        self.actionASCII = QtWidgets.QAction(MainWindow)
        self.actionASCII.setObjectName("actionASCII")
        self.actionBase64 = QtWidgets.QAction(MainWindow)
        self.actionBase64.setObjectName("actionBase64")
        self.actionStr_Hex = QtWidgets.QAction(MainWindow)
        self.actionStr_Hex.setObjectName("actionStr_Hex")
        self.actionURL_UTF8_encode = QtWidgets.QAction(MainWindow)
        self.actionURL_UTF8_encode.setObjectName("actionURL_UTF8_encode")
        self.actionURL_UTF8_decode = QtWidgets.QAction(MainWindow)
        self.actionURL_UTF8_decode.setObjectName("actionURL_UTF8_decode")
        self.actionURL_GB2312_encode = QtWidgets.QAction(MainWindow)
        self.actionURL_GB2312_encode.setObjectName("actionURL_GB2312_encode")
        self.actionURL_GB2312_decode = QtWidgets.QAction(MainWindow)
        self.actionURL_GB2312_decode.setObjectName("actionURL_GB2312_decode")
        self.actionUnicode_encode = QtWidgets.QAction(MainWindow)
        self.actionUnicode_encode.setObjectName("actionUnicode_encode")
        self.actionUnicode_decode = QtWidgets.QAction(MainWindow)
        self.actionUnicode_decode.setObjectName("actionUnicode_decode")
        self.actionEscape_U_encode = QtWidgets.QAction(MainWindow)
        self.actionEscape_U_encode.setObjectName("actionEscape_U_encode")
        self.actionEscape_U_decode = QtWidgets.QAction(MainWindow)
        self.actionEscape_U_decode.setObjectName("actionEscape_U_decode")
        self.actionHtmlEncode_encode = QtWidgets.QAction(MainWindow)
        self.actionHtmlEncode_encode.setObjectName("actionHtmlEncode_encode")
        self.actionHtmlEncode_decode = QtWidgets.QAction(MainWindow)
        self.actionHtmlEncode_decode.setObjectName("actionHtmlEncode_decode")
        self.actionASCII_encode = QtWidgets.QAction(MainWindow)
        self.actionASCII_encode.setObjectName("actionASCII_encode")
        self.actionASCII_decode = QtWidgets.QAction(MainWindow)
        self.actionASCII_decode.setObjectName("actionASCII_decode")
        self.actionBase64_encode = QtWidgets.QAction(MainWindow)
        self.actionBase64_encode.setObjectName("actionBase64_encode")
        self.actionBase64_decode = QtWidgets.QAction(MainWindow)
        self.actionBase64_decode.setObjectName("actionBase64_decode")
        self.actionStr_Hex_encode = QtWidgets.QAction(MainWindow)
        self.actionStr_Hex_encode.setObjectName("actionStr_Hex_encode")
        self.actionHex_Str_decode = QtWidgets.QAction(MainWindow)
        self.actionHex_Str_decode.setObjectName("actionHex_Str_decode")
        self.actionPlugins_manager = QtWidgets.QAction(MainWindow)
        self.actionPlugins_manager.setObjectName("actionPlugins_manager")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGithub = QtWidgets.QAction(MainWindow)
        self.actionGithub.setObjectName("actionGithub")
        self.action_kaisa_encrypt = QtWidgets.QAction(MainWindow)
        self.action_kaisa_encrypt.setObjectName("action_kaisa_encrypt")
        self.action_kaisa_decrypt = QtWidgets.QAction(MainWindow)
        self.action_kaisa_decrypt.setObjectName("action_kaisa_decrypt")
        self.actionRot13_encrypt = QtWidgets.QAction(MainWindow)
        self.actionRot13_encrypt.setObjectName("actionRot13_encrypt")
        self.actionRot13_decrypt = QtWidgets.QAction(MainWindow)
        self.actionRot13_decrypt.setObjectName("actionRot13_decrypt")
        self.action_zhalan_encrypt = QtWidgets.QAction(MainWindow)
        self.action_zhalan_encrypt.setObjectName("action_zhalan_encrypt")
        self.action_zhalan_decrypt = QtWidgets.QAction(MainWindow)
        self.action_zhalan_decrypt.setObjectName("action_zhalan_decrypt")
        self.action_zhujuan_encrypt = QtWidgets.QAction(MainWindow)
        self.action_zhujuan_encrypt.setObjectName("action_zhujuan_encrypt")
        self.action_zhujuan = QtWidgets.QAction(MainWindow)
        self.action_zhujuan.setObjectName("action_zhujuan")
        self.action_mosi_encrypt = QtWidgets.QAction(MainWindow)
        self.action_mosi_encrypt.setObjectName("action_mosi_encrypt")
        self.action_mosi_decrypt = QtWidgets.QAction(MainWindow)
        self.action_mosi_decrypt.setObjectName("action_mosi_decrypt")
        self.action_weinijiya_encrypt = QtWidgets.QAction(MainWindow)
        self.action_weinijiya_encrypt.setObjectName("action_weinijiya_encrypt")
        self.action_weinijiya_decrypt = QtWidgets.QAction(MainWindow)
        self.action_weinijiya_decrypt.setObjectName("action_weinijiya_decrypt")
        self.action_peigen_encrypt = QtWidgets.QAction(MainWindow)
        self.action_peigen_encrypt.setObjectName("action_peigen_encrypt")
        self.action_peihen_decrypt = QtWidgets.QAction(MainWindow)
        self.action_peihen_decrypt.setObjectName("action_peihen_decrypt")
        self.action_yiwei_decrypt = QtWidgets.QAction(MainWindow)
        self.action_yiwei_decrypt.setObjectName("action_yiwei_decrypt")
        self.action_xier_encrypt = QtWidgets.QAction(MainWindow)
        self.action_xier_encrypt.setObjectName("action_xier_encrypt")
        self.actionXXencode = QtWidgets.QAction(MainWindow)
        self.actionXXencode.setObjectName("actionXXencode")
        self.actionXXencode_decode = QtWidgets.QAction(MainWindow)
        self.actionXXencode_decode.setObjectName("actionXXencode_decode")
        self.actionAAencode = QtWidgets.QAction(MainWindow)
        self.actionAAencode.setObjectName("actionAAencode")
        self.actionAAencode_decode = QtWidgets.QAction(MainWindow)
        self.actionAAencode_decode.setObjectName("actionAAencode_decode")
        self.actionUUencode = QtWidgets.QAction(MainWindow)
        self.actionUUencode.setObjectName("actionUUencode")
        self.actionUUencode_decode = QtWidgets.QAction(MainWindow)
        self.actionUUencode_decode.setObjectName("actionUUencode_decode")
        self.actionJJencode = QtWidgets.QAction(MainWindow)
        self.actionJJencode.setObjectName("actionJJencode")
        self.actionJJencode_decode = QtWidgets.QAction(MainWindow)
        self.actionJJencode_decode.setObjectName("actionJJencode_decode")
        self.actionJSfuck = QtWidgets.QAction(MainWindow)
        self.actionJSfuck.setObjectName("actionJSfuck")
        self.actionJSfuck_decode = QtWidgets.QAction(MainWindow)
        self.actionJSfuck_decode.setObjectName("actionJSfuck_decode")
        self.actionBase32_encode = QtWidgets.QAction(MainWindow)
        self.actionBase32_encode.setObjectName("actionBase32_encode")
        self.actionBase32_decode = QtWidgets.QAction(MainWindow)
        self.actionBase32_decode.setObjectName("actionBase32_decode")
        self.actionBase16_decode = QtWidgets.QAction(MainWindow)
        self.actionBase16_decode.setObjectName("actionBase16_decode")
        self.actionBase16_encode = QtWidgets.QAction(MainWindow)
        self.actionBase16_encode.setObjectName("actionBase16_encode")
        self.action_qiaoji = QtWidgets.QAction(MainWindow)
        self.action_qiaoji.setObjectName("action_qiaoji")
        self.action_qiaoji_decode = QtWidgets.QAction(MainWindow)
        self.action_qiaoji_decode.setObjectName("action_qiaoji_decode")
        self.action01248 = QtWidgets.QAction(MainWindow)
        self.action01248.setObjectName("action01248")
        self.action_yunying_encrypt = QtWidgets.QAction(MainWindow)
        self.action_yunying_encrypt.setObjectName("action_yunying_encrypt")
        self.action_yunxing_decrypt = QtWidgets.QAction(MainWindow)
        self.action_yunxing_decrypt.setObjectName("action_yunxing_decrypt")
        self.actionRot = QtWidgets.QAction(MainWindow)
        self.actionRot.setObjectName("actionRot")
        self.actionShellcode_encode = QtWidgets.QAction(MainWindow)
        self.actionShellcode_encode.setObjectName("actionShellcode_encode")
        self.actionShellcode_decode = QtWidgets.QAction(MainWindow)
        self.actionShellcode_decode.setObjectName("actionShellcode_decode")
        self.actionBrainfuck_Ook = QtWidgets.QAction(MainWindow)
        self.actionBrainfuck_Ook.setObjectName("actionBrainfuck_Ook")
        self.actionBrainfuck_Ook_decode = QtWidgets.QAction(MainWindow)
        self.actionBrainfuck_Ook_decode.setObjectName("actionBrainfuck_Ook_decode")
        self.action_dangpu_encrypt = QtWidgets.QAction(MainWindow)
        self.action_dangpu_encrypt.setObjectName("action_dangpu_encrypt")
        self.action_dangpu_decrypt = QtWidgets.QAction(MainWindow)
        self.action_dangpu_decrypt.setObjectName("action_dangpu_decrypt")
        self.actionRabbit_encrypt = QtWidgets.QAction(MainWindow)
        self.actionRabbit_encrypt.setObjectName("actionRabbit_encrypt")
        self.actionRabbit_decrypt = QtWidgets.QAction(MainWindow)
        self.actionRabbit_decrypt.setObjectName("actionRabbit_decrypt")
        self.action2_8 = QtWidgets.QAction(MainWindow)
        self.action2_8.setObjectName("action2_8")
        self.action2_10 = QtWidgets.QAction(MainWindow)
        self.action2_10.setObjectName("action2_10")
        self.action2_16 = QtWidgets.QAction(MainWindow)
        self.action2_16.setObjectName("action2_16")
        self.action2_32 = QtWidgets.QAction(MainWindow)
        self.action2_32.setObjectName("action2_32")
        self.action8_2 = QtWidgets.QAction(MainWindow)
        self.action8_2.setObjectName("action8_2")
        self.action8_10 = QtWidgets.QAction(MainWindow)
        self.action8_10.setObjectName("action8_10")
        self.action8_16 = QtWidgets.QAction(MainWindow)
        self.action8_16.setObjectName("action8_16")
        self.action16_2 = QtWidgets.QAction(MainWindow)
        self.action16_2.setObjectName("action16_2")
        self.action16_8 = QtWidgets.QAction(MainWindow)
        self.action16_8.setObjectName("action16_8")
        self.action16_10 = QtWidgets.QAction(MainWindow)
        self.action16_10.setObjectName("action16_10")
        self.action_others = QtWidgets.QAction(MainWindow)
        self.action_others.setObjectName("action_others")
        self.action10_2 = QtWidgets.QAction(MainWindow)
        self.action10_2.setObjectName("action10_2")
        self.action10_8 = QtWidgets.QAction(MainWindow)
        self.action10_8.setObjectName("action10_8")
        self.action10_16 = QtWidgets.QAction(MainWindow)
        self.action10_16.setObjectName("action10_16")
        self.actionOthers = QtWidgets.QAction(MainWindow)
        self.actionOthers.setObjectName("actionOthers")
        self.action_Plugins = QtWidgets.QAction(MainWindow)
        self.action_Plugins.setObjectName("action_Plugins")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.action_dangpu_decry = QtWidgets.QAction(MainWindow)
        self.action_dangpu_decry.setObjectName("action_dangpu_decry")
        self.menuEncode.addAction(self.actionURL_UTF8_encode)
        self.menuEncode.addAction(self.actionURL_GB2312_encode)
        self.menuEncode.addAction(self.actionUnicode_encode)
        self.menuEncode.addAction(self.actionEscape_U_encode)
        self.menuEncode.addAction(self.actionHtmlEncode_encode)
        self.menuEncode.addAction(self.actionASCII_encode)
        self.menuEncode.addAction(self.actionBase16_encode)
        self.menuEncode.addAction(self.actionBase32_encode)
        self.menuEncode.addAction(self.actionBase64_encode)
        self.menuEncode.addAction(self.actionStr_Hex_encode)
        self.menuEncode.addAction(self.actionShellcode_encode)
        self.menuDecode.addAction(self.actionURL_UTF8_decode)
        self.menuDecode.addAction(self.actionURL_GB2312_decode)
        self.menuDecode.addAction(self.actionUnicode_decode)
        self.menuDecode.addAction(self.actionEscape_U_decode)
        self.menuDecode.addAction(self.actionHtmlEncode_decode)
        self.menuDecode.addAction(self.actionASCII_decode)
        self.menuDecode.addAction(self.actionBase16_decode)
        self.menuDecode.addAction(self.actionBase32_decode)
        self.menuDecode.addAction(self.actionBase64_decode)
        self.menuDecode.addAction(self.actionHex_Str_decode)
        self.menuDecode.addAction(self.actionShellcode_decode)
        self.menuEncrypt.addAction(self.actionRot13_encrypt)
        self.menuEncrypt.addAction(self.action_kaisa_encrypt)
        self.menuEncrypt.addAction(self.action_zhalan_encrypt)
        self.menuEncrypt.addAction(self.action_peigen_encrypt)
        self.menuEncrypt.addAction(self.action_mosi_encrypt)
        self.menuEncrypt.addAction(self.action_yunying_encrypt)
        self.menuEncrypt.addAction(self.action_dangpu_encrypt)
        self.menuEncrypt.addAction(self.action_weinijiya_encrypt)
        self.menuDecrypt.addAction(self.actionRot13_decrypt)
        self.menuDecrypt.addAction(self.action_kaisa_decrypt)
        self.menuDecrypt.addAction(self.action_zhalan_decrypt)
        self.menuDecrypt.addAction(self.action_peihen_decrypt)
        self.menuDecrypt.addAction(self.action_mosi_decrypt)
        self.menuDecrypt.addAction(self.action_yiwei_decrypt)
        self.menuDecrypt.addAction(self.action_yunxing_decrypt)
        self.menuDecrypt.addAction(self.action_dangpu_decry)
        self.menuDecrypt.addAction(self.action_weinijiya_decrypt)
        self.menuBinary.addAction(self.action2_8)
        self.menuBinary.addAction(self.action2_10)
        self.menuBinary.addAction(self.action2_16)
        self.menuBinary.addAction(self.action8_2)
        self.menuBinary.addAction(self.action8_10)
        self.menuBinary.addAction(self.action8_16)
        self.menuBinary.addAction(self.action10_2)
        self.menuBinary.addAction(self.action10_8)
        self.menuBinary.addAction(self.action10_16)
        self.menuBinary.addAction(self.action16_2)
        self.menuBinary.addAction(self.action16_8)
        self.menuBinary.addAction(self.action16_10)
        self.menuBinary.addAction(self.action_others)
        self.menuOthers.addAction(self.actionAbout)
        self.menuOthers.addAction(self.actionAuthor)
        self.menu.addAction(self.actionJSfuck)
        self.menu.addAction(self.actionAAencode)
        self.menu.addAction(self.actionXXencode)
        self.menu.addAction(self.actionJJencode)
        self.menu.addAction(self.actionUUencode)
        self.menu.addAction(self.actionBrainfuck_Ook)
        self.menu.addAction(self.action_qiaoji)
        self.menu.addAction(self.action_zhujuan)
        self.menu.addAction(self.actionOthers)
        self.menuBar.addAction(self.menuEncode.menuAction())
        self.menuBar.addAction(self.menuDecode.menuAction())
        self.menuBar.addAction(self.menuEncrypt.menuAction())
        self.menuBar.addAction(self.menuDecrypt.menuAction())
        self.menuBar.addAction(self.menuBinary.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menuOthers.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Source_text, self.Result_text)
        MainWindow.setTabOrder(self.Result_text, self.Source_tihuan_source)
        MainWindow.setTabOrder(self.Source_tihuan_source, self.Source_tihuan_result)
        MainWindow.setTabOrder(self.Source_tihuan_result, self.Result_tihuan_source)
        MainWindow.setTabOrder(self.Result_tihuan_source, self.Result_tihuan_result)
        MainWindow.setTabOrder(self.Result_tihuan_result, self.Source_tihuan_Button)
        MainWindow.setTabOrder(self.Source_tihuan_Button, self.Source_clear_Button)
        MainWindow.setTabOrder(self.Source_clear_Button, self.Source_Copy_Button)
        MainWindow.setTabOrder(self.Source_Copy_Button, self.Source_Paste_Button)
        MainWindow.setTabOrder(self.Source_Paste_Button, self.Result_tihuan_Button)
        MainWindow.setTabOrder(self.Result_tihuan_Button, self.Result_clear_Button)
        MainWindow.setTabOrder(self.Result_clear_Button, self.Result_Copy_Button)
        MainWindow.setTabOrder(self.Result_Copy_Button, self.Result_Paste_Button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CTF Tools  By qianxiao996  "))
        self.source_text.setText(_translate("MainWindow", "Source"))
        self.label2_5.setText(_translate("MainWindow", "Replace"))
        self.result_text.setText(_translate("MainWindow", "Result"))
        self.label2_6.setText(_translate("MainWindow", "Replace"))
        self.Result_tihuan_Button.setText(_translate("MainWindow", "Replace"))
        self.Result_clear_Button.setText(_translate("MainWindow", "Clear"))
        self.Result_Copy_Button.setText(_translate("MainWindow", "Copy"))
        self.Result_Paste_Button.setText(_translate("MainWindow", "Paste"))
        self.Source_tihuan_Button.setText(_translate("MainWindow", "Replace"))
        self.Source_clear_Button.setText(_translate("MainWindow", "Clear"))
        self.Source_Copy_Button.setText(_translate("MainWindow", "Copy"))
        self.Source_Paste_Button.setText(_translate("MainWindow", "Paste"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuEncode.setTitle(_translate("MainWindow", "Encode"))
        self.menuDecode.setTitle(_translate("MainWindow", "Decode"))
        self.menuEncrypt.setTitle(_translate("MainWindow", "Encrypt"))
        self.menuDecrypt.setTitle(_translate("MainWindow", "Decrypt"))
        self.menuBinary.setTitle(_translate("MainWindow", "Binary"))
        self.menuOthers.setTitle(_translate("MainWindow", "About"))
        self.menu.setTitle(_translate("MainWindow", "Others"))
        self.actionURL_UTF8.setText(_translate("MainWindow", "URL-UTF8 Encode"))
        self.actionURL_GB2312.setText(_translate("MainWindow", "URL-GB2312 Encode"))
        self.actionUnicode.setText(_translate("MainWindow", "Unicode Encode"))
        self.actionEscape_U.setText(_translate("MainWindow", "Escape(%U)"))
        self.actionHtmlEncode.setText(_translate("MainWindow", "HtmlEncode"))
        self.actionASCII.setText(_translate("MainWindow", "ASCII"))
        self.actionBase64.setText(_translate("MainWindow", "Base64"))
        self.actionStr_Hex.setText(_translate("MainWindow", "Str-Hex"))
        self.actionURL_UTF8_encode.setText(_translate("MainWindow", "URL-UTF8"))
        self.actionURL_UTF8_decode.setText(_translate("MainWindow", "URL-UTF8"))
        self.actionURL_GB2312_encode.setText(_translate("MainWindow", "URL-GB2312"))
        self.actionURL_GB2312_decode.setText(_translate("MainWindow", "URL-GB2312"))
        self.actionUnicode_encode.setText(_translate("MainWindow", "Unicode"))
        self.actionUnicode_decode.setText(_translate("MainWindow", "Unicode"))
        self.actionEscape_U_encode.setText(_translate("MainWindow", "Escape(%U)"))
        self.actionEscape_U_decode.setText(_translate("MainWindow", "Escape(%U)"))
        self.actionHtmlEncode_encode.setText(_translate("MainWindow", "HtmlEncode"))
        self.actionHtmlEncode_decode.setText(_translate("MainWindow", "HtmlEncode"))
        self.actionASCII_encode.setText(_translate("MainWindow", "ASCII"))
        self.actionASCII_decode.setText(_translate("MainWindow", "ASCII"))
        self.actionBase64_encode.setText(_translate("MainWindow", "Base64"))
        self.actionBase64_decode.setText(_translate("MainWindow", "Base64"))
        self.actionStr_Hex_encode.setText(_translate("MainWindow", "Str-Hex"))
        self.actionHex_Str_decode.setText(_translate("MainWindow", "Hex-Str"))
        self.actionPlugins_manager.setText(_translate("MainWindow", "Plugins Manager"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionGithub.setText(_translate("MainWindow", "Github"))
        self.action_kaisa_encrypt.setText(_translate("MainWindow", "凯撒密码"))
        self.action_kaisa_decrypt.setText(_translate("MainWindow", "凯撒密码"))
        self.actionRot13_encrypt.setText(_translate("MainWindow", "Rot13"))
        self.actionRot13_decrypt.setText(_translate("MainWindow", "Rot13"))
        self.action_zhalan_encrypt.setText(_translate("MainWindow", "栅栏密码"))
        self.action_zhalan_decrypt.setText(_translate("MainWindow", "栅栏密码"))
        self.action_zhujuan_encrypt.setText(_translate("MainWindow", "猪圈密码"))
        self.action_zhujuan.setText(_translate("MainWindow", "猪圈密码"))
        self.action_mosi_encrypt.setText(_translate("MainWindow", "摩斯密码"))
        self.action_mosi_decrypt.setText(_translate("MainWindow", "摩斯密码"))
        self.action_weinijiya_encrypt.setText(_translate("MainWindow", "维吉尼亚密码"))
        self.action_weinijiya_decrypt.setText(_translate("MainWindow", "维吉尼亚密码"))
        self.action_peigen_encrypt.setText(_translate("MainWindow", "培根密码"))
        self.action_peihen_decrypt.setText(_translate("MainWindow", "培根密码"))
        self.action_yiwei_decrypt.setText(_translate("MainWindow", "移位密码"))
        self.action_xier_encrypt.setText(_translate("MainWindow", "希尔密码"))
        self.actionXXencode.setText(_translate("MainWindow", "XXencode"))
        self.actionXXencode_decode.setText(_translate("MainWindow", "XXencode"))
        self.actionAAencode.setText(_translate("MainWindow", "AAencode"))
        self.actionAAencode_decode.setText(_translate("MainWindow", "AAencode"))
        self.actionUUencode.setText(_translate("MainWindow", "UUencode"))
        self.actionUUencode_decode.setText(_translate("MainWindow", "UUencode"))
        self.actionJJencode.setText(_translate("MainWindow", "JJencode"))
        self.actionJJencode_decode.setText(_translate("MainWindow", "JJencode"))
        self.actionJSfuck.setText(_translate("MainWindow", "JSfuck"))
        self.actionJSfuck_decode.setText(_translate("MainWindow", "JSfuck"))
        self.actionBase32_encode.setText(_translate("MainWindow", "Base32"))
        self.actionBase32_decode.setText(_translate("MainWindow", "Base32"))
        self.actionBase16_decode.setText(_translate("MainWindow", "Base16"))
        self.actionBase16_encode.setText(_translate("MainWindow", "Base16"))
        self.action_qiaoji.setText(_translate("MainWindow", "敲击码"))
        self.action_qiaoji_decode.setText(_translate("MainWindow", "敲击码"))
        self.action01248.setText(_translate("MainWindow", "01248"))
        self.action_yunying_encrypt.setText(_translate("MainWindow", "云影密码"))
        self.action_yunxing_decrypt.setText(_translate("MainWindow", "云影密码"))
        self.actionRot.setText(_translate("MainWindow", "Rot"))
        self.actionShellcode_encode.setText(_translate("MainWindow", "Shellcode"))
        self.actionShellcode_decode.setText(_translate("MainWindow", "Shellcode"))
        self.actionBrainfuck_Ook.setText(_translate("MainWindow", "Brainfuck/Ook!"))
        self.actionBrainfuck_Ook_decode.setText(_translate("MainWindow", "Brainfuck/Ook!"))
        self.action_dangpu_encrypt.setText(_translate("MainWindow", "当铺密码"))
        self.action_dangpu_decrypt.setText(_translate("MainWindow", "当铺密码"))
        self.actionRabbit_encrypt.setText(_translate("MainWindow", "Rabbit"))
        self.actionRabbit_decrypt.setText(_translate("MainWindow", "Rabbit"))
        self.action2_8.setText(_translate("MainWindow", "2->8"))
        self.action2_10.setText(_translate("MainWindow", "2->10"))
        self.action2_16.setText(_translate("MainWindow", "2->16"))
        self.action2_32.setText(_translate("MainWindow", "2->32"))
        self.action8_2.setText(_translate("MainWindow", "8->2"))
        self.action8_10.setText(_translate("MainWindow", "8->10"))
        self.action8_16.setText(_translate("MainWindow", "8->16"))
        self.action16_2.setText(_translate("MainWindow", "16->2"))
        self.action16_8.setText(_translate("MainWindow", "16->8"))
        self.action16_10.setText(_translate("MainWindow", "16->10"))
        self.action_others.setText(_translate("MainWindow", "自定义"))
        self.action10_2.setText(_translate("MainWindow", "10->2"))
        self.action10_8.setText(_translate("MainWindow", "10->8"))
        self.action10_16.setText(_translate("MainWindow", "10->16"))
        self.actionOthers.setText(_translate("MainWindow", "在线网站"))
        self.action_Plugins.setText(_translate("MainWindow", "插件管理"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionAuthor.setText(_translate("MainWindow", "Author"))
        self.action_dangpu_decry.setText(_translate("MainWindow", "当铺密码"))

