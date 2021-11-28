import binascii
import html, base64, sys, string, os, urllib.parse, random, collections, re, base36,base58, base91, py3base92,base62
import importlib.machinery
import webbrowser

import configparser

import Crypto.Util.Counter
import requests
from PyQt5.QtCore import QTranslator

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pyperclip
import json
from GUI.main import Ui_MainWindow
from GUI.KEY_1 import Ui_KEY1
from GUI.Binary import Ui_Binary
from GUI.KEY_2 import Ui_KEY2
from GUI.Xiandaimima import Ui_Form_Xiandaimima
import frozen_dir
from Crypto.Cipher import AES

SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)
version = '1.3.2'
update_time = '20211128'


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
        self.Ui.actionURL_UTF8_encode.triggered.connect(lambda: self.encode(self.Ui.actionURL_UTF8_encode.objectName()))
        self.Ui.actionURL_GB2312_encode.triggered.connect(
            lambda: self.encode(self.Ui.actionURL_GB2312_encode.objectName()))
        self.Ui.actionUnicode_encode.triggered.connect(lambda: self.encode(self.Ui.actionUnicode_encode.objectName()))
        self.Ui.actionEscape_U_encode.triggered.connect(lambda: self.encode(self.Ui.actionEscape_U_encode.objectName()))
        self.Ui.actionHtmlEncode_encode.triggered.connect(
            lambda: self.encode(self.Ui.actionHtmlEncode_encode.objectName()))
        self.Ui.actionASCII_encode.triggered.connect(lambda: self.encode(self.Ui.actionASCII_encode.objectName()))
        self.Ui.actionBase16_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase16_encode.objectName()))
        self.Ui.actionBase32_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase32_encode.objectName()))
        self.Ui.actionBase36_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase36_encode.objectName()))
        self.Ui.actionBase58_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase58_encode.objectName()))
        self.Ui.actionBase62_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase62_encode.objectName()))
        self.Ui.actionBase64_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase64_encode.objectName()))
        self.Ui.actionBase64_2_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase64_2_encode.objectName()))
        self.Ui.actionBase85_ASCII85_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase85_ASCII85_encode.objectName()))
        self.Ui.actionBase85_RFC1924_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase85_RFC1924_encode.objectName()))
        self.Ui.actionBase91_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase91_encode.objectName()))
        self.Ui.actionBase92_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase92_encode.objectName()))
        self.Ui.actionStr_Hex_encode.triggered.connect(lambda: self.encode(self.Ui.actionStr_Hex_encode.objectName()))
        self.Ui.actionShellcode_encode.triggered.connect(
            lambda: self.encode(self.Ui.actionShellcode_encode.objectName()))
        self.Ui.actionQwerty_encode.triggered.connect(lambda: self.encode(self.Ui.actionQwerty_encode.objectName()))
        self.Ui.actiontupian_base64_encode.triggered.connect(
            lambda: self.encode(self.Ui.actiontupian_base64_encode.objectName()))
        self.Ui.actiontupian_hex_encode.triggered.connect(
            lambda: self.encode(self.Ui.actiontupian_hex_encode.objectName()))
        # decode
        self.Ui.actionURL_UTF8_decode.triggered.connect(lambda: self.decode(self.Ui.actionURL_UTF8_decode.objectName()))
        self.Ui.actionURL_GB2312_decode.triggered.connect(
            lambda: self.decode(self.Ui.actionURL_GB2312_decode.objectName()))
        self.Ui.actionUnicode_decode.triggered.connect(lambda: self.decode(self.Ui.actionUnicode_decode.objectName()))
        self.Ui.actionEscape_U_decode.triggered.connect(lambda: self.decode(self.Ui.actionEscape_U_decode.objectName()))
        self.Ui.actionHtmlEncode_decode.triggered.connect(
            lambda: self.decode(self.Ui.actionHtmlEncode_decode.objectName()))
        self.Ui.actionASCII_decode.triggered.connect(lambda: self.decode(self.Ui.actionASCII_decode.objectName()))
        self.Ui.actionBase16_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase16_decode.objectName()))
        self.Ui.actionBase32_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase32_decode.objectName()))
        self.Ui.actionBase36_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase36_decode.objectName()))
        self.Ui.actionBase58_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase58_decode.objectName()))
        self.Ui.actionBase62_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase62_decode.objectName()))
        self.Ui.actionBase64_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase64_decode.objectName()))
        self.Ui.actionBase64_2_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase64_2_decode.objectName()))
        self.Ui.actionBase85_ASCII85_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase85_ASCII85_decode.objectName()))
        self.Ui.actionBase85_RFC1924_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase85_RFC1924_decode.objectName()))
        self.Ui.actionBase91_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase91_decode.objectName()))
        self.Ui.actionBase92_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase92_decode.objectName()))
        self.Ui.actionHex_Str_decode.triggered.connect(lambda: self.decode(self.Ui.actionHex_Str_decode.objectName()))
        self.Ui.actionShellcode_decode.triggered.connect(
            lambda: self.decode(self.Ui.actionShellcode_decode.objectName()))
        self.Ui.actionQwerty_decode.triggered.connect(lambda: self.decode(self.Ui.actionQwerty_decode.objectName()))
        self.Ui.actionbase64_tupian_decode.triggered.connect(
            lambda: self.decode(self.Ui.actionbase64_tupian_decode.objectName()))
        self.Ui.actionhex_tupian_decode.triggered.connect(
            lambda: self.decode(self.Ui.actionhex_tupian_decode.objectName()))
        # encrypt
        self.Ui.actionRot13_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.actionRot13_encrypt.objectName()))
        self.Ui.action_kaisa_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_kaisa_encrypt.objectName()))
        self.Ui.action_zhalan_encrypt.triggered.connect(
            lambda: self.encrypt(self.Ui.action_zhalan_encrypt.objectName()))
        self.Ui.action_zhalan_w_encrypt.triggered.connect(
            lambda: self.encrypt(self.Ui.action_zhalan_w_encrypt.objectName()))
        self.Ui.action_peigen_encrypt.triggered.connect(
            lambda: self.encrypt(self.Ui.action_peigen_encrypt.objectName()))
        self.Ui.action_mosi_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_mosi_encrypt.objectName()))
        self.Ui.action_yunying_encrypt.triggered.connect(
            lambda: self.encrypt(self.Ui.action_yunying_encrypt.objectName()))
        self.Ui.action_dangpu_encrypt.triggered.connect(
            lambda: self.encrypt(self.Ui.action_dangpu_encrypt.objectName()))
        self.Ui.action_sifang_encrypt.triggered.connect(
            lambda: self.encrypt(self.Ui.action_sifang_encrypt.objectName()))
        self.Ui.action_weinijiya_encrypt.triggered.connect(
            lambda: self.encrypt(self.Ui.action_weinijiya_encrypt.objectName()))
        self.Ui.action_Atbash_encrypt.triggered.connect(
            lambda: self.encrypt(self.Ui.action_Atbash_encrypt.objectName()))
        self.Ui.action_fangshe_encrypt.triggered.connect(
            lambda: self.encrypt(self.Ui.action_fangshe_encrypt.objectName()))


        self.Ui.action_xiandaimima.triggered.connect(self.open_xiandaimima)

        # decrypt
        self.Ui.actionRot13_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.actionRot13_decrypt.objectName()))
        self.Ui.action_kaisa_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_kaisa_decrypt.objectName()))
        self.Ui.action_zhalan_decrypt.triggered.connect(
            lambda: self.decrypt(self.Ui.action_zhalan_decrypt.objectName()))
        self.Ui.action_zhalan_w_decrypt.triggered.connect(
            lambda: self.decrypt(self.Ui.action_zhalan_w_decrypt.objectName()))
        self.Ui.action_peihen_decrypt.triggered.connect(
            lambda: self.decrypt(self.Ui.action_peihen_decrypt.objectName()))
        self.Ui.action_mosi_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_mosi_decrypt.objectName()))
        self.Ui.action_yiwei_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_yiwei_decrypt.objectName()))
        self.Ui.action_yunxing_decrypt.triggered.connect(
            lambda: self.decrypt(self.Ui.action_yunxing_decrypt.objectName()))
        self.Ui.action_dangpu_decry.triggered.connect(lambda: self.decrypt(self.Ui.action_dangpu_decry.objectName()))
        self.Ui.action_sifang_decrypt.triggered.connect(
            lambda: self.decrypt(self.Ui.action_sifang_decrypt.objectName()))
        self.Ui.action_weinijiya_decrypt.triggered.connect(
            lambda: self.decrypt(self.Ui.action_weinijiya_decrypt.objectName()))
        self.Ui.action_Atbash_decrypt.triggered.connect(
            lambda: self.decrypt(self.Ui.action_Atbash_decrypt.objectName()))
        self.Ui.action_fangshe_decrypt.triggered.connect(
            lambda: self.decrypt(self.Ui.action_fangshe_decrypt.objectName()))

        # 进制转换
        self.Ui.action2_8.triggered.connect(lambda: self.Binary(self.Ui.action2_8.objectName()))
        self.Ui.action2_10.triggered.connect(lambda: self.Binary(self.Ui.action2_10.objectName()))
        self.Ui.action2_16.triggered.connect(lambda: self.Binary(self.Ui.action2_16.objectName()))
        self.Ui.action8_2.triggered.connect(lambda: self.Binary(self.Ui.action8_2.objectName()))
        self.Ui.action8_10.triggered.connect(lambda: self.Binary(self.Ui.action8_10.objectName()))
        self.Ui.action8_16.triggered.connect(lambda: self.Binary(self.Ui.action8_16.objectName()))
        self.Ui.action10_2.triggered.connect(lambda: self.Binary(self.Ui.action10_2.objectName()))
        self.Ui.action10_8.triggered.connect(lambda: self.Binary(self.Ui.action10_8.objectName()))
        self.Ui.action10_16.triggered.connect(lambda: self.Binary(self.Ui.action10_16.objectName()))
        self.Ui.action16_2.triggered.connect(lambda: self.Binary(self.Ui.action16_2.objectName()))
        self.Ui.action16_8.triggered.connect(lambda: self.Binary(self.Ui.action16_8.objectName()))
        self.Ui.action16_10.triggered.connect(lambda: self.Binary(self.Ui.action16_10.objectName()))
        self.Ui.action_others.triggered.connect(lambda: self.Binary(self.Ui.action_others.objectName()))
        self.Ui.actionAbout.triggered.connect(self.about)
        self.Ui.actionAuthor.triggered.connect(self.author)
        self.Ui.actionUpdate_2.triggered.connect(self.Update)


        self.Ui.yijian_decode.clicked.connect(self.yijian_decode)  #一键解码
        self.Ui.yijian_base.clicked.connect(self.yijian_base)  #一键base
        self.Ui.yijian_decrypto.clicked.connect(self.yijian_decrypto)  # 一键解密
        self.Ui.yijian_jinzhi.clicked.connect(self.yijian_jinzhi)  # 一键进制

        self.Ui.action_str_replace.triggered.connect(self.str_place)  # 字符串替换
        self.Ui.action_str_split.triggered.connect(self.str_split)  # 字符串分割
        self.Ui.action_str_chaifen.triggered.connect(self.str_chaifen)  # 字符串拆分
        self.Ui.action_str_tongji.triggered.connect(self.str_tongji)  # 字符串统计
        self.Ui.action_str_re.triggered.connect(self.str_re)  # 字符串拆分
        self.Ui.action_str_xiaoxie.triggered.connect(lambda:self.Ui.Result_text.setPlainText(self.Ui.Source_text.toPlainText().lower()))  # 字符串全小写
        self.Ui.action_str_daxie.triggered.connect(lambda:self.Ui.Result_text.setPlainText(self.Ui.Source_text.toPlainText().upper()))  # 字符串全小写



        self.readfile()
        # Website
        websitemenubar = self.menuBar()  # 获取窗体的菜单栏
        Website = websitemenubar.addMenu("在线工具")
        for i in json_data:
            impMenu = QMenu(i, self)
            url_list = json_data[i].split('\n')
            for j in url_list:
                sub_action = QAction(QIcon(''), j, self)
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
        for z in config_setup.options('QSS_List'):
            sub_action = QAction(QIcon(''), z, self)
            impMenu.addAction(sub_action)
        others.addMenu(impMenu)
        others.triggered[QAction].connect(self.show_others)

    def yijian_decode(self):
        text = self.Ui.Source_text.toPlainText().strip()
        if text == '':
            self.Ui.Result_text.setPlainText('请输入一个源字符串！')
            return 0
        else:
            self.Ui.Result_text.clear()
            self.out_result("URL UTF8:\n"+self.actionURL_UTF8_decode(text))
            self.out_result("URL GB2312:\n" + self.actionURL_GB2312_decode(text))
            self.out_result("Unicode:\n" + self.actionUnicode_decode(text))
            self.out_result("Escape(%U):\n" + self.actionEscape_U_decode(text))
            self.out_result("HtmlEncode:\n" + self.actionHtmlEncode_decode(text))
            self.out_result("ASCII:\n" + self.actionASCII_decode(text))
            self.out_result("Shellcode:\n" + self.actionShellcode_decode(text))
            self.out_result("Qwerty:\n" + self.actionQwerty_decode(text))
            self.out_result("Hex->Str:\n" + self.actionHex_Str_decode(text))
    def yijian_base(self):
        text = self.Ui.Source_text.toPlainText().strip()
        if text == '':
            self.Ui.Result_text.setPlainText('请输入一个源字符串！')
            return 0
        else:
            self.Ui.Result_text.clear()
            self.out_result("Base16:\n"+self.actionBase16_decode(text))
            self.out_result("Base32:\n" + self.actionBase32_decode(text))
            self.out_result("Base36:\n" + self.actionBase36_decode(text))
            self.out_result("Base58:\n" + self.actionBase58_decode(text))
            self.out_result("Base62:\n" + str(self.actionBase62_decode(text)))
            self.out_result("Base64:\n" + self.actionBase64_decode(text))
            self.out_result("Base85(ASCII85):\n" + self.actionBase85_ASCII85_decode(text))
            self.out_result("Base85(RFC1924):\n" + self.actionBase85_RFC1924_decode(text))
            self.out_result("Base91:\n" + self.actionBase91_decode(text))
            self.out_result("Base92:\n" + self.actionBase92_decode(text))
    def yijian_decrypto(self):
        text = self.Ui.Source_text.toPlainText().strip()
        if text == '':
            self.Ui.Result_text.setPlainText('请输入一个源字符串！')
            return 0
        else:
            self.Ui.Result_text.clear()
            self.out_result("Rot13:\n"+self.actionRot13_decrypt(text))
            self.out_result("凯撒密码:\n" + self.action_kaisa_decrypt(text))
            self.out_result("栅栏密码:\n" + self.action_zhalan_decrypt(text))
            self.out_result("栅栏密码(W型):\n" + self.action_zhalan_w_decrypt(text))
            self.out_result("培根密码:\n" + str(self.action_peihen_decrypt(text)))
            self.out_result("摩斯密码:\n" + self.action_mosi_decrypt(text))
            self.out_result("移位密码:\n" + self.action_yiwei_decrypt(text))
            self.out_result("云影密码:\n" + self.action_yunxing_decrypt(text))
            self.out_result("当铺密码:\n" + self.action_dangpu_decry(text))
            self.out_result("埃特巴什码:\n" + self.action_Atbash_decrypt(text))

    def yijian_jinzhi(self):
        text = self.Ui.Source_text.toPlainText().strip()
        if text == '':
            self.Ui.Result_text.setPlainText('请输入一个源字符串！')
            return 0
        else:
            self.Ui.Result_text.clear()
            self.out_result("2->8:\n"+self.action2_8(text))
            self.out_result("2->10:\n" + self.action2_10(text))
            self.out_result("2->16:\n" + self.action2_16(text))
            self.out_result("8->2:\n" + self.action8_2(text))
            self.out_result("8->10:\n" + str(self.action8_10(text)))
            self.out_result("8->16:\n" + self.action8_16(text))
            self.out_result("10->2:\n" + self.action10_2(text))
            self.out_result("10->8:\n" + self.action10_8(text))
            self.out_result("10->16:\n" + self.action10_16(text))
            self.out_result("16->2:\n" + self.action16_2(text))
            self.out_result("16->8:\n" + self.action16_8(text))
            self.out_result("16->10:\n" + self.action16_10(text))


    def out_result(self,text):
        self.Ui.Result_text.appendPlainText(text+'\n')

    def load_config(self):
        try:
            global config_setup
            global qss_style
            # 实例化configParser对象
            config_setup = configparser.ConfigParser()
            # -read读取ini文件
            config_setup.read('config.ini', encoding='utf-8')
            if 'QSS_Setup' not in config_setup:  # 如果分组type不存在则插入type分组
                config_setup.add_section('QSS_Setup')
                config_setup.set("QSS_Setup", "QSS", 'default.qss')
                config_setup.write(open('config.ini', "r+", encoding="utf-8"))  # r+模式
                qss_Setup = 'default.qss'
            else:
                qss_Setup = config_setup.get('QSS_Setup', 'QSS')
            with open("QSS/" + qss_Setup, 'r', encoding='utf-8') as f:
                qss_style = f.read()
                f.close()

            MainWindows.setStyleSheet(self, qss_style)
            f.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))
            pass

    def show_others(self, q):
        if q.text() == "关于":
            self.about()
            return
        if q.text() == "作者":
            self.author()
            return
        if q.text() == "更新":
            self.Update()
            return
        else:
            try:
                filename = config_setup.get('QSS_List', q.text())
                with open("QSS/" + filename, 'r', encoding='utf-8') as f:
                    qss_style = f.read()
                    f.close()
                MainWindows.setStyleSheet(self, qss_style)
                config_setup.set("QSS_Setup", "QSS", filename)
                f.close()
                # python = sys.executable
                # os.execl(python, python, *sys.argv)
            except Exception as e:
                QMessageBox.critical(self, 'Error', str(e))
                pass

    def show_plugins(self, q):
        try:
            plugins_methods = "Plugins/" + plugins_data[q.text()][:-3]
            filename = "Plugins/" + plugins_data[q.text()]
            text = self.Ui.Source_text.toPlainText()
            if text == '':
                self.Ui.Result_text.setPlainText('请输入一个源字符串！')
                return 0
            nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(plugins_methods, filename).load_module()
            result = nnnnnnnnnnnn1.run(text)
            self.Ui.Result_text.setPlainText(str(result))
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))
            pass

    def show_json(self, q):
        # print(q.text())
        pyperclip.copy(q.text())
        reply = QMessageBox.question(self, 'Message', "链接已复制到剪切板，是否在浏览器中打开链接?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            webbrowser.open(q.text())
        else:
            pass

    def readfile(self):
        try:
            global json_data
            f = open('Plugins//data.json', 'r', encoding='utf-8')
            json_data = json.load(f)
            # print(json_data)
            f.close()
            qss_Setup = config_setup.get('QSS_Setup', 'QSS')

            with open("QSS/" + qss_Setup, 'r', encoding='utf-8') as f:
                qss_style = f.read()
                f.close()
            MainWindows.setStyleSheet(self, qss_style)
            # print(json_data)
            f.close()
            global plugins_data
            f = open('Plugins/Plugins.json', 'r', encoding='utf-8')
            plugins_data = json.load(f)
            # print(plugins_data)
            f.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))
            pass

    # 图片转base64
    def actiontupian_base64_encode(self, text):
        try:
            filename = self.file_open(r"Text Files (*.jpg);;All files(*.*)")
            with open(filename, 'rb') as f:
                base64_data = base64.b64encode(f.read())
                s = base64_data.decode()
            self.Ui.Result_text.setPlainText(str('data:image/%s;base64,%s' % (filename[-3:], s)))
            return 'exit'
        except:
            return('转换失败！')


    # 图片转hex
    def actiontupian_hex_encode(self, text):
        try:
            filename = self.file_open(r"Text Files (*.jpg);;All files(*.*)")
            with open(filename, 'rb') as f:
                hex_data = f.read()
                hexstr = binascii.hexlify(hex_data).decode("utf-8")
                hexstr = hexstr.upper()
            self.Ui.Result_text.setPlainText(str('%s' % (hexstr)))
            return 'exit'
        except:
            return('转换失败！')

        # 编码

    def encode(self, encode_type):
        try:
            text = self.Ui.Source_text.toPlainText()
            if encode_type in ["actiontupian_hex_encode", "actiontupian_base64_encode"]:
                getattr(self, encode_type)(text)
            else:
                if text == '':
                    self.Ui.Result_text.setPlainText('请输入一个源字符串！')
                    return 0
                else:
                    result_text = getattr(self, encode_type)(text)
                    if result_text == "exit":
                        pass
                    elif result_text != "":
                        self.Ui.Result_text.setPlainText(str(result_text))
                    else:
                        self.Ui.Result_text.setPlainText("编码失败！")
        except Exception as e:
            self.Ui.Result_text.setPlainText(str(e))
            pass

    def actionURL_UTF8_encode(self, text):
        text = text.encode('utf-8')
        result_text = urllib.parse.quote(text)
        return result_text

    def actionURL_GB2312_encode(self, text):
        text = text.encode('gb2312')
        result_text = urllib.parse.quote(text)
        return result_text

    def actionUnicode_encode(self, text):
        text = text.encode('unicode_escape')
        result_text = str(text, encoding='utf-8')
        return result_text

    def actionEscape_U_encode(self, text):
        text = text.encode('unicode_escape')
        result_text = str(text, encoding='utf-8').replace('\\u', '%u')
        return result_text

    def actionHtmlEncode_encode(self, text):
        result_text = html.escape(text)
        return result_text

    def actionASCII_encode(self, text):
        result = ''
        for i in text:
            result = str(result) + str(ord(str(i))) + ' '
        result_text = str(result)[:-1]
        return result_text

    def actionBase16_encode(self, text):
        text = text.lower()
        text = base64.b16encode(text.encode("utf-8"))
        result_text = str(text, encoding='utf-8')
        return result_text

    def actionBase32_encode(self, text):
        text = base64.b32encode(text.encode("utf-8"))
        result_text = str(text, encoding='utf-8')
        return result_text

    def actionBase36_encode(self, text):
        result_text = str(base36.loads(text))
        return result_text

    def actionBase58_encode(self, text):
        result_text = base58.b58encode(text.encode('utf-8')).decode()  # 加密
        return result_text
    def actionBase62_encode(self,text):
        try:
            text = base62.encode(int(text))
        except:
            text='base62只能对数字编码！'
        # print(text)
        # result_text = str(text, encoding='utf-8')
        return text
    def actionBase64_encode(self, text):
        text = base64.b64encode(text.encode("utf-8"))
        result_text = str(text, encoding='utf-8')
        return result_text

    def actionBase64_2_encode(self, text):
        self.WChild_base64 = Ui_KEY1()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild_base64.setupUi(self.dialog)
        self.dialog.setWindowTitle("base64自定义")
        self.WChild_base64.label.setText("请输入编码表:")
        self.dialog.show()
        self.WChild_base64.keyenter.clicked.connect(self.base64_zidingyi)
        return 'exit'
    def base64_zidingyi(self):
        self.dialog.close()
        try:
            plain = self.Ui.Source_text.toPlainText().strip()
            n = self.WChild_base64.key.text().strip()
            STANDARD_ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
            CUSTOM_ALPHABET = n.encode()
            ENCODE_TRANS = bytes.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
            result_text  = base64.b64encode(plain.encode()).translate(ENCODE_TRANS).decode()
            self.Ui.Result_text.setPlainText(result_text)
        except Exception as e :
            self.Ui.Result_text.setPlainText(str(e))


    def actionBase85_ASCII85_encode(self, text):
        result_text = base64.a85encode(text.encode('utf-8')).decode()#加密
        return result_text
    def actionBase85_RFC1924_encode(self, text):
        result_text = base64.b85encode(text.encode('utf-8')).decode()  # 加密
        return result_text


    def actionBase91_encode(self, text):
        result_text = base91.encode(text.encode('utf-8'))  #
        return result_text
    def actionBase92_encode(self, text):
        result_text = py3base92.encode(text)
        return result_text



    def actionStr_Hex_encode(self, text):
        result = ''
        for i in text:
            single = str(hex(ord(str(i))))
            result = result + single
        result_text = (str(result)).replace('0x', '')
        return result_text

    def actionShellcode_encode(self, text):
        result = ''
        for i in text:
            single = str(hex(ord(str(i))))
            result = result + single
        result_text = (str(result)).replace('0x', '\\x')
        return result_text

    def actionQwerty_encode(self, text):
        str1 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        str2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result_text = ""
        for s in text:
            if s in str1:
                if s != ' ':
                    result_text = result_text + str1[str2.index(s)]
                else:
                    result_text = result_text + ' '
            else:
                result_text = 'Qwerty只能对字母加密!'
        return result_text
        # print(str(e))

    # 解码
    def decode(self, decode_type):
        try:
            result_text = ''
            # print(decode_type)
            text = self.Ui.Source_text.toPlainText().strip()

            if text == '':
                self.Ui.Result_text.setPlainText('请输入一个源字符串！')
                return 0
            else:
                result_text = getattr(self, decode_type)(text)
                if result_text != "":
                    self.Ui.Result_text.setPlainText(str(result_text))
                else:
                    self.Ui.Result_text.setPlainText('解码失败!')
        except Exception as e:
            self.Ui.Result_text.setPlainText(str(e))
            # print(e)
            pass

    def actionURL_UTF8_decode(self, text):
        try:
            result_text = str(urllib.parse.unquote(text))
        except Exception as  e:
            result_text='解码失败'
        return result_text

    def actionURL_GB2312_decode(self, text):
        try:
            result_text = str(urllib.parse.unquote(text, 'gb2312'))
        except Exception as  e:
            result_text='解码失败'
        return result_text

    def actionUnicode_decode(self, text):
        try:
            result_text = bytes(text, encoding="utf8").decode('unicode_escape')
        except Exception as  e:
            result_text='解码失败'

        return result_text

    def actionEscape_U_decode(self, text):
        try:
            text = text.replace('%u', '\\u').replace('%U', '\\u')
            result_text = bytes(text, encoding="utf8").decode('unicode_escape')
        except Exception as  e:
            result_text='解码失败'

        return result_text

    def actionHtmlEncode_decode(self, text):
        try:
            result_text = html.unescape(text)
        except Exception as  e:
            result_text='解码失败'
        return result_text

    def actionASCII_decode(self, text):
        try:
            if ':' in text:
                text = text.split(":")
            elif ' ' in text:
                text = text.split(" ")
            elif ';' in text:
                text = text.split(";")
            elif ',' in text:
                text = text.split(",")
            else:
                list22 = []
                list22.append(text)
                text = list22
            # print(text)
            result = ''
            for i in text:
                if i != '':
                    # print(i)
                    # print(chr(int(i)))
                    result = result + chr(int(i))
            result_text = result
        except Exception as  e:
            result_text='解码失败'
        return result_text

    def actionBase16_decode(self, text):
        try:
            text = text.upper()
            text = base64.b16decode(text.encode("utf-8"))
            result_text = str(text, encoding='utf-8')
        except Exception as  e:
            result_text='解码失败'
        return result_text

    def actionBase32_decode(self, text):
        try:
            text = base64.b32decode(text.encode("utf-8"))
            result_text = str(text, encoding='utf-8')
        except Exception as  e:
            result_text='解码失败'
        return result_text

    def actionBase36_decode(self, text):
        try:
            text = base36.dumps(int(text))  # 解密
            result_text = str(text)
        except Exception as  e:
            result_text='解码失败'
        return result_text
    def actionBase58_decode(self, text):
        try:
            result_text= base58.b58decode(text).decode()  # 解密
        except Exception as  e:
            result_text='解码失败'
        return result_text
    def actionBase62_decode(self, text):
        try:
            result_text = base62.decode(text)
        except:
            result_text = '解码失败'
        return result_text
    def actionBase64_decode(self, text):
        try:
            text = base64.b64decode(text.encode("utf-8"))
            result_text = str(text, encoding='utf-8')
        except Exception as  e:
            result_text='解码失败'
        return result_text


    def actionBase64_2_decode(self, text):
        self.WChild_base64 = Ui_KEY1()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild_base64.setupUi(self.dialog)
        self.dialog.setWindowTitle("base64自定义")
        self.WChild_base64.label.setText("请输入编码表:")
        self.dialog.show()
        self.WChild_base64.keyenter.clicked.connect(self.base64_zidingyi_decode)
        return 'exit'
    def base64_zidingyi_decode(self):
        self.dialog.close()
        try:
            plain = self.Ui.Source_text.toPlainText().strip()
            n = self.WChild_base64.key.text().strip()
            STANDARD_ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
            CUSTOM_ALPHABET = n.encode()
            DECODE_TRANS = bytes.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)
            result_text = base64.b64decode((plain.encode()).translate(DECODE_TRANS)).decode()
            self.Ui.Result_text.setPlainText(result_text)
        except Exception as e :
            self.Ui.Result_text.setPlainText(str(e))


    def actionBase85_ASCII85_decode(self, text):
        try:
            result_text = base64.a85decode(text).decode()  # 解密
        except Exception as  e:
            result_text='解码失败'
        return result_text

    def actionBase85_RFC1924_decode(self, text):
        try:
            result_text= base64.b85decode(text).decode()  # 解密
        except Exception as  e:
            result_text='解码失败'
        return result_text


    def actionBase91_decode(self, text):
        try:
            result_text =  base91.decode(text).decode()
        except Exception as  e:
            result_text='解码失败'
        return result_text
    def actionBase92_decode(self, text):
        try:
            result_text= py3base92.decode(text)  # 解密
        except Exception as  e:
            result_text='解码失败'
        return result_text


    def actionHex_Str_decode(self, text):
        try:
            text = text.replace('0x', '').replace('0X', '')
            result_text = str(bytes.fromhex(text), encoding="utf-8")
        except Exception as e:
            result_text='解码失败'
        return result_text

    def actionShellcode_decode(self, text):
        try:
            text = text.lower()
            result = ''
            if "0x" in text and "\\x" not in text:
                text = text.split('0x')
            elif "\\x" in text and "0x" not in text:
                text = text.split('\\x')
            else:
                result_text = "请输入正确的格式，如：\n\\x61\\x00\\x62\\x00\\x63\n0x610x000x620x000x63"
                return result_text
            for i in text:
                single = str(bytes.fromhex(i.rjust(2, '0')), encoding="utf-8")
                result = result + single
            result_text = str(result)
        except Exception as e:
            result_text='解码失败'
        return result_text

    def actionQwerty_decode(self, text):
        try:
            letter = {
                'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e', 'y': 'f', 'u': 'g',
                'i': 'h', 'o': 'i', 'p': 'j', 'a': 'k', 's': 'l', 'd': 'm', 'f': 'n',
                'g': 'o', 'h': 'p', 'j': 'q', 'k': 'r', 'l': 's', 'z': 't',
                'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x', 'n': 'y', 'm': 'z',
                'Q': 'A', 'W': 'B', 'E': 'C', 'R': 'D', 'T': 'E', 'Y': 'F', 'U': 'G',
                'I': 'H', 'O': 'I', 'P': 'J', 'A': 'K', 'S': 'L', 'D': 'M', 'F': 'N',
                'G': 'O', 'H': 'P', 'J': 'Q', 'K': 'R', 'L': 'S', 'Z': 'T',
                'X': 'U', 'C': 'V', 'V': 'W', 'B': 'X', 'N': 'Y', 'M': 'Z',
            }
            result_text = ''
            for i in range(0, len(text)):
                if text[i] != ' ':
                    result_text = result_text + letter.get(text[i])
                else:
                    result_text = result_text + ' '
        except Exception as  e:
            result_text='解码失败'
        return result_text

    def actionbase64_tupian_decode(self, text):
        try:
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

    def actionhex_tupian_decode(self, text):
        try:
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

    # encrypt
    def encrypt(self, encrypt_type):
        try:
            result_text = ''
            # print(encrypt_type)
            text = self.Ui.Source_text.toPlainText().strip()
            if text == '':
                self.Ui.Result_text.setPlainText('请输入一个源字符串！')
                return
            else:
                result_text = getattr(self, encrypt_type)(text)
                if result_text == "exit":
                    return
                elif result_text != "":
                    self.Ui.Result_text.setPlainText(result_text)
                else:
                    self.Ui.Result_text.setPlainText('加密失败!')
        except:
            self.Ui.Result_text.setPlainText('加密失败!')
    def actionRot13_encrypt(self,text):
        d = {chr(i + c): chr((i + 13) % 26 + c) for i in range(26) for c in (65, 97)}
        result_text = ''.join([d.get(c, c) for c in text])
        return result_text
    def action_kaisa_encrypt(self,text):

        t = ""
        for c in text:
            if 'a' <= c <= 'z':  # str是可以直接比较的
                t += chr(ord('a') + ((ord(c) - ord('a')) + 3) % 26)
            elif 'A' <= c <= 'Z':
                t += chr(ord('A') + ((ord(c) - ord('A')) + 3) % 26)
            else:
                t += c
        result_text = t
        return result_text

    def action_zhalan_encrypt(self, text):
        self.WChild_zhalan = Ui_KEY1()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild_zhalan.setupUi(self.dialog)
        self.dialog.setWindowTitle("栅栏密码")
        self.WChild_zhalan.label.setText("请输入栏数：")
        self.dialog.show()
        self.WChild_zhalan.keyenter.clicked.connect(self.zhalanEncrypto)
        return "exit"
    def action_zhalan_w_encrypt(self, text):

        self.WChild_zhalan = Ui_KEY1()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild_zhalan.setupUi(self.dialog)
        self.dialog.setWindowTitle("栅栏密码(W型)")
        self.WChild_zhalan.label.setText("请输入栏数：")
        self.dialog.show()
        self.WChild_zhalan.keyenter.clicked.connect(self.zhalan_w_Encrypto)
        return "exit"

    def action_peigen_encrypt(self, text):
        CODE_TABLE = {  # 培根字典
            'aaaaa': 'a', 'aaaab': 'b', 'aaaba': 'c', 'aaabb': 'd', 'aabaa': 'e', 'aabab': 'f', 'aabba': 'g',
            'aabbb': 'h', 'abaaa': 'i', 'abaab': 'j', 'ababa': 'k', 'ababb': 'l', 'abbaa': 'm', 'abbab': 'n',
            'abbba': 'o', 'abbbb': 'p', 'baaaa': 'q', 'baaab': 'r', 'baaba': 's', 'baabb': 't', 'babaa': 'u',
            'babab': 'v', 'babba': 'w', 'babbb': 'x', 'bbaaa': 'y', 'bbaab': 'z'
        }
        str = text.lower()
        listStr = ''
        for i in str:
            if i in CODE_TABLE.values():
                # 将键、值各化为一个列表，取出i在value的位置后根据下标找到对应的键
                listStr += list(CODE_TABLE.keys())[list(CODE_TABLE.values()).index(i)]
        result_text = listStr.upper()  # 大写输出
        return result_text

    def action_mosi_encrypt(self, text):

        CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
                'D': '-..', 'E': '.', 'F': '..-.',
                'G': '--.', 'H': '....', 'I': '..',
                'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---',
                'P': '.--.', 'Q': '--.-', 'R': '.-.',
                'S': '...', 'T': '-', 'U': '..-',
                'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..',
                '0': '-----', '1': '.----', '2': '..---',
                '3': '...--', '4': '....-', '5': '.....',
                '6': '-....', '7': '--...', '8': '---..',
                '9': '----.', '?': '..--..', '/': '-..-.',
                '()': '-.--.-', '-': '-....-', '.': '.-.-.-'
                }
        msg = ''
        for char in text.upper():
            if char in CODE:
                if char == ' ':
                    pass
                else:
                    msg += (CODE[char.upper()] + ' ')
            else:
                msg = '文本中含有不能识别的字符！'
        result_text = msg

        return result_text


    def action_yunying_encrypt(self, text):
        charList = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        cipher = [i for i in text.upper()]
        tmp = []
        ret = []
        for i in range(len(cipher)):
            for j in range(len(charList)):
                if charList[j] == cipher[i]:
                    tmp.append(j + 1)
        for i in tmp:
            res = ''
            if i >= 8:
                for j in range(0, int(i / 8)):
                    res += '8'
            if i % 8 >= 4:
                for j in range(0, int(i % 8 / 4)):
                    res += '4'
            if i % 4 >= 2:
                for j in range(0, int(i % 4 / 2)):
                    res += '2'
            if i % 2 >= 1:
                for j in range(0, int(i % 2 / 1)):
                    res += '1'
            ret.append(res + '0')
        result_text = ''.join(ret)[:-1]
        return result_text

    def action_sifang_encrypt(self, text):
        self.WChild = Ui_KEY2()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild.setupUi(self.dialog)
        self.dialog.setWindowTitle("四方密码")
        self.WChild.key_1.setText("Key square 1：")
        self.WChild.keyl_2.setText("Key square 2：")
        self.dialog.show()
        self.WChild.enter.clicked.connect(self.sifang_encrypt)
        return 'exit'

    def action_dangpu_encrypt(self, text):
        mapping_data = [['田'], ['由'], ['中'], ['人'], ['工'], ['大'], ['王'], ['夫'], ['井'], ['羊']]
        try:
            result = []
            for c in text:
                c_list = mapping_data[int(c)]
                c_index = random.randint(0, len(c_list) - 1)
                result.append(c_list[c_index])
            result_text = ''.join(result)
        except:
            result_text = '未找到该字符串对应的中文！'
        return result_text


    def action_fangshe_encrypt(self, text):
        self.WChild = Ui_KEY2()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild.setupUi(self.dialog)
        self.dialog.setWindowTitle("仿射密码")
        self.WChild.key_1.setText("a：")
        self.WChild.keyl_2.setText("b：")
        self.dialog.show()
        self.WChild.enter.clicked.connect(self.fangshe_encrypt)
        return 'exit'

    def action_weinijiya_encrypt(self, text):
        self.WChild = Ui_KEY1()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild.setupUi(self.dialog)
        self.dialog.setWindowTitle("维吉尼亚密码")
        self.WChild.label.setText("Keyword：")
        self.dialog.show()
        self.WChild.keyenter.clicked.connect(self.VigenereEncrypto)
        return 'exit'

    def action_Atbash_encrypt(self, text):
        str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        str2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
        result_text = ""
        for s in text:
            if s in str1:
                if s != ' ':
                    result_text = result_text + str2[str1.index(s)]
                else:
                    result_text = result_text + ' '
            else:
                result_text = '埃特巴什码只能对英文字母加密！'
        return result_text

    def zhalan_w_encode(self, string, n):
        '''加密'''
        array = self.generate_w(string, n)
        msg = []
        for row in range(n):  # 将每行的字符连起来
            for col in range(len(string)):
                if array[row][col] != '.':
                    msg.append(array[row][col])
        return array, msg

    def generate_w(self, string, n):
        '''将字符排列成w型'''
        array = [['.'] * len(string) for i in range(n)]  # 生成初始矩阵
        row = 0
        upflag = False
        for col in range(len(string)):  # 在矩阵上按w型画出string
            array[row][col] = string[col]
            if row == n - 1:
                upflag = True
            if row == 0:
                upflag = False
            if upflag:
                row -= 1
            else:
                row += 1
        return array

    def VigenereEncrypto(self):
        try:
            self.dialog.close()
            text = self.Ui.Source_text.toPlainText().strip().lower()
            key = self.WChild.key.text()
            ptLen = len(text)
            keyLen = len(key)
            if keyLen == 0:
                self.Ui.Result_text.setPlainText('请输入一个合法的key!')
                return
            quotient = ptLen // keyLen  # 商
            remainder = ptLen % keyLen  # 余
            out = ""
            for i in range(0, quotient):
                for j in range(0, keyLen):
                    c = int((ord(text[i * keyLen + j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
                    # global output
                    out += chr(c)

            for i in range(0, remainder):
                c = int((ord(text[quotient * keyLen + i]) - ord('a') + ord(key[i]) - ord('a')) % 26 + ord('a'))
                # global output
                out += chr(c)

            if out != '':
                self.Ui.Result_text.setPlainText(out)
                return
            else:
                self.Ui.Result_text.setPlainText('加密失败!')
        except Exception as e:
            self.Ui.Result_text.setPlainText(str(e))

    def sifang_encrypt(self):
        self.dialog.close()
        try:
            text = (self.Ui.Source_text.toPlainText().strip()).lower()
            key1 = self.WChild.Key1.text().upper()
            key2 = self.WChild.Key2.text().upper()
            matrix = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
            pla = "abcdefghijklmnoprstuvwxyz"
            key1 = '[' + key1 + "]"
            key2 = '[' + key2 + "]"
            key1 = ''.join(collections.OrderedDict.fromkeys(key1))
            key2 = ''.join(collections.OrderedDict.fromkeys(key2))
            matrix1 = re.sub('[\[\]]', '', key1) + re.sub(key1, '', matrix)
            matrix2 = re.sub('[\[\]]', '', key2) + re.sub(key2, '', matrix)
            matrix_list1 = []
            matrix_list2 = []
            pla_list = []
            for i in range(0, len(matrix1), 5):
                matrix_list1.append(list(matrix1[i:i + 5]))
            for i in range(0, len(matrix2), 5):
                matrix_list2.append(list(matrix2[i:i + 5]))
            for i in range(0, len(pla), 5):
                pla_list.append(list(pla[i:i + 5]))
            pla = text.replace(' ', '')
            if len(pla) % 2 != 0:
                pla += 'x'
            cip = ""
            for i in range(0, len(pla), 2):
                data = pla[i:i + 2]
                # 两个子母中第一个字母位置
                first = self.find_index(data[0], pla_list)
                # 两个子母中第二个字母位置
                second = self.find_index(data[1], pla_list)
                return_cip = ""
                return_cip += matrix_list1[first[0]][second[1]]
                return_cip += matrix_list2[second[0]][first[1]]
                cip += return_cip
            if cip != '':
                self.Ui.Result_text.setPlainText(cip)
            else:
                # return "加密失败！"
                self.Ui.Result_text.setPlainText('加密失败！')

        except Exception as  e:
            self.Ui.Result_text.setPlainText(str(e))
            # print(str(e))

    def gcd(self, a, b):
        if (a < b):
            t = a
            a = b
            b = t

        while (0 != b):
            t = a
            a = b
            b = t % b
        return a

    def fangshe_encrypt(self):
        self.dialog.close()
        try:
            letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 字母表
            text = (self.Ui.Source_text.toPlainText().strip())
            key1 = self.WChild.Key1.text()
            key2 = self.WChild.Key2.text()
            # print(text,key2,key1)
            try:
                if (0 == int(key1.isdigit()) or 0 == int(key2.isdigit())):
                    self.Ui.Result_text.setPlainText('输入有误! 密钥为数字！')
                    return
                if (self.gcd(int(key1), 26) != 1):
                    self.Ui.Result_text.setPlainText('输入有误! key1和26必须互素！')
                    return
            except:
                self.Ui.Result_text.setPlainText('输入有误！')
                return
            else:
                ciphertext = ""
                for ch in text:  # 遍历明文
                    if ch.isalpha():  # 明文是否为字母,如果是,则判断大小写,分别进行加密
                        if ch.isupper():
                            ciphertext += letter_list[(int(key1) * (ord(ch) - 65) + int(key2)) % 26]
                        else:
                            ciphertext += letter_list[(int(key1) * (ord(ch) - 97) + int(key2)) % 26].lower()
                    else:  # 如果密文不为字母,直接添加到密文字符串里
                        ciphertext += ch
                self.Ui.Result_text.setPlainText(ciphertext)
                return
        except Exception as  e:
            self.Ui.Result_text.setPlainText('加密失败！')
            return

    # 查询明文字母位置
    def find_index(self, x, pla_list):
        for i in range(len(pla_list)):
            for j in range(len(pla_list[i])):
                if pla_list[i][j] == x:
                    return i, j

    def zhalan_w_Encrypto(self):
        msg=''
        self.dialog.close()
        plain = self.Ui.Source_text.toPlainText().strip()
        try:
            array, msg = self.zhalan_w_encode(plain, int(self.WChild_zhalan.key.text()))
        except Exception as e:
            self.Ui.Result_text.setPlainText(str(e))
        self.Ui.Result_text.setPlainText(str(''.join(msg)))
        return

    def zhalanEncrypto(self):
        self.dialog.close()
        plain = self.Ui.Source_text.toPlainText().strip()
        try:
            n = int(self.WChild_zhalan.key.text())
            ans = ''
            for i in range(n):
                for j in range(int(plain.__len__() / n + 0.5)):
                    try:
                        ans += plain[j * n + i]
                    except:
                        pass
        except:
            ans = "请输入正确的分组！"
        if ans != '':
            self.Ui.Result_text.setPlainText(ans)
            return
        else:
            self.Ui.Result_text.setPlainText("加密失败!")
            return
    # decrypt
    def decrypt(self, decrypt_type):
        try:
            # print(decrypt_type)
            text = self.Ui.Source_text.toPlainText().strip()
            if text == '':
                self.Ui.Result_text.setPlainText('请输入一个源字符串！')
                return 0
            else:
                result_text = getattr(self, decrypt_type)(text)
                if result_text=='exit':
                    pass
                else:
                    self.Ui.Result_text.setPlainText(result_text)
        except Exception as e:
            self.Ui.Result_text.setPlainText(str(e))
    def actionRot13_decrypt(self,text):
        try:
            PAIRS = {
                "a": "n", "b": "o", "c": "p", "d": "q", "e": "r",
                "f": "s", "g": "t", "h": "u", "i": "v", "j": "w",
                "k": "x", "l": "y", "m": "z", "n": "a", "o": "b",
                "p": "c", "q": "d", "r": "e", "s": "f", "t": "g",
                "u": "h", "v": "i", "w": "j", "x": "k", "y": "l",
                "z": "m", "A": "N", "B": "O", "C": "P", "D": "Q",
                "E": "R", "F": "S", "G": "T", "H": "U", "I": "V",
                "J": "W", "K": "X", "L": "Y", "M": "Z", "N": "A",
                "O": "B", "P": "C", "Q": "D", "R": "E", "S": "F",
                "T": "G", "U": "H", "V": "I", "W": "J", "X": "K",
                "Y": "L", "Z": "M"
            }
            result_text = "".join(PAIRS.get(c, c) for c in text)
        except Exception as  e:
            result_text='解密失败'
        return result_text
    def action_kaisa_decrypt(self, text):
        try:
            t = ""
            for c in text:
                if 'a' <= c <= 'z':  # str是可以直接比较的
                    t += chr(ord('a') + ((ord(c) - ord('a')) - 3) % 26)
                elif 'A' <= c <= 'Z':
                    t += chr(ord('A') + ((ord(c) - ord('A')) - 3) % 26)
                else:
                    t += c
            result_text = t
        except Exception as  e:
            result_text='解密失败'
        return result_text
    def action_zhalan_decrypt(self, text):
        try:
            result_text=''
            factors = [fac for fac in range(2, len(text)) if len(text) % fac == 0]  # 取得密文长度的所有因数
            for fac in factors:
                flag = ''
                for i in range(fac):  # 按一定的步长取几组字符，并连接起来，这里组数就等于步长数
                    flag += text[i::fac]
                result_text += "分为%s栏，解密结果为:%s\n" % (fac, flag)
        except Exception as  e:
            result_text='解密失败'
        return result_text
    def action_zhalan_w_decrypt(self, text):
        try:
            result_text=''
            for n in range(2, len(text)):  # 遍历所有可能的栏数
                # print(str(n) + '栏：' + ''.join(self.zhanlan_w_decode(text, n)[1]))
                result_text += "分为%s栏，解密结果为:%s\n" % (str(n), ''.join(self.zhanlan_w_decode(text, n)[1]))
        except Exception as  e:
            result_text='解密失败'
        return result_text
    def action_peihen_decrypt(self, text):
        try:
            return_str = ''
            dicts = {'aabbb': 'H', 'aabba': 'G', 'baaab': 'R', 'baaaa': 'Q', 'bbaab': 'Z', 'bbaaa': 'Y',
                     'abbab': 'N',
                     'abbaa': 'M', 'babaa': 'U', 'babab': 'V', 'abaaa': 'I', 'abaab': 'J', 'aabab': 'F',
                     'aabaa': 'E',
                     'aaaaa': 'A', 'aaaab': 'B', 'baabb': 'T', 'baaba': 'S', 'aaaba': 'C', 'aaabb': 'D',
                     'abbbb': 'P',
                     'abbba': 'O', 'ababa': 'K', 'ababb': 'L', 'babba': 'W', 'babbb': 'X'}
            sums = len(text)
            j = 5  ##每5个为一组
            for i in range(int(sums / j)):
                result = text[j * i:j * (i + 1)].lower()
                return_str += str(dicts[result], )
            result_text = return_str
        except Exception as  e:
            result_text='解密失败'
        return result_text
    def action_mosi_decrypt(self, text):
        try:
            dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                    '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2',
                    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                    '--...': '7', '---..': '8', '----.': '9', '-----': '0',
                    '..--..': '?', '-..-.': '/', '-.--.-': '()', '-....-': '-',
                    '.-.-.-': '.'
                    }
            msg = ''
            if ' ' in text:
                split_str = ''
            if '/' in text:
                split_str = '/'
            else:
                split_str = text.replace('.', '').replace('-', '')[0:1]
            s = text.split(split_str)
            for item in s:
                if item != '' and item != ' ':
                    msg += (dict[item])
            result_text = msg
        except Exception as  e:
            result_text='解密失败'
        return result_text
    def action_yiwei_decrypt(self, text):
        try:
            inputStr = text
            #
            result = ''
            for j in range(26):
                result_list = []
                for i, num in zip(inputStr, range(len(inputStr))):
                    # print(i)
                    if i.islower:
                        caseS1 = string.ascii_lowercase * 2
                    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        caseS1 = string.ascii_uppercase * 2
                    status = caseS1.find(i)
                    if status != -1:
                        result_list.append(caseS1[status + j])
                    else:
                        result_list.append(inputStr[num])
                text2 = ("".join(result_list), "向右偏移了{}位".format(j))
                result += text2[0] + ' ' + text2[1] + '\n'
            result_text = result
        except Exception as  e:
            result_text='解密失败'
        return result_text
    def action_yunxing_decrypt(self, text):
        try:
            other_letters = []
            for s in text:
                if not ['0', '1', '2', '4', '8'].count(s):
                    other_letters.append(s)
            if other_letters:
                result_text = '加密字符串内只能包含0、1、2、4、8'
            else:
                result_text=''
                charList = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
                ret = []
                plaintext = [i for i in text.split('0')]
                for i in plaintext:
                    tmp = 0
                    for j in range(len(i)):
                        tmp += int(i[j])
                    ret.append(charList[tmp - 1])
                result_text = ''.join(ret)
        except Exception as  e:
            result_text='解密失败'
        return result_text
    def action_dangpu_decry(self, text):
        try:
            mapping_data = {'田': 0, '由': 1, '中': 2, '人': 3, '工': 4, '大': 5, '王': 6, '夫': 7, '井': 8, '羊': 9}
            result_text = ''.join(map(lambda x: str(mapping_data[x]), text))
        except Exception as e :
            result_text='解密失败'
        return result_text
    def action_sifang_decrypt(self, text):
        self.WChild = Ui_KEY2()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild.setupUi(self.dialog)
        self.dialog.setWindowTitle("四方密码")
        self.WChild.key_1.setText("Key square 1：")
        self.WChild.keyl_2.setText("Key square 2：")
        self.dialog.show()
        self.WChild.enter.clicked.connect(self.sifang_decrypt)
        return 'exit'
    def action_fangshe_decrypt(self, text):
        self.WChild = Ui_KEY2()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild.setupUi(self.dialog)
        self.dialog.setWindowTitle("仿射密码")
        self.WChild.key_1.setText("a：")
        self.WChild.keyl_2.setText("b：")
        self.dialog.show()
        self.WChild.enter.clicked.connect(self.fangshe_decrypt)
        return 'exit'
    def action_weinijiya_decrypt(self, text):
        self.WChild = Ui_KEY1()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild.setupUi(self.dialog)
        self.dialog.setWindowTitle("维吉尼亚密码")
        self.WChild.label.setText("Keyword：")
        self.dialog.show()
        self.WChild.keyenter.clicked.connect(self.VigenereDecrypto)
        return 'exit'
    def action_Atbash_decrypt(self, text):
        try:
            str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            str2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
            result_text = ""
            for s in text:
                if s != ' ':
                    result_text = result_text + str1[str2.index(s)]
                else:
                    result_text = result_text + ' '
        except Exception as  e:
            result_text='解密失败'
        return result_text
    def VigenereDecrypto(self):
        try:
            self.dialog.close()
            letter_list = string.ascii_uppercase
            letter_list2 = string.ascii_lowercase
            message = self.Ui.Source_text.toPlainText().strip()
            key = self.WChild.key.text()
            if len(key) == 0:
                self.Ui.Result_text.setPlainText('请输入一个合法的key!')
                return
            key_list = []
            for i in key:
                key_list.append(ord(i.upper()) - 65)
            plaintext = ""
            flag = 0
            for cipher in message:
                if flag % len(key_list) == 0:
                    flag = 0
                if cipher.isalpha():
                    if cipher.isupper():
                        plaintext += letter_list[(ord(cipher) - 65 - key_list[flag]) % 26]
                        flag += 1
                    if cipher.islower():
                        plaintext += letter_list2[(ord(cipher) - 97 - key_list[flag]) % 26]
                        flag += 1
                else:
                    plaintext += cipher
            if plaintext != '':
                # return plaintext
                self.Ui.Result_text.setPlainText(plaintext)
            else:
                # return '解密失败!'
                self.Ui.Result_text.setPlainText('解密失败!')
        except Exception as e:
            # return str(e)
            self.Ui.Result_text.setPlainText(str(e))

    def sifang_decrypt(self):
        self.dialog.close()
        try:
            text = (self.Ui.Source_text.toPlainText().strip()).upper()
            key1 = self.WChild.Key1.text().upper()
            key2 = self.WChild.Key2.text().upper()
            matrix = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
            pla = "abcdefghijklmnoprstuvwxyz"
            key1 = '[' + key1 + "]"
            key2 = '[' + key2 + "]"
            key1 = ''.join(collections.OrderedDict.fromkeys(key1))
            key2 = ''.join(collections.OrderedDict.fromkeys(key2))
            matrix1 = re.sub('[\[\]]', '', key1) + re.sub(key1, '', matrix)
            matrix2 = re.sub('[\[\]]', '', key2) + re.sub(key2, '', matrix)
            matrix_list1 = []
            matrix_list2 = []
            pla_list = []
            # print(matrix1)
            for i in range(0, len(matrix1), 5):
                matrix_list1.append(list(matrix1[i:i + 5]))
            for i in range(0, len(matrix2), 5):
                matrix_list2.append(list(matrix2[i:i + 5]))
            for i in range(0, len(pla), 5):
                pla_list.append(list(pla[i:i + 5]))
            cip = text.replace(' ', '')
            result = ''
            for i in range(0, len(cip), 2):
                letter = cip[i:i + 2]
                # 两个子母中第一个字母位置
                first = self.find_index1(letter[0], matrix_list1)

                # 两个子母中第二个字母位置
                second = self.find_index2(letter[1], matrix_list2)

                return_pla = ""
                return_pla += pla_list[first[0]][second[1]]
                return_pla += pla_list[second[0]][first[1]]
                result += return_pla
            if result != '':
                self.Ui.Result_text.setPlainText(result)
            else:
                self.Ui.Result_text.setPlainText('解密失败！')

        except Exception as e:
            self.Ui.Result_text.setPlainText(str(e))
            # print(str(e))
            pass

    # 求逆元函数
    def GetInverse(self, a, m):
        for i in range(m):
            if (1 == (a * i) % m):
                return i
        return a

    def fangshe_decrypt(self):
        self.dialog.close()
        try:
            key1 = self.WChild.Key1.text()
            key2 = self.WChild.Key2.text()
            try:
                if (0 == int(key1.isdigit()) or 0 == int(key2.isdigit())):
                    self.Ui.Result_text.setPlainText('输入有误! 密钥为数字。')
                    return
                if (self.gcd(int(key1), 26) != 1):
                    key1_list = []
                    result = ''
                    for i in range(0, int(key1)):
                        if self.gcd(i, 26) == 1:
                            key1_list.append(i)
                    for z in key1_list:
                        result += 'key1:%s' % z + '   明文:' + self.fangshe_getdecrypt(int(z), int(key2)) + '\n'

                    self.Ui.Result_text.setPlainText('输入有误! key1和26必须互素。以下为爆破key1的结果\n' + result)
                    return
            except:
                self.Ui.Result_text.setPlainText('输入有误!')
                return
                # self.Ui.Result_text.setPlainText('输入有误!')
            else:
                self.Ui.Result_text.setPlainText(self.fangshe_getdecrypt(int(key1), int(key2)))
        except Exception as e:
            self.Ui.Result_text.setPlainText('解密失败。')
            # print(str(e))
            pass

    def fangshe_getdecrypt(self, key1, key2):
        try:
            text = (self.Ui.Source_text.toPlainText().strip())
            letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 字母表
            plaintext = ""
            for ch in text:  # 遍历密文
                if ch.isalpha():  # 密文为否为字母,如果是,则判断大小写,分别进行解密
                    if ch.isupper():
                        plaintext += letter_list[self.GetInverse(key1, 26) * (ord(ch) - 65 - key2) % 26]
                    else:
                        plaintext += letter_list[self.GetInverse(key1, 26) * (ord(ch) - 97 - key2) % 26].lower()
                else:  # 如果密文不为字母,直接添加到明文字符串里
                    plaintext += ch
            return plaintext
        except:
            return

    # 查询两个密文字母位置
    def find_index1(self, x, matrix_list1):
        for i in range(len(matrix_list1)):
            for j in range(len(matrix_list1[i])):
                if matrix_list1[i][j] == x:
                    return i, j

    def find_index2(self, y, matrix_list2):
        for k in range(len(matrix_list2)):
            for l in range(len(matrix_list2[k])):
                if matrix_list2[k][l] == y:
                    return k, l

    # Binary
    def Binary(self, Binary_type):
        try:
            result_text = ''
            text = self.Ui.Source_text.toPlainText().strip()
            if text == '':
                self.Ui.Result_text.setPlainText('请输入一个源字符串！')
                return 0
            else:
                if Binary_type=='action_others':
                    self.action_get_others()
                else:
                    all_result = ''
                    all_n = text.split("\n")
                    for i in all_n:
                        all_text = i.split(" ")
                        for text in all_text:
                            result_text = getattr(self, Binary_type)(text)
                            if result_text=='exit':
                                pass
                            else:
                                all_result += str(result_text).replace('0o', '').replace('0x', '').replace('0b', '')+' '
                        all_result+='\n'
                    if all_result != "":
                        self.Ui.Result_text.setPlainText(all_result.strip())
                    else:
                        self.Ui.Result_text.setPlainText('转换失败')
        except Exception as e:
            self.Ui.Result_text.setPlainText(str(e))
            pass
    def action2_8(self,text):
        try:
            result = int(text, 2)
            result_text = str(oct(result))
        except Exception as e :
            result_text = '您输入的不是2进制'
        return  result_text

    def action2_10(self, text):
        try:
            result = int(text, 2)
            result_text = str(result)
        except Exception as e :
            result_text = '您输入的不是2进制'
        return result_text

    def action2_16(self, text):
        try:
            result_text = str(hex(int(text, 2)))
        except Exception as e :
            result_text = '您输入的不是2进制'
        return result_text

    def action8_2(self, text):
        try:
            result = int(text, 8)
            result_text = str(bin(result))
        except Exception as e :
            result_text = '您输入的不是8进制'
        return result_text

    def action8_10(self, text):
        try:
            result = int(text, 8)
            result_text = str(result)
        except Exception as e :
            result_text = '您输入的不是8进制'
        return result_text

    def action8_16(self, text):
        try:
            result = int(text, 8)
            result_text = str(hex(result))
        except Exception as e :
            result_text = '您输入的不是8进制'
        return result_text

    def action10_2(self, text):
        try:
            s = int(text)
            result_text = str(bin(s))
        except Exception as e :
            result_text = '您输入的不是10进制'
        return result_text

    def action10_8(self, text):
        try:
            s = int(text)
            result_text = str(oct(s))
        except Exception as e :
            result_text = '您输入的不是10进制'
        return result_text

    def action10_16(self, text):
        try:
            s = int(text)
            result_text = str(hex(s))
        except Exception as e :
            result_text = '您输入的不是10进制'
        return result_text

    def action16_2(self, text):
        try:
            result_text = str(bin(int(text, 16)))
        except Exception as e :
            result_text = '您输入的不是16进制'
        return result_text

    def action16_8(self, text):
        try:
            result = int(text, 16)
            result_text = str(oct(result))
        except Exception as e :
            result_text = '您输入的不是16进制'
        return result_text

    def action16_10(self, text):
        try:
            result = int(text, 16)
            result_text = str(result)
        except Exception as e :
            result_text = '您输入的不是16进制'
        return result_text

    def action_get_others(self):
        self.Binary_dialog = Ui_Binary()
        self.dialog = QtWidgets.QDialog(self)
        self.dialog.setWindowTitle("自定义转换")
        self.Binary_dialog.setupUi(self.dialog)
        self.dialog.show()
        self.Binary_dialog.enter.clicked.connect(self.Binary_conversion)
        return 'exit'


    def Binary_conversion(self):
        try:
            return_Data = ''
            self.dialog.close()
            if self.Binary_dialog.Source.text() != '' and self.Binary_dialog.result.text() != '':
                text = self.Ui.Source_text.toPlainText().strip()
                all_text = text.split(" ")
                all_result = ''
                for text in all_text:
                    # print(text)
                    from_ = int(self.Binary_dialog.Source.text())
                    to_ = int(self.Binary_dialog.result.text())
                    # from_进制转换为十进制
                    ten_num = sum([int(i) * from_ ** n for n, i in enumerate(text[::-1])])
                    # print(ten_num)
                    # 十进制转换为to_进制
                    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']
                    b = []
                    while True:
                        s = ten_num // to_  # 商
                        y = ten_num % to_  # 余数
                        b = b + [y]
                        if s == 0:
                            break
                        ten_num = s
                    b.reverse()
                    for i in b:
                        return_Data = str(a[i])
                    all_result+=return_Data+' '
                self.Ui.Result_text.setPlainText(all_result)
        except Exception as e:
            pass

    def Copy_text(self, text):
        try:
            if text == 'Source':
                data = self.Ui.Source_text.toPlainText().strip()
            if text == 'result':
                data = self.Ui.Result_text.toPlainText()
            # 访问剪切板，存入值
            pyperclip.copy(data)
        except Exception as e:
            pass



    def zhanlan_w_decode(self, string, n):
        '''解密'''
        array = self.generate_w(string, n)
        sub = 0
        for row in range(n):  # 将w型字符按行的顺序依次替换为string
            for col in range(len(string)):
                if array[row][col] != '.':
                    array[row][col] = string[sub]
                    sub += 1
        msg = []
        for col in range(len(string)):  # 以列的顺序依次连接各字符
            for row in range(n):
                if array[row][col] != '.':
                    msg.append(array[row][col])
        return array, msg

    def paste(self, text):
        try:
            data = pyperclip.paste()
            if text == 'Source':
                # print(text)
                source_text = self.Ui.Source_text.toPlainText().strip()  #
                data = source_text + data
                self.Ui.Source_text.setPlainText(data)
            if text == 'result':
                result_text = self.Ui.Result_text.toPlainText()  #
                data = result_text + data
                self.Ui.Result_text.setPlainText(data)
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
        fileName, selectedFilter = QFileDialog.getOpenFileName(self, (r"上传文件"), (r"C:\windows"), type)
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
    def str_place(self):
        self.WChild_replace = Ui_KEY2()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild_replace.setupUi(self.dialog)
        self.dialog.setWindowTitle("替换")
        self.WChild_replace.key_1.setText("查找内容：")
        self.WChild_replace.keyl_2.setText("替换内容：")
        self.WChild_replace.enter.setText("替换输入文本")
        self.WChild_replace.quxiao.setText("替换输出文本")
        self.dialog.show()
        self.WChild_replace.enter.clicked.connect(lambda: self.str_replace("Source"))
        self.WChild_replace.quxiao.clicked.connect(lambda: self.str_replace("Result"))
    def str_chaifen(self):
        self.WChild_chaifen = Ui_KEY1()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild_chaifen.setupUi(self.dialog)
        self.dialog.setWindowTitle("字符串长度拆分")
        self.WChild_chaifen.label.setText("请输入字符串长度:")
        self.dialog.show()
        self.WChild_chaifen.keyenter.clicked.connect(self.str_chaifen_chuli)
    def str_chaifen_chuli(self):
        text = self.Ui.Source_text.toPlainText().strip()
        try:
            changdu = int(self.WChild_chaifen.key.text())
        except:
            return_text='请输入一个数字。'
            self.Ui.Result_text.setPlainText(str(return_text))
            return
        if changdu>len(text):
            return_text = '分割长度大于字符串长度。'
        else:
            text = [text[i:i + changdu] for i in range(0, len(text), changdu)]
            # text = re.findall(r'.{'+str(changdu)+'}', text)
            return_text = ' '.join(text)
            pass
        self.Ui.Result_text.setPlainText(str(return_text))
        self.dialog.close()

    def str_split(self):
        self.WChild_split = Ui_KEY1()
        self.dialog = QtWidgets.QDialog(self)
        self.WChild_split.setupUi(self.dialog)
        self.dialog.setWindowTitle("字符串分割")
        self.WChild_split.label.setText("请输入分隔符号:")
        self.dialog.show()
        self.WChild_split.keyenter.clicked.connect(self.str_split_chuli)
    def str_split_chuli(self):
        text = self.Ui.Source_text.toPlainText().strip()
        split_str = self.WChild_split.key.text()
        text  = text.split(split_str)
        return_text = ' '.join(text)
        self.Ui.Result_text.setPlainText(str(return_text.strip()))
        self.dialog.close()
    def str_tongji(self):
        data = self.Ui.Source_text.toPlainText().strip()
        s = ''
        l = len(data)
        for x in range(0, l):
            if not data[x] in s:
                s += data[x]
        result = {d: 0 for d in s}
        for d in data:
            for alpha in s:
                if d == alpha:
                    result[alpha] = result[alpha] + 1

        result1 = sorted(result.items(), key=lambda x: x[1], reverse=True)
        return_text ='大->小:\n'
        for x in result1:
            return_text +=str(x[1])
        return_text += '\n\n小->大:\n'
        result2 = sorted(result.items(), key=lambda x: x[1], reverse=False)
        for x in result2:
            return_text +=str(x[1])
        return_text += '\n\n'
        for x in result1:
            return_text +=x[0]+":"+str(x[1])+'\n'
        self.Ui.Result_text.setPlainText(return_text)

        # print(type(result))
    def str_re(self):
        text = self.Ui.Source_text.toPlainText().strip()
        self.Ui.Result_text.setPlainText(str(text[::-1]))
    def keyPressEvent(self,event):
        # print("按下：" + str(event.key()))
        if event.key() == QtCore.Qt.Key_H:
            self.str_place()
            # if QApplication.keyboardModifiers() == Qt.ControlModifier:
            #     self.actionFile.save(self.action_text.toPlainText())
            #     self.status.showMessage("保存成功 %s" % self.file)
    def str_replace(self,type):
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


    def zhuan_yuanwenben(self):
        text = self.Ui.Result_text.toPlainText()
        if text:
            self.Ui.Source_text.setPlainText(text)
    def open_xiandaimima(self):
        self.form_xiandaimima = QtWidgets.QWidget()
        self.xiandaimima_widget = Ui_Form_Xiandaimima()
        self.xiandaimima_widget.setupUi(self.form_xiandaimima)
        self.form_xiandaimima.setStyleSheet(qss_style)
        self.form_xiandaimima.setWindowIcon(QtGui.QIcon('./logo.ico'))
        self.form_xiandaimima.show()
        self.xiandaimima_widget.AES_Encrypto.clicked.connect(self.AES_Encrypto)
        self.xiandaimima_widget.AES_Decrypto.clicked.connect(self.AES_Decrypto)
        self.xiandaimima_widget.AES_Mode.activated[str].connect(self.change_aes_setting)

        # print(values)
        # self.WChild_xiandaimima.vuln_name.setText(values[0]['vuln_name'])
        # self.WChild_xiandaimima.cms_name.setText(values[0]['cms_name'])
    def change_aes_setting(self):
        AES_Mode = self.xiandaimima_widget.AES_Mode.currentText()
        if AES_Mode=='ECB':
            self.xiandaimima_widget.AES_Pianyi.setEnabled(False)
        else:
            self.xiandaimima_widget.AES_Pianyi.setEnabled(True)

    def AES_Encrypto(self):
        aes_mode = self.xiandaimima_widget.AES_Mode.currentText()
        aes_zifuji = self.xiandaimima_widget.AES_zifuji.currentText()
        aes_tianchong = self.xiandaimima_widget.AES_Tianchong.currentText()
        aes_iv = self.xiandaimima_widget.AES_Pianyi.text()
        aes_encode = self.xiandaimima_widget.AES_Bianma.currentText()
        aes_key  =  self.xiandaimima_widget.AES_Miyao.text()
        aes_m_text = self.xiandaimima_widget.AES_Source.toPlainText()
        if not  aes_key:
            QMessageBox.critical(self.form_xiandaimima, 'Error','AES密钥不能为空')
            return
        else:
            if len(aes_key)!=16 and len(aes_key)!=24 and len(aes_key)!=32:
                QMessageBox.critical(self.form_xiandaimima, 'Error', 'AES密钥应为16、24、32位')
                return
            else:
                aes_key =aes_key.encode(aes_zifuji)
            if aes_mode not in ["ECB"]:
                if len(aes_iv) !=16:
                    QMessageBox.critical(self.form_xiandaimima, 'Error', 'AES偏移长度必须为16位')
                    return
                if not aes_iv:
                    QMessageBox.critical(self.form_xiandaimima, 'Error', '偏移不能为空！')
                    return
                else:
                    aes_iv = aes_iv.encode(aes_zifuji)

        if not aes_m_text:
            QMessageBox.critical(self.form_xiandaimima, 'Error','请输入明文')
            return
        else:
            aes_m_text = self.aes_buqi_(aes_m_text.encode(aes_zifuji),len(aes_key),aes_tianchong,aes_zifuji)
        if aes_mode =="CBC":
            cryptor = AES.new(aes_key, AES.MODE_CBC, aes_iv)
        elif aes_mode =="ECB":
            cryptor = AES.new(aes_key, AES.MODE_ECB)
        elif aes_mode =="CFB":
            cryptor = AES.new(aes_key, AES.MODE_CFB, aes_iv)
        elif aes_mode =="CTR":
            ctr = Crypto.Util.Counter.new(128, initial_value=int(binascii.hexlify(aes_iv), 16))
            cryptor = AES.new(aes_key, AES.MODE_CTR,counter=ctr)
        elif aes_mode =="OFB":
            cryptor = AES.new(aes_key, AES.MODE_OFB, aes_iv)
        else:
            QMessageBox.critical(self.form_xiandaimima, 'Error','加密模式设置错误')
            return
        return_text = cryptor.encrypt(aes_m_text)
        if aes_encode =='Base64':
            return_text = str(base64.encodebytes(return_text), encoding=aes_zifuji).strip()

        elif aes_encode == 'Hex':
            return_text =  str(binascii.b2a_hex(return_text),encoding=aes_zifuji).strip()
        # print(return_text)
        self.xiandaimima_widget.AES_Result.setPlainText(return_text)
    def AES_Decrypto(self):
        aes_mode = self.xiandaimima_widget.AES_Mode.currentText()
        aes_zifuji = self.xiandaimima_widget.AES_zifuji.currentText()
        aes_iv = self.xiandaimima_widget.AES_Pianyi.text()
        aes_encode = self.xiandaimima_widget.AES_Bianma.currentText()
        aes_key  =  self.xiandaimima_widget.AES_Miyao.text()
        aes_m_text = self.xiandaimima_widget.AES_Result.toPlainText()
        if not  aes_key:
            QMessageBox.critical(self.form_xiandaimima, 'Error','AES密钥不能为空')
            return
        else:
            if len(aes_key)!=16 and len(aes_key)!=24 and len(aes_key)!=32:
                QMessageBox.critical(self.form_xiandaimima, 'Error', 'AES密钥应为16、24、32位')
                return
            else:
                aes_key =aes_key.encode(aes_zifuji)
            if aes_mode not in ["ECB"]:
                if len(aes_iv) !=16:
                    QMessageBox.critical(self.form_xiandaimima, 'Error', 'AES偏移长度必须为16位')
                    return
                if not aes_iv:
                    QMessageBox.critical(self.form_xiandaimima, 'Error', '偏移不能为空！')
                    return
                else:
                    aes_iv = aes_iv.encode(aes_zifuji)

        if not aes_m_text:
            QMessageBox.critical(self.form_xiandaimima, 'Error','请输入明文')
            return
        else:
            if aes_encode == 'Base64':
                aes_m_text = base64.b64decode(aes_m_text.encode(aes_zifuji))
            elif aes_encode == 'Hex':
                aes_m_text = bytes.fromhex(aes_m_text)
        if aes_mode == "CBC":
            cryptor = AES.new(aes_key, AES.MODE_CBC, aes_iv)
        elif aes_mode == "ECB":
            cryptor = AES.new(aes_key, AES.MODE_ECB)
        elif aes_mode == "CFB":
            cryptor = AES.new(aes_key, AES.MODE_CFB, aes_iv)
        elif aes_mode == "CTR":
            ctr = Crypto.Util.Counter.new(128, initial_value=int(binascii.hexlify(aes_iv), 16))
            cryptor = AES.new(aes_key, AES.MODE_CTR, counter=ctr)
        elif aes_mode == "OFB":
            cryptor = AES.new(aes_key, AES.MODE_OFB, aes_iv)
        else:
            QMessageBox.critical(self.form_xiandaimima, 'Error', '加密模式设置错误')
            return
        try:
            return_text = cryptor.decrypt(aes_m_text)
            ret = self._unpad(return_text)
            return_text = ret.decode(aes_zifuji)

        except:
            return_text = '解密失败'

        self.xiandaimima_widget.AES_Source.setPlainText(return_text.strip())

    def _unpad(self,s):
        return s[:-ord(s[len(s) - 1:])]

    # https://baijiahao.baidu.com/s?id=1706700589435327561&wfr=spider&for =pc
    def aes_buqi_(self,text,length,aes_tianchong,aes_zifuji):
        if aes_tianchong=="ZeroPadding":
            tianchong_str = '\0'
            # length = 16
            count = len(text)
            if count < length:
                add = (length - count)
                # \0 backspace
                # text = text + ('\0' * add)
                text = text + (tianchong_str * add).encode(aes_zifuji)
            elif count > length:
                add = (length - (count % length))
                # text = text + ('\0' * add)
                text = text + (tianchong_str * add).encode(aes_zifuji)
            return text
        elif aes_tianchong=="Pkcs7":
            bs = 16
            # length = len(text)
            # bytes_length = len(text)
            # padding_size = length if (bytes_length == length) else bytes_length
            padding_size = len(text)
            padding = bs - padding_size % bs
            padding_text = chr(padding) * padding
            # print(text+ padding_text.encode(aes_zifuji))
            return (text+ padding_text.encode(aes_zifuji))
        elif aes_tianchong == "Iso10126":
            bs=16
            padding_size = len(text)
            padding = bs - padding_size % bs
            # * padding-1
            qian_Str=''
            for i in range(0,padding-1):
                qian_Str +=  chr(random.randint(0,9))
            padding_text = qian_Str+chr(padding)
            return (text + padding_text.encode(aes_zifuji))
        elif aes_tianchong=="AnsiX923":
            bs=16
            tianchong_str='\0'
            padding_size = len(text)
            padding = bs - padding_size % bs
            text = text + (tianchong_str * (padding-1)+chr(padding)).encode(aes_zifuji)
            return text
        elif aes_tianchong=="No Padding":
            while len(text) % 16 != 0:
                text += '\0'.encode(aes_zifuji)
            return text

        else:
            tianchong_str = '\0'
            # length = 16
            count = len(text)
            if count < length:
                add = (length - count)
                # \0 backspace
                # text = text + ('\0' * add)
                text = text + (tianchong_str * add).encode(aes_zifuji)
            elif count > length:
                add = (length - (count % length))
                # text = text + ('\0' * add)
                text = text + (tianchong_str * add).encode(aes_zifuji)
            return text


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
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
