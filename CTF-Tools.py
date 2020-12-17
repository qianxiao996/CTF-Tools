import html,base64,sys,string,os,urllib.parse,random,collections,re
import importlib.machinery
import webbrowser

import requests

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import win32con,json
import win32clipboard as wincld
from GUI.main import Ui_MainWindow
from GUI.KEY_1 import Ui_KEY1
from GUI.Binary import Ui_Binary
from GUI.KEY_2 import Ui_KEY2
import frozen_dir
SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)
version = '1.2.6'
update_time = '20201217'
class MainWindows(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindows,self).__init__(parent)
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.about_text = "\t\t\tAbout\n       此程序为CTF密码学辅助工具，可进行常见的编码、解码、加密、解密操作，请勿非法使用！\n\t\t\tPowered by qianxiao996"
        self.author_text = "作者邮箱：qianxiao996@126.com\n作者主页：https://blog.qianxiao996.cn\nGithub：https://github.com/qianxiao996"

        self.setWindowTitle('CTF-Tools V '+version+' '+update_time+' By qianxiao996 ')
        # self.setFixedSize(self.width(), self.height()) ##设置宽高不可变
        self.setWindowIcon(QtGui.QIcon('./logo.ico'))
        self.Ui.Source_clear_Button.clicked.connect(lambda:self.Ui.Source_text.clear())  # clear_source
        self.Ui.Result_clear_Button.clicked.connect(lambda:self.Ui.Result_text.clear())  # clear_result
        self.Ui.Source_Copy_Button.clicked.connect(lambda:self.Copy_text('Source'))  # copy_source
        self.Ui.Result_Copy_Button.clicked.connect(lambda:self.Copy_text('result'))  # copy_result
        self.Ui.Source_tihuan_Button.clicked.connect(lambda:self.tihuan('Source'))  # tihuan_source
        self.Ui.Result_tihuan_Button.clicked.connect(lambda:self.tihuan('result'))  # tihuan_result
        self.Ui.Source_Paste_Button.clicked.connect(lambda: self.paste('Source'))  # paste_Source
        self.Ui.Result_Paste_Button.clicked.connect(lambda: self.paste('result'))  # paste_result
        #encode
        self.Ui.actionURL_UTF8_encode.triggered.connect(lambda:self.encode(self.Ui.actionURL_UTF8_encode.text()))
        self.Ui.actionURL_GB2312_encode.triggered.connect(lambda: self.encode(self.Ui.actionURL_GB2312_encode.text()))
        self.Ui.actionUnicode_encode.triggered.connect(lambda: self.encode(self.Ui.actionUnicode_encode.text()))
        self.Ui.actionEscape_U_encode.triggered.connect(lambda: self.encode(self.Ui.actionEscape_U_encode.text()))
        self.Ui.actionHtmlEncode_encode.triggered.connect(lambda: self.encode(self.Ui.actionHtmlEncode_encode.text()))
        self.Ui.actionASCII_encode.triggered.connect(lambda: self.encode(self.Ui.actionASCII_encode.text()))
        self.Ui.actionBase16_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase16_encode.text()))
        self.Ui.actionBase32_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase32_encode.text()))
        self.Ui.actionBase64_encode.triggered.connect(lambda: self.encode(self.Ui.actionBase64_encode.text()))
        self.Ui.actionStr_Hex_encode.triggered.connect(lambda: self.encode(self.Ui.actionStr_Hex_encode.text()))
        self.Ui.actionShellcode_encode.triggered.connect(lambda: self.encode(self.Ui.actionShellcode_encode.text()))
        self.Ui.actionQwerty_encode.triggered.connect(lambda: self.encode(self.Ui.actionQwerty_encode.text()))
        self.Ui.actiontupian_base64_encode.triggered.connect(lambda: self.encode(self.Ui.actiontupian_base64_encode.text()))
        #decode
        self.Ui.actionURL_UTF8_decode.triggered.connect(lambda:self.decode(self.Ui.actionURL_UTF8_decode.text()))
        self.Ui.actionURL_GB2312_decode.triggered.connect(lambda: self.decode(self.Ui.actionURL_GB2312_decode.text()))
        self.Ui.actionUnicode_decode.triggered.connect(lambda: self.decode(self.Ui.actionUnicode_decode.text()))
        self.Ui.actionEscape_U_decode.triggered.connect(lambda: self.decode(self.Ui.actionEscape_U_decode.text()))
        self.Ui.actionHtmlEncode_decode.triggered.connect(lambda: self.decode(self.Ui.actionHtmlEncode_decode.text()))
        self.Ui.actionASCII_decode.triggered.connect(lambda: self.decode(self.Ui.actionASCII_decode.text()))
        self.Ui.actionBase16_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase16_decode.text()))
        self.Ui.actionBase32_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase32_decode.text()))
        self.Ui.actionBase64_decode.triggered.connect(lambda: self.decode(self.Ui.actionBase64_decode.text()))
        self.Ui.actionHex_Str_decode.triggered.connect(lambda: self.decode(self.Ui.actionHex_Str_decode.text()))
        self.Ui.actionShellcode_decode.triggered.connect(lambda: self.decode(self.Ui.actionShellcode_decode.text()))
        self.Ui.actionQwerty_decode.triggered.connect(lambda: self.decode(self.Ui.actionQwerty_decode.text()))
        self.Ui.actionbase64_tupian_decode.triggered.connect(lambda: self.decode(self.Ui.actionbase64_tupian_decode.text()))
        #encrypt
        self.Ui.actionRot13_encrypt.triggered.connect(lambda:self.encrypt(self.Ui.actionRot13_encrypt.text()))
        self.Ui.action_kaisa_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_kaisa_encrypt.text()))
        self.Ui.action_zhalan_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_zhalan_encrypt.text()))
        self.Ui.action_peigen_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_peigen_encrypt.text()))
        self.Ui.action_mosi_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_mosi_encrypt.text()))
        self.Ui.action_yunying_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_yunying_encrypt.text()))
        self.Ui.action_dangpu_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_dangpu_encrypt.text()))
        self.Ui.action_sifang_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_sifang_encrypt.text()))
        self.Ui.action_weinijiya_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_weinijiya_encrypt.text()))
        self.Ui.action_Atbash_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_Atbash_encrypt.text()))
        self.Ui.action_fangshe_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_fangshe_encrypt.text()))

        #decrypt
        self.Ui.actionRot13_decrypt.triggered.connect(lambda:self.decrypt(self.Ui.actionRot13_decrypt.text()))
        self.Ui.action_kaisa_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_kaisa_decrypt.text()))
        self.Ui.action_zhalan_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_zhalan_decrypt.text()))
        self.Ui.action_peihen_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_peihen_decrypt.text()))
        self.Ui.action_mosi_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_mosi_decrypt.text()))
        self.Ui.action_yiwei_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_yiwei_decrypt.text()))
        self.Ui.action_yunxing_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_yunxing_decrypt.text()))
        self.Ui.action_dangpu_decry.triggered.connect(lambda: self.decrypt(self.Ui.action_dangpu_decry.text()))
        self.Ui.action_sifang_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_sifang_decrypt.text()))
        self.Ui.action_weinijiya_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_weinijiya_decrypt.text()))
        self.Ui.action_Atbash_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_Atbash_decrypt.text()))
        self.Ui.action_fangshe_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_fangshe_decrypt.text()))

        #进制转换
        self.Ui.action2_8.triggered.connect(lambda:self.Binary(self.Ui.action2_8.text()))
        self.Ui.action2_10.triggered.connect(lambda: self.Binary(self.Ui.action2_10.text()))
        self.Ui.action2_16.triggered.connect(lambda: self.Binary(self.Ui.action2_16.text()))
        self.Ui.action8_2.triggered.connect(lambda: self.Binary(self.Ui.action8_2.text()))
        self.Ui.action8_10.triggered.connect(lambda: self.Binary(self.Ui.action8_10.text()))
        self.Ui.action8_16.triggered.connect(lambda: self.Binary(self.Ui.action8_16.text()))
        self.Ui.action10_2.triggered.connect(lambda: self.Binary(self.Ui.action10_2.text()))
        self.Ui.action10_8.triggered.connect(lambda: self.Binary(self.Ui.action10_8.text()))
        self.Ui.action10_16.triggered.connect(lambda: self.Binary(self.Ui.action10_16.text()))
        self.Ui.action16_2.triggered.connect(lambda: self.Binary(self.Ui.action16_2.text()))
        self.Ui.action16_8.triggered.connect(lambda: self.Binary(self.Ui.action16_8.text()))
        self.Ui.action16_10.triggered.connect(lambda: self.Binary(self.Ui.action16_10.text()))
        self.Ui.action_others.triggered.connect(lambda: self.Binary(self.Ui.action_others.text()))
        self.Ui.actionAbout.triggered.connect(self.about)
        self.Ui.actionAuthor.triggered.connect(self.author)
        self.Ui.actionUpdate_2.triggered.connect(self.Update)

        self.readfile()
        #Website
        websitemenubar = self.menuBar()  # 获取窗体的菜单栏
        Website = websitemenubar.addMenu("Website")
        for i in json_data:
            impMenu = QMenu(i, self)
            url_list  = json_data[i].split('\n')
            for j in url_list:
                sub_action = QAction(QIcon(''), j, self)
                impMenu.addAction(sub_action)
            Website.addMenu(impMenu)
        Website.triggered[QAction].connect(self.show_json)
        #Plugins
        Pluginsmenubar = self.menuBar()  # 获取窗体的菜单栏
        plugins = Pluginsmenubar.addMenu("Plugins")
        for k in plugins_data:
            # print(k)
            sub_action = QAction(QIcon(''), k, self)
            plugins.addAction(sub_action)
        plugins.triggered[QAction].connect(self.show_plugins)
        #Others
        othersmenubar = self.menuBar()  # 获取窗体的菜单栏
        others = othersmenubar.addMenu("Others")
        for j in ["About",'Author','Update']:
            sub_action = QAction(QIcon(''), j, self)
            others.addAction(sub_action)
        impMenu = QMenu("Style", self)
        for z in json_qss:
            sub_action = QAction(QIcon(''), z, self)
            impMenu.addAction(sub_action)
        others.addMenu(impMenu)
        others.triggered[QAction].connect(self.show_others)
    def show_others(self,q):
        if q.text() =="About":
            self.about()
            return
        if q.text() =="Author":
            self.author()
            return
        if q.text() =="Update":
            self.Update()
            return
        else:
            try:
                with open("QSS/" + json_qss[q.text()], 'r', encoding='utf-8') as f:
                    qss_style = f.read()
                    f.close()
                MainWindows.setStyleSheet(self, qss_style)
                f = open('QSS/Setup.txt', 'w', encoding='utf-8')
                f.write('{"QSS": "%s"}'%json_qss[q.text()])
                f.close()
                python = sys.executable
                os.execl(python, python, *sys.argv)
            except Exception as e:
                QMessageBox.critical(self, 'Error', str(e))
                pass
    def show_plugins(self,q):
        try:
            plugins_methods = "Plugins/" + plugins_data[q.text()][:-3]
            filename = "Plugins/" + plugins_data[q.text()]
            text = self.Ui.Source_text.toPlainText()
            if text=='':
                self.Ui.Result_text.setText('请输入一个源字符串！')
                return 0
            nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(plugins_methods, filename).load_module()
            result = nnnnnnnnnnnn1.run(text)
            self.Ui.Result_text.setText(str(result))
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))
            pass

    def show_json(self,q):
        # print(q.text())
        wincld.OpenClipboard()
        wincld.EmptyClipboard()
        wincld.SetClipboardData(win32con.CF_UNICODETEXT, q.text())
        wincld.CloseClipboard()
        reply = QMessageBox.question(self, 'Message', "链接已复制到剪切板，是否在浏览器中打开链接?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            webbrowser.open(q.text())
        else:
            pass

    def readfile(self):
        try:
            global json_data
            f=open('data.json','r',encoding='utf-8')
            json_data=json.load(f)
            # print(json_data)
            f.close()
            global json_qss
            f=open('QSS/list.txt','r',encoding='utf-8')
            json_qss=json.load(f)
            # print(json_data)
            f.close()
            f=open('QSS/Setup.txt','r',encoding='utf-8')
            qss_Setup=json.load(f)
            with open("QSS/"+qss_Setup["QSS"], 'r', encoding='utf-8') as f:
                qss_style = f.read()
                f.close()
            MainWindows.setStyleSheet(self,qss_style)
            # print(json_data)
            f.close()
            global plugins_data
            f = open('Plugins/Plugins.json', 'r', encoding='utf-8')
            plugins_data = json.load(f)
            # print(plugins_data)
            f.close()
        except Exception as e :
            QMessageBox.critical(self,'Error',str(e))
            pass

    #编码
    def encode(self,encode_type):
        try:
            result_text=''
            # print(encode_type)
            if encode_type == '图片->base64':
                try:
                    filename = self.file_open(r"Text Files (*.jpg);;All files(*.*)")
                    with open(filename, 'rb') as f:
                        base64_data = base64.b64encode(f.read())
                        s = base64_data.decode()
                    self.Ui.Result_text.setText(str('data:image/%s;base64,%s' % (filename[-3:],s)))
                    return
                except:
                    self.Ui.Result_text.setText('转换失败！')
                    return
            text = self.Ui.Source_text.toPlainText()
            if text=='':
                self.Ui.Result_text.setText('请输入一个源字符串！')
                return 0
            # print(encode_type)
            if encode_type=='URL-UTF8':
                text = text.encode('utf-8')
                result_text = urllib.parse.quote(text)
            elif encode_type == 'URL-GB2312':
                text = text.encode('gb2312')
                result_text = urllib.parse.quote(text)
            elif encode_type=='Unicode':
                text = text.encode('unicode_escape')
                result_text = str(text, encoding='utf-8')
            elif encode_type=='Escape(%U)':
                text = text.encode('unicode_escape')
                result_text = str(text, encoding='utf-8').replace('\\u', '%u')
            elif encode_type=='HtmlEncode':
                result_text = html.escape(text)
            elif encode_type=='ASCII':
                result = ''
                for i in text:
                    result = str(result) + str(ord(str(i))) + ' '
                result_text=str(result)[:-1]
            elif encode_type=='Base16':
                text = base64.b16encode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            elif encode_type=='Base32':
                text = base64.b32encode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            elif encode_type=='Base64':
                text = base64.b64encode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            elif encode_type=='Str->Hex':
                result = ''
                for i in text:
                    single = str(hex(ord(str(i))))
                    result = result + single
                result_text='0x' + (str(result)).replace('0x', '')
            elif encode_type=='Shellcode':
                result = ''
                for i in text:
                    single = str(hex(ord(str(i))))
                    result = result + single
                result_text=(str(result)).replace('0x', '\\x')
            elif encode_type=='Qwerty':
                str1 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
                str2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                result_text = ""
                for s in text:
                    if s in str1:
                        if s !=' ':
                            result_text = result_text + str1[str2.index(s)]
                        else:
                            result_text = result_text+' '
                    else:
                        result_text ='Qwerty只能对字母加密!'
            if result_text!="":
                self.Ui.Result_text.setText(str(result_text))
            else:
                self.Ui.Result_text.setText("编码失败！")
        except Exception as e :
            self.Ui.Result_text.setText(str(e))
            pass
            # print(str(e))
    #解码
    def decode(self,decode_type):
        try:
            result_text=''
            # print(decode_type)
            text = self.Ui.Source_text.toPlainText()
            if text=='':
                self.Ui.Result_text.setText('请输入一个源字符串！') 
                return 0
            if decode_type=='URL-UTF8':
                result_text = str(urllib.parse.unquote(text))
            elif decode_type == 'URL-GB2312':
                result_text = str(urllib.parse.unquote(text, 'gb2312'))
            elif decode_type=='Unicode':
                result_text = bytes(text, encoding="utf8").decode('unicode_escape')
            elif decode_type=='Escape(%U)':
                text = text.replace('%u', '\\u').replace('%U', '\\u')
                result_text = bytes(text, encoding="utf8").decode('unicode_escape')
            elif decode_type=='HtmlEncode':
                result_text = html.unescape(text)
            elif decode_type=='ASCII':
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
                    text=list22
                # print(text)
                result = ''
                for i in text:
                    if i != '':
                        # print(i)
                        # print(chr(int(i)))
                        result = result + chr(int(i))
                result_text =result
            elif decode_type=='Base16':
                text = base64.b16decode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            elif decode_type=='Base32':
                text = base64.b32decode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            elif decode_type=='Base64':
                text = base64.b64decode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            elif decode_type=='Hex->Str':
                text = text.replace('0x', '').replace('0X', '')
                result_text = str(bytes.fromhex(text), encoding="utf-8")
            elif decode_type=='Shellcode':
                result = ''
                text = text.split('\\x')
                for i in text:
                    single = str(bytes.fromhex(i), encoding="utf-8")
                    result = result + single
                result_text =str(result)
            elif decode_type=='Qwerty':
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
            elif decode_type == 'base64->图片':
                try:
                    file_name = self.file_save('tupian.jpg')
                    # print(file_name)
                    str2 = base64.b64decode(text.replace('data:image/jpg;base64,','').replace('data:image/jpeg;base64,','').replace('data:image/png;base64,','').replace('data:image/gif;base64,',''))
                    file1 = open(file_name, 'wb')
                    file1.write(str2)
                    file1.close()
                    QMessageBox.information(self,'Success','转换成功，文件位置:%s'%file_name)
                    result_text='转换成功，文件位置:\n%s'%file_name
                except:
                    pass
            if result_text!="":
                self.Ui.Result_text.setText(str(result_text))
            else:
                self.Ui.Result_text.setText('解码失败!')
        except Exception as e :
            self.Ui.Result_text.setText(str(e)) 
            # print(e)
            pass
    #encrypt
    def encrypt(self,encrypt_type):
        try:
            result_text=''
            # print(encrypt_type)
            text = self.Ui.Source_text.toPlainText()
            if text=='':
                self.Ui.Result_text.setText('请输入一个源字符串！')
                return 0
            if encrypt_type=='Rot13':
                d = {chr(i + c): chr((i + 13) % 26 + c) for i in range(26) for c in (65, 97)}
                result_text = ''.join([d.get(c, c) for c in text])
            elif encrypt_type=='凯撒密码':
                t = ""
                for c in text:
                    if 'a' <= c <= 'z':  # str是可以直接比较的
                        t += chr(ord('a') + ((ord(c) - ord('a')) + 3) % 26)
                    elif 'A' <= c <= 'Z':
                        t += chr(ord('A') + ((ord(c) - ord('A')) + 3) % 26)
                    else:
                        t += c
                result_text=t
            elif encrypt_type=='栅栏密码':
                self.WChild_zhalan = Ui_KEY1()
                self.dialog = QtWidgets.QDialog(self)
                self.WChild_zhalan.setupUi(self.dialog)
                self.dialog.show()
                self.WChild_zhalan.keyenter.clicked.connect(self.zhalanEncrypto)
                return 0
            elif encrypt_type=='培根密码':
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
                result_text = listStr.upper() # 大写输出
            elif encrypt_type=='摩斯密码':
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
                        '9': '----.', '?': '..--..','/': '-..-.',
                        '()': '-.--.-','-': '-....-','.': '.-.-.-'
                        }
                msg = ''
                for char in text:
                    if char in CODE:
                        if char == ' ':
                            pass
                        else:
                            msg+=(CODE[char.upper()] + ' ')
                    else:
                        msg = '文本中含有不能识别的字符！'
                result_text =msg
            elif encrypt_type=='云影密码':
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
                        for j in range(0,int(i/8)):
                            res+= '8'
                    if i % 8 >= 4:
                        for j in range(0,int(i % 8 / 4)):
                            res+= '4'
                    if i % 4 >= 2:
                        for j in range(0,int(i % 4 / 2)):
                            res+= '2'
                    if i % 2 >= 1:
                        for j in range(0,int(i % 2 / 1)):
                            res+= '1'
                    ret.append(res + '0')
                result_text= ''.join(ret)[:-1]
                # print(result_text)
            elif encrypt_type == '四方密码':
                self.WChild = Ui_KEY2()
                self.dialog = QtWidgets.QDialog(self)
                self.WChild.setupUi(self.dialog)
                self.dialog.show()
                self.WChild.enter.clicked.connect(self.sifang_encrypt)
                return
            elif encrypt_type == '当铺密码':
                mapping_data =[['田'], ['由'], ['中'], ['人'], ['工'], ['大'], ['王'], ['夫'], ['井'], ['羊']]
                try:
                    result = []
                    for c in text:
                        c_list = mapping_data[int(c)]
                        c_index = random.randint(0, len(c_list) - 1)
                        result.append(c_list[c_index])
                    result_text = ''.join(result)
                except:
                    result_text='未找到该字符串对应的中文！'
            elif encrypt_type == '仿射密码':
                self.WChild = Ui_KEY2()
                self.dialog = QtWidgets.QDialog(self)
                self.WChild.setupUi(self.dialog)
                self.dialog.show()
                self.WChild.enter.clicked.connect(self.fangshe_encrypt)
                return

            elif encrypt_type=='维吉尼亚密码':
                self.WChild = Ui_KEY1()
                self.dialog = QtWidgets.QDialog(self)
                self.WChild.setupUi(self.dialog)
                self.dialog.show()
                self.WChild.keyenter.clicked.connect(self.VigenereEncrypto)
                return 0
            elif encrypt_type=='埃特巴什码':
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
            if result_text!="":
                self.Ui.Result_text.setText(result_text)
            else:
                self.Ui.Result_text.setText('加密失败!')
        except Exception as e :
            self.Ui.Result_text.setText(str(e)) 
            # QMessageBox.critical(self,'Error',str(e))
            # print(str(e))
            pass
    def VigenereEncrypto(self):
        try:
            self.dialog.close()
            text = self.Ui.Source_text.toPlainText()
            key = self.WChild.key.text()
            ptLen = len(text)
            keyLen =  len(key)
            if keyLen==0:
                self.Ui.Result_text.setText(str('请输入一个合法的key！')) 
                return 0
            quotient = ptLen // keyLen    #商
            remainder = ptLen % keyLen    #余
            out = ""
            for i in range (0 , quotient) :
                for j in range (0 , keyLen) :
                    c = int((ord(text[i*keyLen+j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
                    #global output
                    out += chr (c)

            for i in range (0 , remainder) :
                c =  int((ord(text[quotient*keyLen+i]) - ord('a') + ord(key[i]) - ord('a')) % 26 + ord('a'))
                #global output
                out += chr (c)

            if out!='':
                self.Ui.Result_text.setText(out)
            else:
                self.Ui.Result_text.setText('加密失败！')
        except Exception as e :
            self.Ui.Result_text.setText(str(e)) 
    def sifang_encrypt(self):
        self.dialog.close()
        try:
            text = (self.Ui.Source_text.toPlainText()).lower()
            key1 = self.WChild.Key1.text().upper()
            key2 = self.WChild.Key2.text().upper()
            matrix = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
            pla = "abcdefghijklmnoprstuvwxyz"
            key1 = '['+key1+"]"
            key2 = '['+key2+"]"
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
                first = self.find_index(data[0],pla_list)
                # 两个子母中第二个字母位置
                second = self.find_index(data[1],pla_list)
                return_cip = ""
                return_cip += matrix_list1[first[0]][second[1]]
                return_cip += matrix_list2[second[0]][first[1]]
                cip += return_cip
            if cip != '':
                self.Ui.Result_text.setText(cip)
            else:
                self.Ui.Result_text.setText('加密失败！')

        except Exception as  e:
            # print(str(e))
            pass

    def gcd(self,a, b):
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
            text = (self.Ui.Source_text.toPlainText())
            key1 = self.WChild.Key1.text()
            key2 = self.WChild.Key2.text()
            # print(text,key2,key1)
            try:
                if (0 == int(key1.isdigit()) or 0 == int(key2.isdigit())):
                    self.Ui.Result_text.setText('输入有误! 密钥为数字。')
                if (self.gcd(int(key1),26)!=1):
                    self.Ui.Result_text.setText('输入有误! key1和26必须互素。')
                    return 0
            except:
                self.Ui.Result_text.setText('输入有误!')

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
                self.Ui.Result_text.setText(ciphertext)
        except Exception as  e:
            self.Ui.Result_text.setText('加密失败!')
            # print(str(e))
            pass
    # 查询明文字母位置
    def find_index(self,x,pla_list):
        for i in range(len(pla_list)):
            for j in range(len(pla_list[i])):
                if pla_list[i][j] == x:
                    return i, j
    def zhalanEncrypto(self):
        self.dialog.close()
        plain = self.Ui.Source_text.toPlainText()
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
            self.Ui.Result_text.setText(ans)
        else:
            self.Ui.Result_text.setText('加密失败！')


    #decrypt
    def decrypt(self,decrypt_type):
        try:
            result_text=''
            # print(decrypt_type)
            text = self.Ui.Source_text.toPlainText()
            if text=='':
                self.Ui.Result_text.setText('请输入一个源字符串！')
                return 0
            if decrypt_type == 'Rot13':
                PAIRS= {
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
            elif decrypt_type == '凯撒密码':
                t = ""
                for c in text:
                    if 'a' <= c <= 'z':  # str是可以直接比较的
                        t += chr(ord('a') + ((ord(c) - ord('a')) -3) % 26)
                    elif 'A' <= c <= 'Z':
                        t += chr(ord('A') + ((ord(c) - ord('A')) - 3) % 26)
                    else:
                        t += c
                result_text=t
            elif decrypt_type == '栅栏密码':
                for n in range(2, text.__len__() - 1):
                    ans = ''
                    for i in range(n):
                        for j in range(int(text.__len__() / n + 0.5)):
                            try:
                                ans += text[j * n + i]
                            except:
                                pass
                    result_text+="分为%s栏，解密结果为:%s\n"%(n,ans)
            elif decrypt_type == '培根密码':
                return_str=''
                dicts = {'aabbb': 'H', 'aabba': 'G', 'baaab': 'R', 'baaaa': 'Q', 'bbaab': 'Z', 'bbaaa': 'Y', 'abbab': 'N',
                         'abbaa': 'M', 'babaa': 'U', 'babab': 'V', 'abaaa': 'I', 'abaab': 'J', 'aabab': 'F', 'aabaa': 'E',
                         'aaaaa': 'A', 'aaaab': 'B', 'baabb': 'T', 'baaba': 'S', 'aaaba': 'C', 'aaabb': 'D', 'abbbb': 'P',
                         'abbba': 'O', 'ababa': 'K', 'ababb': 'L', 'babba': 'W', 'babbb': 'X'}
                sums = len(text)
                j = 5  ##每5个为一组
                for i in range(int(sums / j)):
                    result = text[j * i:j * (i + 1)].lower()
                    return_str+=str(dicts[result],)
                result_text=return_str
            elif decrypt_type == '摩斯密码':
                dict = {'.-': 'A','-...': 'B','-.-.': 'C','-..': 'D',
                        '.': 'E','..-.': 'F','--.': 'G','....': 'H',
                        '..': 'I','.---': 'J','-.-': 'K','.-..': 'L',
                        '--': 'M','-.': 'N','---': 'O','.--.': 'P',
                        '--.-': 'Q','.-.': 'R','...': 'S','-': 'T',
                        '..-': 'U','...-': 'V', '.--': 'W','-..-': 'X',
                        '-.--': 'Y','--..': 'Z','.----': '1','..---': '2',
                        '...--': '3','....-': '4','.....': '5', '-....': '6',
                        '--...': '7', '---..': '8','----.': '9','-----': '0',
                        '..--..': '?','-..-.': '/', '-.--.-': '()','-....-': '-',
                        '.-.-.-': '.'
                        }
                msg = ''
                s= text.split(' ')
                for item in s:
                    if item!=''and item!=' ':
                     msg += (dict[item])
                result_text = msg
            elif decrypt_type == '移位密码':
                inputStr = text
                #
                result=''
                for j in range(26):
                    result_list = []
                    for i, num in zip(inputStr, range(len(inputStr))):
                        #print(i)
                        if i.islower:
                            caseS1 = string.ascii_lowercase * 2
                        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                            caseS1 = string.ascii_uppercase * 2
                        status = caseS1.find(i)
                        if status != -1:
                            result_list.append(caseS1[status + j])
                        else:
                            result_list.append(inputStr[num])
                    text2=("".join(result_list), "向右偏移了{}位".format(j))
                    result+= text2[0]+' '+text2[1]+'\n'
                result_text =result
            elif decrypt_type == '云影密码':
                other_letters = []
                for s in text:
                    if not ['0','1','2','4','8'].count(s):
                        other_letters.append(s)
                if other_letters:
                    result_text='加密字符串内只能包含0、1、2、4、8'
                else:
                    charList = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
                    ret = []
                    plaintext = [i for i in text.split('0')]
                    for i in plaintext:
                        tmp = 0
                        for j in range(len(i)):
                            tmp += int(i[j])
                        ret.append(charList[tmp - 1])
                    result_text= ''.join(ret)
            elif decrypt_type == '当铺密码':
                mapping_data ={'田': 0, '由': 1, '中': 2, '人': 3, '工': 4, '大': 5, '王': 6, '夫': 7, '井': 8, '羊': 9}
                result_text = ''.join(map(lambda x: str(mapping_data[x]), text))
            elif decrypt_type == '四方密码':
                self.WChild = Ui_KEY2()
                self.dialog = QtWidgets.QDialog(self)
                self.WChild.setupUi(self.dialog)
                self.dialog.show()
                self.WChild.enter.clicked.connect(self.sifang_decrypt)
                return 0
            elif decrypt_type == '仿射密码':
                self.WChild = Ui_KEY2()
                self.dialog = QtWidgets.QDialog(self)
                self.WChild.setupUi(self.dialog)
                self.dialog.show()
                self.WChild.enter.clicked.connect(self.fangshe_decrypt)
                return 0

            elif decrypt_type == '维吉尼亚密码':
                self.WChild = Ui_KEY1()
                self.dialog = QtWidgets.QDialog(self)
                self.WChild.setupUi(self.dialog)
                self.dialog.show()
                self.WChild.keyenter.clicked.connect(self.VigenereDecrypto)
                return 0
            elif decrypt_type=='埃特巴什码':
                str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                str2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
                result_text = ""
                for s in text:
                    if s != ' ':
                        result_text = result_text + str1[str2.index(s)]
                    else:
                        result_text = result_text + ' '
            if result_text!="":
                self.Ui.Result_text.setText(result_text)
            else:
                self.Ui.Result_text.setText('解密失败！')
        except Exception as e :
            self.Ui.Result_text.setText(str(e)) 
            # QMessageBox.critical(self,'Error',str(e))
            pass
            # print(str(e))
    def VigenereDecrypto(self):
        try:
            self.dialog.close()
            letter_list = string.ascii_uppercase
            letter_list2 = string.ascii_lowercase
            message = self.Ui.Source_text.toPlainText()
            key = self.WChild.key.text()
            if len(key)==0:
                self.Ui.Result_text.setText(str('请输入一个合法的key！')) 
                return 0
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
            if plaintext!='':
                self.Ui.Result_text.setText(plaintext)
            else:
                self.Ui.Result_text.setText('解密失败!')
        except Exception as e:
            self.Ui.Result_text.setText(str(e)) 
    def sifang_decrypt(self):
        self.dialog.close()
        try:
            # print(1)
            text = (self.Ui.Source_text.toPlainText()).upper()
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
                first = self.find_index1(letter[0],matrix_list1)

                # 两个子母中第二个字母位置
                second = self.find_index2(letter[1],matrix_list2)

                return_pla = ""
                return_pla += pla_list[first[0]][second[1]]
                return_pla += pla_list[second[0]][first[1]]
                result += return_pla
            if result != '':
                self.Ui.Result_text.setText(result)
            else:
                self.Ui.Result_text.setText('解密失败！')

        except Exception as e:
            # print(str(e))
            pass

    # 求逆元函数
    def GetInverse(self,a, m):
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
                    self.Ui.Result_text.setText('输入有误! 密钥为数字。')
                    return
                if (self.gcd(int(key1),26)!=1):
                    key1_list = []
                    result = ''
                    for i in range(0,int(key1)):
                        if self.gcd(i,26)==1:
                            key1_list.append(i)
                    for z in key1_list:
                        result+= 'key1:%s'%z+'   明文:'+self.fangshe_getdecrypt(int(z), int(key2))+'\n'
                    self.Ui.Result_text.setText('输入有误! key1和26必须互素。以下为爆破key1的结果\n'+result)
                    return 0
            except:
                self.Ui.Result_text.setText('输入有误!')
            else:
                self.Ui.Result_text.setText(self.fangshe_getdecrypt(int(key1),int(key2)))
        except Exception as e:
            self.Ui.Result_text.setText('解密失败。')
            # print(str(e))
            pass
    def fangshe_getdecrypt(self,key1,key2):
        try:
            text = (self.Ui.Source_text.toPlainText())
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
            return  plaintext
        except:
            return


    # 查询两个密文字母位置
    def find_index1(self,x,matrix_list1):
        for i in range(len(matrix_list1)):
            for j in range(len(matrix_list1[i])):
                if matrix_list1[i][j] == x:
                    return i, j

    def find_index2(self,y,matrix_list2):
        for k in range(len(matrix_list2)):
            for l in range(len(matrix_list2[k])):
                if matrix_list2[k][l] == y:
                    return k, l
    #Binary
    def Binary(self,Binary_type):
        try:
            result_text=''
            text = self.Ui.Source_text.toPlainText()
            if text == '':
                self.Ui.Result_text.setText('请输入一个源字符串！')
                return 0
            all_text = text.split(" ")
            all_result = ''
            for text in all_text:
                if text =="":
                    break
                if Binary_type == '2->8':
                    result = int(text, 2)
                    result_text = str(oct(result))
                elif Binary_type == '2->10':
                    result = int(text, 2)
                    result_text=str(result)
                elif Binary_type == '2->16':
                    result_text=str(hex(int(text,2)))
                elif Binary_type == '8->2':
                    result = int(text, 8)
                    result_text = str(bin(result))
                elif Binary_type == '8->10':
                    result = int(text, 8)
                    result_text = str(result)
                elif Binary_type == '8->16':
                    result = int(text, 8)
                    result_text=str(hex(result))
                elif Binary_type == '10->2':
                    s = int(text)
                    result_text = str(bin(s))
                elif Binary_type == '10->8':
                    s = int(text)
                    result_text = str(oct(s))
                elif Binary_type == '10->16':
                    s = int(text)
                    result_text =str(hex(s))
                elif Binary_type == '16->2':
                    result_text=str(bin(int(text,16)))
                elif Binary_type == '16->8':
                    result = int(text, 16)
                    result_text = str(oct(result))
                elif Binary_type == '16->10':
                    result = int(text, 16)
                    result_text = str(result)
                elif Binary_type == '自定义':
                    self.Binary_dialog = Ui_Binary()
                    self.dialog = QtWidgets.QDialog(self)
                    self.Binary_dialog.setupUi(self.dialog)
                    self.dialog.show()
                    self.Binary_dialog.enter.clicked.connect(self.Binary_conversion)
                    return 0
                all_result=all_result+result_text+' '
            all_result=str(all_result).replace('0o','').replace('0x','').replace('0b','')
            self.Ui.Result_text.setText(all_result)
        except Exception as e :
            self.Ui.Result_text.setText(str(e)) 
            pass
    def Binary_conversion(self):
        try:
            return_Data = ''
            self.dialog.close()
            if self.Binary_dialog.Source.text()!='' and self.Binary_dialog.result.text()!='':
                text = self.Ui.Source_text.toPlainText()
                # print(text)
                from_ = int(self.Binary_dialog.Source.text())
                to_ = int(self.Binary_dialog.result.text())
                #from_进制转换为十进制
                ten_num = sum([int(i) * from_ ** n for n, i in enumerate(text[::-1])])
                # print(ten_num)
                #十进制转换为to_进制
                a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']
                b = []
                while True:
                    s = ten_num // to_ # 商
                    y = ten_num % to_ # 余数
                    b = b + [y]
                    if s == 0:
                        break
                    ten_num = s
                b.reverse()
                for i in b:
                    return_Data+=str(a[i])
                self.Ui.Result_text.setText(return_Data)
        except Exception as e :
            pass
    def Copy_text(self,text):
        try:
            if  text=='Source':
                data = self.Ui.Source_text.toPlainText()
            if  text=='result':
                data = self.Ui.Result_text.toPlainText()
            # 访问剪切板，存入值
            wincld.OpenClipboard()
            wincld.EmptyClipboard()
            wincld.SetClipboardData(win32con.CF_UNICODETEXT, data)
            wincld.CloseClipboard()
        except Exception as e :
            pass
    def tihuan(self,text):
        try:
            if  text=='Source':
                data = self.Ui.Source_text.toPlainText()
                source_text = self.Ui.Source_tihuan_source.text()
                result_text = self.Ui.Source_tihuan_result.text()
                text = self.Ui.Source_text.toPlainText()
                text = text.replace(source_text, result_text)
                self.Ui.Source_text.setText(str(text))
            if  text=='result':
                data = self.Ui.Result_text.toPlainText()
                source_text = self.Ui.Result_tihuan_source.text()
                result_text = self.Ui.Result_tihuan_result.text()
                text = self.Ui.Result_text.toPlainText()
                text = text.replace(source_text, result_text)
                self.Ui.Result_text.setText(str(text))
        except Exception as e :
            pass
    def paste(self,text):
        try:
            wincld.OpenClipboard()
            data = wincld.GetClipboardData(win32con.CF_UNICODETEXT)
            wincld.CloseClipboard()
            if  text=='Source':
                # print(text)
                source_text = self.Ui.Source_text.toPlainText() #
                data=source_text+data
                self.Ui.Source_text.setText(data)
            if  text=='result':
                result_text = self.Ui.Result_text.toPlainText() #
                data=result_text+data
                self.Ui.Result_text.setText(data)
        except Exception as e :
            # print(str(e))
            pass
    # 关于
    def about(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about(self, "About",self.about_text)
    #作者
    def author(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about(self, "Author", self.author_text)
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
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    window.show()
    try:
        response = requests.get("https://qianxiao996.cn/ctf-tools/version.txt",timeout = 2)
        if (int(response.text.replace('.',''))>int(version.replace('.',''))):
            reply = QMessageBox.question(window,'软件更新', "检测到软件已发布新版本，是否前去下载?",QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                webbrowser.open('https://github.com/qianxiao996/CTF-Tools/releases')
            else:
                pass
    except:
        pass
    sys.exit(app.exec_())
