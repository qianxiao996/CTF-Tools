# coding=utf-8
import base64
import binascii
import configparser
import importlib.machinery
import os
import random
import sys

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import webbrowser
import qdarkstyle
import requests
from PyQt5.QtCore import QTranslator, QCoreApplication, QEvent
from qdarkstyle import LightPalette
from module.CipherAnalyse import Cipher_Thread
from module.AutoGetFlag import  AutoGetFlag
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pyperclip
import json
from GUI.main import Ui_MainWindow
from GUI.KEY_1 import Ui_KEY1
from GUI.KEY_2 import Ui_KEY2
from GUI.Cipher import Ui_Cipher
import frozen_dir
from module.func_binary import Class_Binary
from module.func_decode import Class_Decode
from module.func_encrypt import Class_Encrypt
from module.func_encode import Class_Encode
from module.func_tools import Class_Tools
from module.func_decrypt import Class_Decrypt
from QWidget_XiandaiMima import QWidget_XiandaiMima

SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)
version = '1.3.7'
update_time = '20220721'


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.about_text = "\t\t\tAbout\n       此程序为CTF密码学辅助工具，可进行常见的编码、解码、加密、解密操作，请勿非法使用！\n\t\t\tPowered by qianxiao996"
        self.author_text = "作者邮箱：qianxiao996@126.com\nGithub：https://github.com/qianxiao996"
        self.load_config()
        self.setWindowTitle('CTF-Tools V ' + version + ' ' + update_time + ' By qianxiao996 ')
        # self.setFixedSize(self.width(), self.height()) ##设置宽高不可变
        self.setWindowIcon(QtGui.QIcon('./logo.ico'))
        self.Ui.Source_clear_Button.clicked.connect(lambda: self.Ui.Source_text.clear())  # clear_source
        self.Ui.Result_clear_Button.clicked.connect(lambda: self.Ui.Result_text.clear())  # clear_result
        self.Ui.Source_Copy_Button.clicked.connect(lambda: self.Copy_text('Source'))  # copy_source
        self.Ui.Result_Copy_Button.clicked.connect(lambda: self.Copy_text('result'))  # copy_result
        self.Ui.Source_Paste_Button.clicked.connect(lambda: self.paste('Source'))  # paste_Source
        self.Ui.zhuanyuan.clicked.connect(self.zhuan_yuanwenben)  # paste_result
        # encode
        self.Ui.actionURL_encode.triggered.connect(lambda: self.gogogo('url'))
        self.Ui.actionUnicode_encode.triggered.connect(lambda: self.gogogo('unicode'))
        self.Ui.actionEscape_U_encode.triggered.connect(lambda: self.gogogo('escape_u'))
        self.Ui.actionHtmlEncode_encode.triggered.connect(lambda: self.gogogo('html'))
        self.Ui.actionASCII_2_encode.triggered.connect(lambda: self.gogogo('ASCII_2'))
        self.Ui.actionASCII_8_encode.triggered.connect(lambda: self.gogogo('ASCII_8'))
        self.Ui.actionASCII_10_encode.triggered.connect(lambda: self.gogogo('ASCII_10'))
        self.Ui.actionASCII_16_encode.triggered.connect(lambda: self.gogogo('ASCII_16'))
        self.Ui.actionBase16_encode.triggered.connect(lambda: self.gogogo('base16'))
        self.Ui.actionBase32_encode.triggered.connect(lambda: self.gogogo('base32'))
        self.Ui.actionBase36_encode.triggered.connect(lambda: self.gogogo('base36'))
        self.Ui.actionBase58_encode.triggered.connect(lambda: self.gogogo('base58'))
        self.Ui.actionBase62_encode.triggered.connect(lambda: self.gogogo('base62'))
        self.Ui.actionBase64_encode.triggered.connect(lambda: self.gogogo('base64'))
        self.Ui.actionBase64_2_encode.triggered.connect(
            lambda: self.UI_KEY1('base64_zidingyi', 'Encode', "base64自定义", "请输入编码表:"))
        self.Ui.actionBase85_ASCII85_encode.triggered.connect(lambda: self.gogogo('bae85_ASCII85'))
        self.Ui.actionBase85_RFC1924_encode.triggered.connect(lambda: self.gogogo('bae85_RFC1924'))
        self.Ui.actionBase91_encode.triggered.connect(lambda: self.gogogo('base91'))
        self.Ui.actionBase92_encode.triggered.connect(lambda: self.gogogo('base92'))
        self.Ui.actionStr_Hex_encode.triggered.connect(lambda: self.gogogo('Str_Hex'))
        self.Ui.actionShellcode_encode.triggered.connect(lambda: self.gogogo('shellcode'))
        self.Ui.actionQwerty_encode.triggered.connect(lambda: self.gogogo('qwerty'))
        self.Ui.actiontupian_base64_encode.triggered.connect(self.img_base64_encode)
        self.Ui.actiontupian_hex_encode.triggered.connect(self.img_hex_encode)
        self.Ui.actionJsFuck_encode.triggered.connect(lambda: self.gogogo('jsfuck'))
        self.Ui.actionJJEncode_encode.triggered.connect(lambda: self.gogogo('jjencode'))
        self.Ui.actionAAEncode_encode.triggered.connect(lambda: self.gogogo('aaencode'))
        self.Ui.actionSocialism_encode.triggered.connect(lambda: self.gogogo('Socialism'))
        self.Ui.actionjother_encode.triggered.connect(lambda: self.gogogo('jother'))
        self.Ui.actionbaijiaxing_encode.triggered.connect(lambda: self.gogogo('baijiaxing'))

        # decode
        self.Ui.actionURL_decode.triggered.connect(lambda: self.gogogo('url', 'Decode'))
        self.Ui.actionUnicode_decode.triggered.connect(lambda: self.gogogo('unicode', 'Decode'))
        self.Ui.actionEscape_U_decode.triggered.connect(lambda: self.gogogo('escape_u', 'Decode'))
        self.Ui.actionHtmlEncode_decode.triggered.connect(lambda: self.gogogo('html', 'Decode'))
        self.Ui.actionASCII_2_decode.triggered.connect(lambda: self.gogogo('ASCII_2', 'Decode'))
        self.Ui.actionASCII_8_decode.triggered.connect(lambda: self.gogogo('ASCII_8', 'Decode'))
        self.Ui.actionASCII_10_decode.triggered.connect(lambda: self.gogogo('ASCII_10', 'Decode'))
        self.Ui.actionASCII_16_decode.triggered.connect(lambda: self.gogogo('ASCII_16', 'Decode'))
        self.Ui.actionJsFuck_decode.triggered.connect(lambda: self.gogogo('jsfuck', 'Decode'))
        self.Ui.actionJJEncode_decode.triggered.connect(lambda: self.gogogo('jjencode', 'Decode'))
        self.Ui.actionAAEncode_decode.triggered.connect(lambda: self.gogogo('aaencode', 'Decode'))
        self.Ui.actionBase16_decode.triggered.connect(lambda: self.gogogo('base16', 'Decode'))
        self.Ui.actionBase32_decode.triggered.connect(lambda: self.gogogo('base32', 'Decode'))
        self.Ui.actionBase36_decode.triggered.connect(lambda: self.gogogo('base36', 'Decode'))
        self.Ui.actionBase58_decode.triggered.connect(lambda: self.gogogo('base58', 'Decode'))
        self.Ui.actionBase62_decode.triggered.connect(lambda: self.gogogo('base62', 'Decode'))
        self.Ui.actionBase64_decode.triggered.connect(lambda: self.gogogo('base64', 'Decode'))
        self.Ui.actionBase64_2_decode.triggered.connect(
            lambda: self.UI_KEY1('base64_zidingyi', 'Decode', "base64自定义", "请输入编码表:"))
        self.Ui.actionBase85_ASCII85_decode.triggered.connect(lambda: self.gogogo('bae85_ASCII85', 'Decode'))
        self.Ui.actionBase85_RFC1924_decode.triggered.connect(lambda: self.gogogo('bae85_RFC1924', 'Decode'))
        self.Ui.actionBase91_decode.triggered.connect(lambda: self.gogogo('base91', 'Decode'))
        self.Ui.actionBase92_decode.triggered.connect(lambda: self.gogogo('base92', 'Decode'))
        self.Ui.actionHex_Str_decode.triggered.connect(lambda: self.gogogo('Hex_Str', 'Decode'))
        self.Ui.actionShellcode_decode.triggered.connect(lambda: self.gogogo('shellcode', 'Decode'))
        self.Ui.actionQwerty_decode.triggered.connect(lambda: self.gogogo('qwerty', 'Decode'))
        self.Ui.actionbase64_tupian_decode.triggered.connect(self.base64_img_decode)
        self.Ui.actionhex_tupian_decode.triggered.connect(self.hex_img_decode)
        self.Ui.actionSocialism_decode.triggered.connect(lambda: self.gogogo('Socialism', 'Decode'))
        self.Ui.actionjother_decode.triggered.connect(lambda: self.gogogo('jother', 'Decode'))
        self.Ui.actionbaijiaxing_decode.triggered.connect(lambda: self.gogogo('baijiaxing', 'Decode'))

        # encrypt
        self.Ui.actionRot13_encrypt.triggered.connect(lambda: self.gogogo('rot13', 'Encrypt'))
        self.Ui.action_kaisa_encrypt.triggered.connect(lambda: self.gogogo('kaisa', 'Encrypt'))
        self.Ui.action_zhalan_encrypt.triggered.connect(lambda: self.UI_KEY1('zhalan', 'Encrypt', "栅栏密码", "请输入栏数:"))
        self.Ui.action_zhalan_w_encrypt.triggered.connect(
            lambda: self.UI_KEY1('zhalan_w', 'Encrypt', "栅栏密码(W型)", "请输入栏数:"))
        self.Ui.action_peigen_encrypt.triggered.connect(lambda: self.gogogo('peigen', 'Encrypt'))
        self.Ui.action_mosi_encrypt.triggered.connect(lambda: self.gogogo('mosi', 'Encrypt'))
        self.Ui.action_yunying_encrypt.triggered.connect(lambda: self.gogogo('yunying', 'Encrypt'))
        self.Ui.action_dangpu_encrypt.triggered.connect(lambda: self.gogogo('dangpu', 'Encrypt'))
        self.Ui.action_sifang_encrypt.triggered.connect(
            lambda: self.UI_KEY2('sifang', 'Encrypt', "四方密码", "Key square 1:", "Key square 2:"))
        self.Ui.action_weinijiya_encrypt.triggered.connect(
            lambda: self.UI_KEY1('vigenere', 'Encrypt', "维吉尼亚密码", "Keyword:"))
        self.Ui.action_Atbash_encrypt.triggered.connect(lambda: self.gogogo('atbash', 'Encrypt'))
        self.Ui.action_fangshe_encrypt.triggered.connect(lambda: self.UI_KEY2('fangshe', 'Encrypt', "仿射密码", "a:", "b:"))
        self.Ui.action_yufolunchan_v2_encrypt.triggered.connect(
            lambda: self.UI_KEY1('yufolunchan_v2', 'Encrypt', "与佛论禅 v2.0", "箴言:"))
        self.Ui.actionADFGX_encrypt.triggered.connect(lambda: self.gogogo('Polybius', 'Encrypt'))
        self.Ui.actiona1z26_encrypt.triggered.connect(lambda: self.gogogo('a1z26', 'Encrypt'))

        # decrypt
        self.Ui.actionRot5_decrypt.triggered.connect(lambda: self.gogogo('rot5', 'Decrypt'))
        self.Ui.actionRot13_decrypt.triggered.connect(lambda: self.gogogo('rot13', 'Decrypt'))
        self.Ui.actionRot18_decrypt.triggered.connect(lambda: self.gogogo('rot18', 'Decrypt'))
        self.Ui.actionRot47_decrypt.triggered.connect(lambda: self.gogogo('rot47', 'Decrypt'))
        self.Ui.action_kaisa_decrypt.triggered.connect(lambda: self.gogogo('kaisa', 'Decrypt'))
        self.Ui.action_zhalan_decrypt.triggered.connect(lambda: self.gogogo('zhalan', 'Decrypt'))
        self.Ui.action_zhalan_w_decrypt.triggered.connect(lambda: self.gogogo('zhalan_w', 'Decrypt'))
        self.Ui.action_peihen_decrypt.triggered.connect(lambda: self.gogogo('peigen', 'Decrypt'))
        self.Ui.action_mosi_decrypt.triggered.connect(lambda: self.gogogo('mosi', 'Decrypt'))
        self.Ui.action_yiwei_decrypt.triggered.connect(lambda: self.gogogo('yiwei', 'Decrypt'))
        self.Ui.action_yunxing_decrypt.triggered.connect(lambda: self.gogogo('yunying', 'Decrypt'))
        self.Ui.action_dangpu_decry.triggered.connect(lambda: self.gogogo('dangpu', 'Decrypt'))
        self.Ui.action_sifang_decrypt.triggered.connect(
            lambda: self.UI_KEY2('sifang', 'Decrypt', "四方密码", "Key square 1:", "Key square 2:"))
        self.Ui.action_weinijiya_decrypt.triggered.connect(
            lambda: self.UI_KEY1('vigenere', 'Decrypt', "维吉尼亚密码", "Keyword:"))
        self.Ui.action_Atbash_decrypt.triggered.connect(lambda: self.gogogo('atbash', 'Decrypt'))
        self.Ui.action_fangshe_decrypt.triggered.connect(lambda: self.UI_KEY2('fangshe', 'Decrypt', "仿射密码", "a:", "b:"))
        self.Ui.action_yufolunchan_v1_decrypt.triggered.connect(lambda: self.gogogo('yufolunchan_v1', 'Decrypt'))
        self.Ui.action_yufolunchan_v2_decrypt.triggered.connect(
            lambda: self.UI_KEY1('yufolunchan_v2', 'Decrypt', "与佛论禅 v2.0", "箴言:"))
        self.Ui.action_ADFGX_decrypt.triggered.connect(lambda: self.gogogo('Polybius', 'Decrypt'))
        self.Ui.actiona1z26_decrypt.triggered.connect(lambda: self.gogogo('a1z26', 'Decrypt'))

        # 进制转换
        self.Ui.action2_8.triggered.connect(lambda: self.Binary_gogogo('2_8'))
        self.Ui.action2_10.triggered.connect(lambda: self.Binary_gogogo('2_10'))
        self.Ui.action2_16.triggered.connect(lambda: self.Binary_gogogo('2_16'))
        self.Ui.action8_2.triggered.connect(lambda: self.Binary_gogogo('8_2'))
        self.Ui.action8_10.triggered.connect(lambda: self.Binary_gogogo('8_10'))
        self.Ui.action8_16.triggered.connect(lambda: self.Binary_gogogo('8_16'))
        self.Ui.action10_2.triggered.connect(lambda: self.Binary_gogogo('10_2'))
        self.Ui.action10_8.triggered.connect(lambda: self.Binary_gogogo('10_8'))
        self.Ui.action10_16.triggered.connect(lambda: self.Binary_gogogo('10_16'))
        self.Ui.action16_2.triggered.connect(lambda: self.Binary_gogogo('16_2'))
        self.Ui.action16_8.triggered.connect(lambda: self.Binary_gogogo('16_8'))
        self.Ui.action16_10.triggered.connect(lambda: self.Binary_gogogo('16_10'))
        self.Ui.action_others.triggered.connect(
            lambda: self.UI_KEY2('renyijinzhi_zhuanhuan', 'Binary', "任意进制转换", "转换前进制:", "转换后进制:"))
        self.Ui.actionAbout.triggered.connect(self.about)
        self.Ui.actionAuthor.triggered.connect(self.author)
        self.Ui.actionUpdate_2.triggered.connect(self.Update)

        self.Ui.miwenfenxi.clicked.connect(self.miwenfenxi)  # 一键解码
        self.Ui.auto_get_flag.clicked.connect(self.auto_get_flag)  # 一键解码

        # self.Ui.yijian_decode.clicked.connect(self.yijian_decode)  # 一键解码
        # self.Ui.yijian_base.clicked.connect(self.yijian_base)  # 一键base
        # self.Ui.yijian_decrypto.clicked.connect(self.yijian_decrypto)  # 一键解密
        # self.Ui.yijian_jinzhi.clicked.connect(self.yijian_jinzhi)  # 一键进制

        self.Ui.action_str_replace.triggered.connect(self.str_place)  # 字符串替换
        self.Ui.action_str_split.triggered.connect(
            lambda: self.UI_KEY1('str_split', 'Tools', "字符串分割", "请输入分隔符号:"))  # 字符串分割
        self.Ui.action_str_chaifen.triggered.connect(
            lambda: self.UI_KEY1('str_chaifen', 'Tools', "字符串长度拆分", "请输入字符串长度:"))  # 字符串拆分
        self.Ui.action_str_tongji.triggered.connect(lambda: self.gogogo('str_tongji', 'Tools'))  # 字符串统计
        self.Ui.action_str_re.triggered.connect(lambda: self.gogogo('str_re', 'Tools'))  # 字符串拆分
        self.Ui.action_str_xiaoxie.triggered.connect(
            lambda: self.Ui.Result_text.setPlainText(self.Ui.Source_text.toPlainText().lower()))  # 字符串全小写
        self.Ui.action_str_daxie.triggered.connect(
            lambda: self.Ui.Result_text.setPlainText(self.Ui.Source_text.toPlainText().upper()))  # 字符串全小写
        #
        self.Ui.tab_add.clicked.connect(self.add_Tab)  # 添加tab
        self.Ui.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.Ui.tabWidget.currentChanged.connect(self.onCurrentChanged)
        self.Ui.tabWidget.tabBar().installEventFilter(self)
        self.Ui.tabWidget.tabBar().previousMiddleIndex = -1

        self.Ui.xiandaimima.clicked.connect(self.open_xiandaimima)

        self.readfile()
        # Website
        websitemenubar = self.menuBar()  # 获取窗体的菜单栏
        Website = websitemenubar.addMenu("在线工具")
        for i in json_data:
            impMenu = QMenu(i, self)
            url_list = json_data[i]
            for key in url_list.keys():
                sub_action = QAction(QIcon(''), key, self)
                impMenu.addAction(sub_action)
            Website.addMenu(impMenu)
        Website.triggered[QAction].connect(self.show_json)
        # Plugins
        Pluginsmenubar = self.menuBar()  # 获取窗体的菜单栏
        plugins = Pluginsmenubar.addMenu("插件")
        for k in plugins_data:
            # print(k)
            sub_action = QAction(QIcon(''), k, self)
            plugins.addAction(sub_action)
        plugins.triggered[QAction].connect(self.show_plugins)
        # Others
        othersmenubar = self.menuBar()  # 获取窗体的菜单栏
        others = othersmenubar.addMenu("其他")
        for j in ["关于", '作者', '更新']:
            sub_action = QAction(QIcon(''), j, self)
            others.addAction(sub_action)
        impMenu = QMenu("皮肤", self)
        pifu_list = ['默认皮肤', '明亮风格', '暗黑风格']
        # for z in config_setup.options('QSS_List'):
        for z in pifu_list:
            sub_action = QAction(QIcon(''), z, self)
            impMenu.addAction(sub_action)
        others.addMenu(impMenu)
        others.triggered[QAction].connect(self.show_others)
        # 编码

    def get_text_list(self, text):
        text_list = []
        if self.Ui.checkBox_line.isChecked():
            text_list = text.splitlines()
        else:
            text_list.append(text)
        return text_list


    def out_result(self, text):
        self.Ui.Result_text.appendPlainText(text + '\n')

    def load_config(self):
        try:
            global config_setup
            # global qss_style
            # 实例化configParser对象
            config_setup = configparser.ConfigParser()
            # -read读取ini文件
            config_setup.read('config.ini', encoding='utf-8')
            if 'Skin' not in config_setup:  # 如果分组type不存在则插入type分组
                config_setup.add_section('Skin')
                config_setup.set("Skin", "default", '明亮风格')
                qss_Setup = '明亮风格'
            else:
                qss_Setup = config_setup.get('Skin', 'default')
            self.change_pifu(qss_Setup)
            # if 'QSS_Setup' not in config_setup:  # 如果分组type不存在则插入type分组
            #     config_setup.add_section('QSS_Setup')
            #     config_setup.set("QSS_Setup", "QSS", 'default.qss')
            #     config_setup.write(open('config.ini', "r+", encoding="utf-8"))  # r+模式
            #     qss_Setup = 'default.qss'
            # else:
            #     qss_Setup = config_setup.get('QSS_Setup', 'QSS')
            # with open("QSS/" + qss_Setup, 'r', encoding='utf-8') as f:
            #     qss_style = f.read()
            #     f.close()

            # MainWindows.setStyleSheet(self, qss_style)
            # f.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))
            pass

    def show_others(self, q):

        if q.text() == "关于":
            self.about()
            return
        elif q.text() == "作者":
            self.author()
            return
        elif q.text() == "更新":
            self.Update()
            return
        else:
            self.change_pifu(q.text())

            # try:
            # print(q.text())
            # filename = config_setup.get('QSS_List', q.text())
            # with open("QSS/" + filename, 'r', encoding='utf-8') as f:
            #     qss_style = f.read()
            #     f.close()
            # MainWindows.setStyleSheet(self, qss_style)
            # config_setup.set("QSS_Setup", "QSS", filename)
            # f.close()
            # python = sys.executable
            # os.execl(python, python, *sys.argv)
            # except Exception as e:
            #     QMessageBox.critical(self, 'Error', str(e))
            #     pass

    def change_pifu(self, q):
        config_setup.set("Skin", "default", q)
        if q == "默认皮肤":
            app.setStyleSheet('')
        elif q == "明亮风格":
            app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
        elif q == "暗黑风格":
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def show_plugins(self, q):
        try:
            self.plugins_methods = "Plugins/" + plugins_data[q.text()][:-3]
            self.plugins_filename = "Plugins/" + plugins_data[q.text()]
            text = self.Ui.Source_text.toPlainText()
            if text == '':
                self.Ui.Result_text.appendPlainText('请输入一个源字符串！')
                return 0
            self.Ui.Result_text.clear()
            nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(self.plugins_methods, self.plugins_filename).load_module()
            result = nnnnnnnnnnnn1.run(text,self.PLUGINS_UI_KEY1,self.PLUGINS_UI_KEY2)
            if result:
                self.Ui.Result_text.appendPlainText(str(result[1]))
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))
    def PLUGINS_UI_KEY1(self, func_name, title, label_text):
        text = self.Ui.Source_text.toPlainText()
        if len(text) <= 0:
            self.Ui.Result_text.appendPlainText('请输入一个源字符串！')
            return 0
        self.WChild = Ui_KEY1()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild.setupUi(self.dialog)
        self.dialog.setWindowTitle(title)
        self.WChild.label.setText(label_text)
        self.dialog.show()
        self.WChild.keyenter.clicked.connect(lambda:self.colse_key1(func_name))


    def colse_key1(self,func_name):
        self.dialog.close()
        self.Ui.Result_text.clear()
        text = self.Ui.Source_text.toPlainText()
        key1 = self.WChild.key.text().strip()

        nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(self.plugins_methods, self.plugins_filename).load_module()
        Function = getattr(nnnnnnnnnnnn1, func_name)  # 以字符串的形式执行函数
        result = Function(text,key1)
        self.Ui.Result_text.appendPlainText(str(result))
    def PLUGINS_UI_KEY2(self, func_name,title, label_text1, label_text2):
        text = self.Ui.Source_text.toPlainText()
        self.WChild = Ui_KEY2()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild.setupUi(self.dialog)
        self.dialog.setWindowTitle(title)
        self.WChild.key_1.setText(label_text1)
        self.WChild.key_2.setText(label_text2)
        self.dialog.show()
        self.WChild.enter.clicked.connect(lambda: self.colse_key2(func_name))
    def colse_key2(self,func_name):
        self.dialog.close()
        self.Ui.Result_text.clear()
        text = self.Ui.Source_text.toPlainText()
        key1 = self.WChild.Key1.text().strip()
        key2 = self.WChild.Key2.text().strip()
        nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(self.plugins_methods, self.plugins_filename).load_module()
        Function = getattr(nnnnnnnnnnnn1, func_name)  # 以字符串的形式执行函数
        result = Function(text,key1,key2)
        self.Ui.Result_text.appendPlainText(str(result))
    def show_json(self, q):
        try:
            othersmenubar = self.menuBar()  # 获取窗体的菜单栏
            #
            # print(i[1].menu().actions()[4].text())
            for i in othersmenubar.actions():
                # print(i.text())
                if i.text() == "在线工具":
                    # sub_action = i()
                    for j in i.menu().actions():
                        # print(j.text())
                        # 输出为关于软件、检查更新、意见反馈、皮肤风格
                        for k in j.menu().actions():
                            # print(k.text())
                            if k == q:
                                # print(j.text()+'|'+q.text())
                                if 'http://' in json_data[j.text()][q.text()] or 'https://' in json_data[j.text()][
                                    q.text()]:
                                    # print(q.text())
                                    pyperclip.copy(json_data[j.text()][q.text()])
                                    reply = QMessageBox.question(self, 'Message', "链接已复制到剪切板，是否在浏览器中打开链接?",
                                                                 QMessageBox.Yes | QMessageBox.No,
                                                                 QMessageBox.Yes)

                                    if reply == QMessageBox.Yes:
                                        webbrowser.open(json_data[j.text()][q.text()])
                                    else:
                                        pass
                                elif os.path.isfile(json_data[j.text()][q.text()]):
                                    dialog_fault = QDialog(self)
                                    lb = QLabel(dialog_fault)
                                    dialog_fault.setWindowTitle(q.text())
                                    # url_father = os.path.dirname(os.path.abspath(__file__))
                                    # image_path = url_father + "/fault_information.png"
                                    pic = QPixmap(json_data[j.text()][q.text()])
                                    lb.resize(pic.width(), pic.height())
                                    lb.setPixmap(pic.scaled(lb.size(), QtCore.Qt.IgnoreAspectRatio))
                                    # label_pic.setGeometry(10, 10, 1019, 537)
                                    dialog_fault.show()

                                else:
                                    pyperclip.copy(json_data[j.text()][q.text()])
                                    QMessageBox.information(self, 'Success', '链接已复制到剪切板')

                                return
                        #     else:
                        #         pass
                    # return
        except Exception as e:
            QMessageBox.critical(self, 'Error', '程序报错:' + str(e))
            pass

    def readfile(self):
        try:
            global json_data
            f = open('Plugins//data.json', 'r', encoding='utf-8')
            json_data = json.load(f)
            # print(json_data)
            f.close()
            # qss_Setup = config_setup.get('QSS_Setup', 'QSS')
            #
            # with open("QSS/" + qss_Setup, 'r', encoding='utf-8') as f:
            #     qss_style = f.read()
            #     f.close()
            # MainWindows.setStyleSheet(self, qss_style)
            # print(json_data)
            # f.close()
            global plugins_data
            f = open('Plugins/Plugins.json', 'r', encoding='utf-8')
            plugins_data = json.load(f)
            # print(plugins_data)
            f.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))
            pass

    # 图片转base64
    def img_base64_encode(self):
        try:
            self.Ui.Result_text.clear()
            filename = self.file_open(r"Text Files (*.jpg);;All files(*.*)")
            with open(filename, 'rb') as f:
                base64_data = base64.b64encode(f.read())
                s = base64_data.decode()
            self.Ui.Result_text.appendPlainText(str('data:image/%s;base64,%s' % (filename[-3:], s)))
            return 'exit'
        except:
            return ('转换失败！')

    # 图片转hex
    def img_hex_encode(self):
        try:
            self.Ui.Result_text.clear()
            encode_type = self.Ui.encode_type.currentText()
            filename = self.file_open(r"Text Files (*.jpg);;All files(*.*)")
            with open(filename, 'rb') as f:
                hex_data = f.read()
                hexstr = binascii.hexlify(hex_data).decode(encode_type)
                hexstr = hexstr.upper()
            self.Ui.Result_text.appendPlainText(str('%s' % (hexstr)))
            return 'exit'
        except:
            return ('转换失败！')

    def UI_KEY2(self, encode_name, encode_type, title, label_text1, label_text2):
        text = self.Ui.Source_text.toPlainText()
        if len(text) <= 0:
            self.Ui.Result_text.appendPlainText('请输入一个源字符串！')
            return 0
        self.WChild = Ui_KEY2()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild.setupUi(self.dialog)
        self.dialog.setWindowTitle(title)
        self.WChild.key_1.setText(label_text1)
        self.WChild.key_2.setText(label_text2)
        self.dialog.show()
        self.WChild.enter.clicked.connect(lambda: self.UI_KEY2_click_func(encode_name, encode_type))

    def UI_KEY2_click_func(self, func_name, class_name):
        self.dialog.close()
        try:
            self.Ui.Result_text.clear()
            text = self.Ui.Source_text.toPlainText()
            text_list = self.get_text_list(text)
            encode_type = self.Ui.encode_type.currentText()
            key1 = self.WChild.Key1.text().strip()
            key2 = self.WChild.Key2.text().strip()
            obj = eval('Class_' + class_name + '()')
            for text in text_list:
                status,result_text,type__ = getattr(obj, 'func_'+func_name)(encode_type, text, key1, key2)
                self.Ui.Result_text.appendPlainText(str(result_text).strip())
        except Exception as e:
            self.Ui.Result_text.appendPlainText(str(e))

    def UI_KEY1(self, encode_name, encode_type, title, label_text):
        text = self.Ui.Source_text.toPlainText()
        if len(text) <= 0:
            self.Ui.Result_text.appendPlainText('请输入一个源字符串！')
            return 0
        self.WChild = Ui_KEY1()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild.setupUi(self.dialog)
        self.dialog.setWindowTitle(title)
        self.WChild.label.setText(label_text)
        self.dialog.show()
        self.WChild.keyenter.clicked.connect(lambda: self.UI_KEY1_click_func(encode_name, encode_type))

    def UI_KEY1_click_func(self, func_name, class_name):
        self.dialog.close()
        try:
            self.Ui.Result_text.clear()
            text = self.Ui.Source_text.toPlainText()
            text_list = self.get_text_list(text)
            encode_type = self.Ui.encode_type.currentText()
            n = self.WChild.key.text().strip()
            obj = eval('Class_' + class_name + '()')
            for text in text_list:
                status,result_text,type__ = getattr(obj, 'func_'+func_name)(encode_type, text, n)
                self.Ui.Result_text.appendPlainText(str(result_text).strip())
        except Exception as e:
            self.Ui.Result_text.appendPlainText(str(e))

    def Binary_gogogo(self, Binary_type):
        try:
            self.Ui.Result_text.clear()
            text = self.Ui.Source_text.toPlainText()
            if len(text) <= 0:
                self.Ui.Result_text.appendPlainText('请输入一个源字符串！')
                return 0
            else:
                text_list = self.get_text_list(text)
            for text in text_list:
                status,result_text,type__ = getattr(Class_Binary(), 'exec_Binary')(text, Binary_type)
                self.Ui.Result_text.appendPlainText(str(result_text))
        except Exception as e:
            self.Ui.Result_text.appendPlainText(str(e))

    def gogogo(self, func_name, class_name="Encode"):
        try:
            self.Ui.Result_text.clear()
            text = self.Ui.Source_text.toPlainText().strip()
            if len(text) <= 0:
                self.Ui.Result_text.appendPlainText('请输入一个源字符串！')
                return 0
            else:
                text_list = self.get_text_list(text)
            encode_type = self.Ui.encode_type.currentText()
            obj = eval('Class_' + class_name + '()')
            for text in text_list:
                status,result_text,type__ = getattr(obj, 'func_'+func_name)(encode_type, text)
                self.Ui.Result_text.appendPlainText(str(result_text))
        except Exception as e:
            self.Ui.Result_text.appendPlainText(str(e))

    def base64_img_decode(self):
        try:
            text = self.Ui.Source_text.toPlainText().strip()
            file_name = self.file_save('tupian.jpg')
            # print(file_name)
            str2 = base64.b64decode(
                text.replace('data:image/jpg;base64,', '').replace('data:image/jpeg;base64,', '').replace(
                    'data:image/png;base64,', '').replace('data:image/gif;base64,', ''))
            file1 = open(file_name, 'wb')
            file1.write(str2)
            file1.close()
            QMessageBox.information(self, 'Success', '转换成功，文件位置:%s' % file_name)
            result_text = '转换成功，文件位置:\n%s' % file_name
        except:
            result_text = "转换失败！"
        return result_text

    def hex_img_decode(self):
        try:
            text = self.Ui.Source_text.toPlainText().strip()
            file_name = self.file_save('hextupian.jpg')
            # print(file_name)
            file1 = open(file_name, 'wb')
            pic = binascii.a2b_hex(text.encode())
            file1.write(pic)
            file1.close()
            QMessageBox.information(self, 'Success', '转换成功，文件位置:%s' % file_name)
            result_text = '转换成功，文件位置:\n%s' % file_name
        except:
            result_text = "转换失败！"
            pass
        return result_text

    def Copy_text(self, text):
        try:
            data = ''
            if text == 'Source':
                data = self.Ui.Source_text.toPlainText().strip()
            if text == 'result':
                data = self.Ui.Result_text.toPlainText()
            # 访问剪切板，存入值
            pyperclip.copy(data)
        except Exception as e:
            pass

    def paste(self, text):
        try:
            data = pyperclip.paste()
            if text == 'Source':
                # print(text)
                source_text = self.Ui.Source_text.toPlainText().strip()  #
                data = source_text + data
                self.Ui.Source_text.appendPlainText(data)
            if text == 'result':
                result_text = self.Ui.Result_text.toPlainText()  #
                data = result_text + data
                self.Ui.Result_text.appendPlainText(data)
        except Exception as e:
            # print(str(e))
            pass

    # 关于
    def about(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about(self, "关于", self.about_text)

    # 作者
    def author(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about(self, "作者", self.author_text)

    def Update(self):
        webbrowser.open("https://github.com/qianxiao996/CTF-Tools/releases")

    # 文件打开对话框
    def file_open(self, type):
        fileName, selectedFilter = QFileDialog.getOpenFileName(self, (r"上传文件"), (r""), type)
        return (fileName)  # 返回文件路径

    # 保存文件对话框
    def file_save(self, filename):
        fileName, filetype = QFileDialog.getSaveFileName(self, (r"保存文件"), (r'C:\Users\Administrator\\' + filename),
                                                         r"All files(*.*)")
        return fileName

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        try:
            config_setup.write(open('config.ini', "r+", encoding="utf-8"))  # r+模式
        except:
            QMessageBox.critical(self, 'False', "配置文件保存失败!")

    def keyPressEvent(self, event):
        # print("按下：" + str(event.key()))
        if event.key() == QtCore.Qt.Key_H:
            self.str_place()
            # if QApplication.keyboardModifiers() == Qt.ControlModifier:
            #     self.actionFile.save(self.action_text.toPlainText())
            #     self.status.showMessage("保存成功 %s" % self.file)

    def zhuan_yuanwenben(self):
        text = self.Ui.Result_text.toPlainText()
        if text:
            self.Ui.Source_text.setPlainText(text)

    def open_xiandaimima(self):
        self.w = QWidget_XiandaiMima()
        self.w.show()
        # self.form_xiandaimima = QtWidgets.QWidget()
        # self.xiandaimima_widget = XiandaiMima()
        # self.xiandaimima_widget.setupUi(self.form_xiandaimima)
        # # self.form_xiandaimima.setStyleSheet(qss_style)
        # self.form_xiandaimima.setWindowIcon(QtGui.QIcon('./logo.ico'))
        # self.form_xiandaimima.show()
        # self.xiandaimima_widget.AES_Encrypto.clicked.connect(self.AES_Encrypto)
        # self.xiandaimima_widget.AES_Decrypto.clicked.connect(self.AES_Decrypto)
        # self.xiandaimima_widget.AES_Mode.activated[str].connect(self.change_aes_setting)

        # print(values)
        # self.WChild_xiandaimima.vuln_name.setText(values[0]['vuln_name'])
        # self.WChild_xiandaimima.cms_name.setText(values[0]['cms_name'])

    # https://baijiahao.baidu.com/s?id=1706700589435327561&wfr=spider&for =pc

    def add_Tab(self):
        self.Ui.tab = QWidget()
        self.Ui.tab.setObjectName(u"tab")
        self.Ui.gridLayout = QGridLayout(self.Ui.tab)
        self.Ui.gridLayout.setObjectName(u"gridLayout")
        self.Ui.verticalLayout = QVBoxLayout()
        self.Ui.verticalLayout.setObjectName(u"verticalLayout")
        self.Ui.source_text = QLabel(self.Ui.tab)
        self.Ui.source_text.setObjectName(u"source_text")
        # self.source_text.setMinimumSize(QSize(0, 30))
        self.Ui.source_text.setStyleSheet(u"")

        self.Ui.verticalLayout.addWidget(self.Ui.source_text)
        self.Ui.Source_text = QPlainTextEdit(self.Ui.tab)
        self.Ui.Source_text.setObjectName(u"Source_text")
        self.Ui.Source_text.setPlaceholderText('请在此处输入')

        self.Ui.verticalLayout.addWidget(self.Ui.Source_text)

        self.Ui.result_text = QLabel(self.Ui.tab)
        self.Ui.result_text.setObjectName(u"result_text")
        # self.result_text.setMinimumSize(QSize(0, 30))
        self.Ui.result_text.setStyleSheet(u"")

        self.Ui.verticalLayout.addWidget(self.Ui.result_text)

        self.Ui.Result_text = QPlainTextEdit(self.Ui.tab)
        self.Ui.Result_text.setObjectName(u"Result_text")
        self.Ui.Result_text.setPlaceholderText('结果会显示在此处')

        self.Ui.verticalLayout.addWidget(self.Ui.Result_text)
        self.Ui.source_text.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.Ui.result_text.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.Ui.gridLayout.addLayout(self.Ui.verticalLayout, 0, 0, 1, 1)
        lisra = ["梦媛", "涵钰", "妲可", "含钰", "连倩", "辰泽", "涵博", "海萍", "祖儿", "佳琪", "诗晗", "之言", "清妍", "淑媛", "智妍", "晴然", "树静",
                 "娜娜", "瑞楠", "晓满", "婉雅", "雨婷", "筱满", "雅文", "玉琪", "敖雯", "文殊", "喻喧", "海英", "舒欣", "云亿", "莨静", "雅芝", "蕴兵",
                 "乐乐", "之恋", "小满", "悦心", "可人", "忆初", "衬心", "诠释", "尘封", "奔赴", "心鸢", "晴栀", "堇年", "青柠", "埋葬", "夏墨", "随风",
                 "屿暖", "深邃", "途往", "迷离", "槿城", "零落", "余笙", "梦呓", "墨凉", "晨曦", "纪年", "未央", "失语", "柠栀", "梦巷", "九离", "暮雨",
                 "木兮", "浅歌", "沐北", "惜颜", "素笺", "锁心", "柠萌", "卿歌", "归期", "予别", "情笙", "缥缈", "轩辕", "浮光", "缠绵", "碧影", "星愿",
                 "星月", "星雨", "沧澜", "醉月", "春媱", "夏露", "秋颜", "冬耀", "缱绻", "涟漪", "若溪", "微凉", "暖阳", "半夏", "崖悔", "洛尘", "矜柔",
                 "绚烂", "矫情", "真淳", "明媚", "迷离", "隐忍", "灼热", "幻灭", "落拓", "锦瑟", "妖娆", "邪殇", "离殇", "恋夏", "梦琪", "忆柳", "之桃",
                 "慕青", "问兰", "尔岚", "元香", "初夏", "沛菡", "傲珊", "曼文", "乐菱", "痴珊", "恨玉", "惜文", "香寒", "新柔", "语蓉", "海安", "夜蓉",
                 "涵柏", "水桃", "醉蓝", "春儿", "语琴", "从彤", "傲晴", "语兰", "又菱", "碧彤", "元霜", "怜梦", "紫寒", "妙彤", "曼易", "南莲", "紫翠",
                 "雨寒", "易烟", "如萱", "若南", "寻真", "晓亦", "向珊", "慕灵", "以蕊", "寻雁", "映易", "雪柳", "孤岚", "笑霜", "海云", "凝天", "沛珊",
                 "寒云", "冰旋", "宛儿", "绿真", "盼儿", "晓霜", "碧凡", "夏菡", "若烟", "半梦", "雅绿", "冰蓝", "灵槐", "平安", "书翠", "翠风", "香巧",
                 "代云", "梦曼", "幼翠", "友巧", "听寒", "梦柏", "醉易", "访旋", "亦玉", "凌萱", "访卉", "怀亦", "笑蓝", "春翠", "靖柏", "夜蕾", "冰夏",
                 "梦松", "书雪", "乐枫", "念薇", "靖雁", "寻春", "恨山", "从寒", "忆香", "觅波", "静曼", "凡旋", "以亦", "念露", "芷蕾", "千兰", "新波",
                 "代真", "新蕾", "雁玉", "冷卉", "紫山", "千琴", "恨天", "傲芙", "盼山", "怀蝶", "冰兰", "山柏", "翠萱", "恨松", "问旋", "从南", "白易",
                 "问筠", "如霜", "半芹", "丹珍", "冰彤", "亦寒", "寒雁", "怜云", "寻文", "乐丹", "翠柔", "谷山", "之瑶", "冰露", "尔珍", "谷雪", "乐萱",
                 "涵菡", "海莲", "傲蕾", "青槐", "冬儿", "易梦", "惜雪", "宛海", "之柔", "夏青", "亦瑶", "妙菡", "春竹", "痴梦", "紫蓝", "晓巧", "幻柏",
                 "元风", "冰枫", "访蕊", "南春", "芷蕊", "凡蕾", "凡柔", "安蕾", "天荷", "含玉", "书兰", "雅琴", "书瑶", "春雁", "从安", "夏槐", "念芹",
                 "怀萍", "代曼", "幻珊", "谷丝", "秋翠", "白晴", "海露", "代荷", "含玉", "书蕾", "听白", "访琴", "灵雁", "秋春", "雪青", "乐瑶", "含烟",
                 "涵双", "平蝶", "雅蕊", "傲之", "灵薇", "绿春", "含蕾", "从梦", "从蓉", "初丹", "听兰", "听蓉", "语芙", "夏彤", "凌瑶", "忆翠", "幻灵",
                 "怜菡", "紫南", "依珊", "妙竹", "访烟", "怜蕾", "映寒", "友绿", "冰萍", "惜霜", "凌香", "芷蕾", "雁卉", "迎梦", "元柏", "代萱", "紫真",
                 "千青", "凌寒", "紫安", "寒安", "怀蕊", "秋荷", "涵雁", "以山", "凡梅", "盼曼", "翠彤", "谷冬", "新巧", "冷安", "千萍", "冰烟", "雅阳",
                 "友绿", "南松", "诗云", "飞风", "寄灵", "书芹", "幼蓉", "以蓝", "笑寒", "忆寒", "秋烟", "芷巧", "水香", "映之", "醉波", "幻莲", "夜山",
                 "芷卉", "向彤", "小玉", "幼南", "凡梦", "尔曼", "念波", "迎松", "青寒", "笑天", "涵蕾", "YYDS", "栓Q", "辣鸡CTF,毁我青春"]
        self.Ui.tabWidget.addTab(self.Ui.tab, random.choice(lisra))
        self.Ui.tabWidget.setCurrentIndex(self.Ui.tabWidget.count() - 1)

    def closeTab(self, currentIndex):
        if self.Ui.tabWidget.count() == 1:
            QMessageBox.information(self, '嘤嘤嘤', '最后一个Tab了，无法关闭！')
        else:
            self.Ui.tabWidget.removeTab(currentIndex)

    def onCurrentChanged(self, ix):
        w = self.Ui.tabWidget.widget(ix)
        te = w.findChild(QPlainTextEdit, 'Source_text')
        re = w.findChild(QPlainTextEdit, 'Result_text')
        if te is not None:
            self.Ui.Source_text = te
            self.Ui.Result_text = re
            # print(te.toPlainText())

    def eventFilter(self, object, event):
        if object == self.Ui.tabWidget.tabBar():
            # if  event.type() in [QEvent.MouseButtonPress,  QEvent.MouseButtonRelease] :
            if event.type() in [QEvent.MouseButtonPress]:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == QtCore.Qt.RightButton:
                    self.add_Tab()
            elif event.type() == QtCore.QEvent.MouseButtonDblClick:
                # If image is double clicked, remove bar.
                self.add_Tab()
        return False

    def str_place(self):
        self.WChild_replace = Ui_KEY2()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild_replace.setupUi(self.dialog)
        self.dialog.setWindowTitle("替换")
        self.WChild_replace.key_1.setText("查找内容：")
        self.WChild_replace.key_2.setText("替换内容：")
        self.WChild_replace.enter.setText("替换输入文本")
        self.WChild_replace.quxiao.setText("替换输出文本")
        self.dialog.show()
        self.WChild_replace.enter.clicked.connect(lambda: self.str_replace("Source"))
        self.WChild_replace.quxiao.clicked.connect(lambda: self.str_replace("Result"))

    def str_replace(self, type):
        source_text = self.WChild_replace.Key1.text()
        result_text = self.WChild_replace.Key2.text()
        if type == 'Source':
            text = self.Ui.Source_text.toPlainText().strip()
            text = text.replace(source_text, result_text)
            self.Ui.Source_text.setPlainText(str(text))
        if type == 'Result':
            text = self.Ui.Result_text.toPlainText()
            text = text.replace(source_text, result_text)
            self.Ui.Result_text.setPlainText(str(text))
        self.dialog.close()

    def miwenfenxi(self):
        self.WChild_Ui_Cipher = Ui_Cipher()
        self.dialog_Ui_Cipher = QtWidgets.QDialog(self)
        self.WChild_Ui_Cipher.setupUi(self.dialog_Ui_Cipher)
        self.dialog_Ui_Cipher.setWindowTitle("密文识别")
        self.WChild_Ui_Cipher.pushButton_enter.setText("密文分析")
        self.WChild_Ui_Cipher.pushButton_close.setText("批量解密")
        self.dialog_Ui_Cipher.show()
        self.WChild_Ui_Cipher.pushButton_enter.clicked.connect(lambda:self.miwenfenxi_click(0))
        self.WChild_Ui_Cipher.pushButton_close.clicked.connect(lambda:self.miwenfenxi_click(1))

    def miwenfenxi_click(self,out_mima):
        cryptostr = self.WChild_Ui_Cipher.plainTextEdit_source.toPlainText()  # 获取密文
        if not  cryptostr:
            QMessageBox.critical(self, 'Error', "请输入一个密文！")
            return
        self.WChild_Ui_Cipher.plainTextEdit_source.clear()
        key1 = self.WChild_Ui_Cipher.lineEdit_key1.text()  # 获取密文
        key2 = self.WChild_Ui_Cipher.lineEdit_key2.text()  # 获取密文
        key3 = self.WChild_Ui_Cipher.lineEdit_key3.text()  # 获取密文
        self.thread = Cipher_Thread(cryptostr, key1,key2,key3)
        self.thread.signal.connect(self.Out_Cipherxxx)
        self.thread.start()  # 启动线程
        #解密完成输出结果
        self._decode_flag=0
        #是否输出密码
        self.out_mima = out_mima
    def Out_Cipherxxx(self,result):
        if result[0]:
            if result[1] == "end":
                if self._decode_flag:
                    txt = '操作完成!'
                else:
                    txt = '很遗憾，未能分析出密文类型！'
            else:
                self._decode_flag=1
                if self.out_mima:
                    txt = str(result[1])+"\n"+'-'*len(result[1].encode('gbk'))+"\n"+str(result[2])+'\n------------------------------------------------------------------'
                else:
                    txt = str(result[1])
            self.WChild_Ui_Cipher.plainTextEdit_source.appendPlainText(txt)

    def auto_get_flag(self):
        self.WChild_Ui_Getflag = Ui_Cipher()
        self.dialog_Ui_Getflag = QtWidgets.QDialog(self)
        self.WChild_Ui_Getflag.setupUi(self.dialog_Ui_Getflag)
        self.dialog_Ui_Getflag.setWindowTitle("自动获取FLAG")
        self.WChild_Ui_Getflag.pushButton_enter.setText("获取FLAG")
        self.WChild_Ui_Getflag.pushButton_close.setText("关闭窗口")
        self.WChild_Ui_Getflag.lineEdit_key3.setPlaceholderText("必填")
        self.WChild_Ui_Getflag.label_key3.setText("FLAG关键字:")
        self.dialog_Ui_Getflag.show()
        self.WChild_Ui_Getflag.pushButton_enter.clicked.connect(self.auto_get_flag_click)
        self.WChild_Ui_Getflag.pushButton_close.clicked.connect(lambda:self.dialog_Ui_Getflag.close())

    def auto_get_flag_click(self):
        self.WChild_Ui_Getflag.pushButton_enter.setEnabled(False)
        self.WChild_Ui_Getflag.pushButton_enter.setText("正在提取Flag...")
        cryptostr = self.WChild_Ui_Getflag.plainTextEdit_source.toPlainText()
        key1 = self.WChild_Ui_Getflag.lineEdit_key1.text()  # 获取密文
        key2 = self.WChild_Ui_Getflag.lineEdit_key2.text()  # 获取密文
        flag_guanjianzi = self.WChild_Ui_Getflag.lineEdit_key3.text()  # 获取密文
        if not cryptostr:
            QMessageBox.critical(self, 'Error', "密文不能为空！")
        if not flag_guanjianzi:
            QMessageBox.critical(self, 'Error', "关键字不能为空！")
            return
        self.thread = AutoGetFlag(cryptostr,key1,key2,flag_guanjianzi)
        self.thread.signal.connect(self.out_flag)
        self.thread.start()  # 启动线程

    def out_flag(self,result):
        self.Ui.Result_text.setPlainText(result[1])
        if result[0]:
            self.dialog_Ui_Getflag.close()
            QMessageBox.information(self, 'Success', '恭喜！成功获取flag！')
        else:
            QMessageBox.information(self, 'Success', "自动提取flag失败！")
            self.WChild_Ui_Getflag.pushButton_enter.setEnabled(True)
            self.WChild_Ui_Getflag.pushButton_enter.setText("获取FLAG")

        # print(result)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    window = MainWindows()
    translator = QTranslator()
    translator.load('./QSS/qm/qt_zh_CN.qm')  # 改变中文菜单
    app.installTranslator(translator)
    translator_2 = QTranslator()
    translator_2.load('./QSS/qm/widgets_zh_cn.qm')  # 改变QTextEdit右键为中文
    app.installTranslator(translator_2)
    window.show()
    try:
        response = requests.get("https://qianxiao996.cn/ctf-tools/version.txt", timeout=2)
        if (int(response.text.replace('.', '')) > int(version.replace('.', ''))):
            reply = QMessageBox.question(window, '软件更新', "检测到软件已发布新版本，是否前去下载?", QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                webbrowser.open('https://github.com/qianxiao996/CTF-Tools/releases')
            else:
                pass
    except:
        pass
    sys.exit(app.exec_())
