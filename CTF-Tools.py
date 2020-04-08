import html,base64,sys,string,os,urllib.parse,random
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import win32con,json
import win32clipboard as wincld
from GUI.main import Ui_MainWindow
from GUI.sub import Ui_Form
from GUI.data import Ui_data
from GUI.Binary import Ui_Binary
import frozen_dir
SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)
class MainWindows(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindows,self).__init__(parent)
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.setFixedSize(self.width(), self.height()) ##设置宽高不可变
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
        #encrypt
        self.Ui.actionRot13_encrypt.triggered.connect(lambda:self.encrypt(self.Ui.actionRot13_encrypt.text()))
        self.Ui.action_kaisa_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_kaisa_encrypt.text()))
        self.Ui.action_zhalan_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_zhalan_encrypt.text()))
        self.Ui.action_peigen_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_peigen_encrypt.text()))
        self.Ui.action_mosi_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_mosi_encrypt.text()))
        self.Ui.action_yunying_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_yunying_encrypt.text()))
        self.Ui.action_dangpu_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_dangpu_encrypt.text()))
        self.Ui.action_weinijiya_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_weinijiya_encrypt.text()))
        self.Ui.action_Atbash_encrypt.triggered.connect(lambda: self.encrypt(self.Ui.action_Atbash_encrypt.text()))

        #decrypt
        self.Ui.actionRot13_decrypt.triggered.connect(lambda:self.decrypt(self.Ui.actionRot13_decrypt.text()))
        self.Ui.action_kaisa_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_kaisa_decrypt.text()))
        self.Ui.action_zhalan_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_zhalan_decrypt.text()))
        self.Ui.action_peihen_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_peihen_decrypt.text()))
        self.Ui.action_mosi_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_mosi_decrypt.text()))
        self.Ui.action_yiwei_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_yiwei_decrypt.text()))
        self.Ui.action_yunxing_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_yunxing_decrypt.text()))
        self.Ui.action_dangpu_decry.triggered.connect(lambda: self.decrypt(self.Ui.action_dangpu_decry.text()))
        self.Ui.action_weinijiya_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_weinijiya_decrypt.text()))
        self.Ui.action_Atbash_decrypt.triggered.connect(lambda: self.decrypt(self.Ui.action_Atbash_decrypt.text()))

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
        self.readfile()
        #其他编码
        self.Ui.actionAAencode.triggered.connect(lambda:self.show_json('AAencode'))
        self.Ui.actionXXencode.triggered.connect(lambda:self.show_json('XXencode'))
        self.Ui.actionJJencode.triggered.connect(lambda:self.show_json('JJencode'))
        self.Ui.actionUUencode.triggered.connect(lambda:self.show_json('UUencode'))
        self.Ui.action_qiaoji.triggered.connect(lambda:self.show_json('敲击码'))
        self.Ui.actionJSfuck.triggered.connect(lambda:self.show_json('JSfuck'))
        self.Ui.actionBrainfuck_Ook.triggered.connect(lambda:self.show_json('Brainfuck/Ook!'))
        self.Ui.action_zhujuan.triggered.connect(lambda:self.show_json('猪圈密码'))
        self.Ui.actionOthers.triggered.connect(lambda:self.show_json('在线网站'))

    def show_json(self,type):
        self.data_form = Ui_data()
        self.dialog = QtWidgets.QDialog(self)
        self.data_form.setupUi(self.dialog)
        self.data_form.textEdit.setText(json_data[type])
        self.data_form.textEdit.moveCursor(QTextCursor.Start)
        self.data_form.textEdit.moveCursor(QtGui.QTextCursor.End, QTextCursor.MoveAnchor)  # 光标移动到最后
        self.dialog.show()
    def readfile(self):
        try:
            global json_data
            f=open('data.json','r',encoding='utf-8')
            json_data=json.load(f)
            # print(json_data)
            f.close()
        except Exception as e :
            QMessageBox.critical(self,'Error',str(e))

    #编码
    def encode(self,encode_type):
        try:
            result_text=''
            # print(encode_type)
            text = self.Ui.Source_text.toPlainText()
            if text=='':
                return 0
            if encode_type=='URL-UTF8':
                text = text.encode('utf-8')
                result_text = urllib.parse.quote(text)
            if encode_type == 'URL-GB2312':
                text = text.encode('gb2312')
                result_text = urllib.parse.quote(text)
            if encode_type=='Unicode':
                text = text.encode('unicode_escape')
                result_text = str(text, encoding='utf-8')
            if encode_type=='Escape(%U)':
                text = text.encode('unicode_escape')
                result_text = str(text, encoding='utf-8').replace('\\u', '%u')
            if encode_type=='HtmlEncode':
                result_text = html.escape(text)
            if encode_type=='ASCII':
                result = ''
                for i in text:
                    result = str(result) + str(ord(str(i))) + ' '
                result_text=str(result)[:-1]
            if encode_type=='Base16':
                text = base64.b16encode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            if encode_type=='Base32':
                text = base64.b32encode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            if encode_type=='Base64':
                text = base64.b64encode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            if encode_type=='Str-Hex':
                result = ''
                for i in text:
                    single = str(hex(ord(str(i))))
                    result = result + single
                result_text='0x' + (str(result)).replace('0x', '')
            if encode_type=='Shellcode':
                result = ''
                for i in text:
                    single = str(hex(ord(str(i))))
                    result = result + single
                result_text=(str(result)).replace('0x', '\\x')
            if encode_type=='Qwerty':
                str1 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
                str2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                result_text = ""
                for s in text:
                    if s !=' ':
                        result_text = result_text + str1[str2.index(s)]
                    else:
                        result_text = result_text+' '
            self.Ui.Result_text.setText(str(result_text))
        except Exception as e :
            pass
    #解码
    def decode(self,decode_type):
        try:
            result_text=''
            # print(decode_type)
            text = self.Ui.Source_text.toPlainText()
            if text=='':
                return 0
            if decode_type=='URL-UTF8':
                result_text = str(urllib.parse.unquote(text))
            if decode_type == 'URL-GB2312':
                result_text = str(urllib.parse.unquote(text, 'gb2312'))
            if decode_type=='Unicode':
                result_text = bytes(text, encoding="utf8").decode('unicode_escape')
            if decode_type=='Escape(%U)':
                text = text.replace('%u', '\\u').replace('%U', '\\u')
                result_text = bytes(text, encoding="utf8").decode('unicode_escape')
            if decode_type=='HtmlEncode':
                result_text = html.unescape(text)
            if decode_type=='ASCII':
                if ':' in text:
                    text = text.split(":")
                if ' ' in text:
                    text = text.split(" ")
                if ';' in text:
                    text = text.split(";")
                if ',' in text:
                    text = text.split(",")
                result = ''
                for i in text:
                    if i != '':
                        # print(chr(int(i)))
                        result = result + chr(int(i))
                result_text =result
            if decode_type=='Base16':
                text = base64.b16decode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            if decode_type=='Base32':
                text = base64.b32decode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            if decode_type=='Base64':
                text = base64.b64decode(text.encode("utf-8"))
                result_text=str(text, encoding='utf-8')
            if decode_type=='Hex-Str':
                text = text.replace('0x', '').replace('0X', '')
                result_text = str(bytes.fromhex(text), encoding="utf-8")
            if decode_type=='Shellcode':
                result = ''
                text = text.split('\\x')
                for i in text:
                    single = str(bytes.fromhex(i), encoding="utf-8")
                    result = result + single
                result_text =str(result)
            if decode_type=='Qwerty':
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
            self.Ui.Result_text.setText(str(result_text))
        except Exception as e :
            # print(e)
            pass
    #encrypt
    def encrypt(self,encrypt_type):
        try:
            result_text=''
            # print(encrypt_type)
            text = self.Ui.Source_text.toPlainText()
            if text=='':
                return 0
            if encrypt_type=='Rot13':
                d = {chr(i + c): chr((i + 13) % 26 + c) for i in range(26) for c in (65, 97)}
                result_text = ''.join([d.get(c, c) for c in text])
            if encrypt_type=='凯撒密码':
                t = ""
                for c in text:
                    if 'a' <= c <= 'z':  # str是可以直接比较的
                        t += chr(ord('a') + ((ord(c) - ord('a')) + 3) % 26)
                    elif 'A' <= c <= 'Z':
                        t += chr(ord('A') + ((ord(c) - ord('A')) + 3) % 26)
                    else:
                        t += c
                result_text=t
            if encrypt_type=='栅栏密码':
                self.WChild_zhalan = Ui_Form()
                self.dialog = QtWidgets.QDialog(self)
                self.WChild_zhalan.setupUi(self.dialog)
                self.dialog.show()
                self.WChild_zhalan.keyenter.clicked.connect(self.zhalanEncrypto)
            if encrypt_type=='培根密码':
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
            if encrypt_type=='摩斯密码':
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
                    if char == ' ':
                        pass
                    else:
                        msg+=(CODE[char.upper()] + ' ')
                result_text =msg
            if encrypt_type=='云影密码':
                charList = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
                cipher = [i for i in text]
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
            if encrypt_type == '当铺密码':
                try:
                    mapping_data = [[], [], [], [], [], [], [], [], [], []]
                    with open('dangpu.data', 'r', encoding='UTF-8') as f:
                        for line in f:
                            ss = line.strip('\n').split(' ')
                            mapping_data[int(ss[1]) - 1].append(ss[0])
                except Exception as  e:
                    QMessageBox.critical(self, 'Error', 'dangpu.data加载错误！')
                result = []
                for c in text:
                    c_list = mapping_data[int(c)]
                    c_index = random.randint(0, len(c_list) - 1)
                    result.append(c_list[c_index])
                result_text = ''.join(result)
            if encrypt_type=='维吉尼亚密码':
                self.WChild = Ui_Form()
                self.dialog = QtWidgets.QDialog(self)
                self.WChild.setupUi(self.dialog)
                self.dialog.show()
                self.WChild.keyenter.clicked.connect(self.VigenereEncrypto)
            if encrypt_type=='埃特巴什码':
                str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                str2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
                result_text = ""
                for s in text:
                    if s != ' ':
                        result_text = result_text + str2[str1.index(s)]
                    else:
                        result_text = result_text + ' '
            self.Ui.Result_text.setText(result_text)
        except Exception as e :
            # QMessageBox.critical(self,'Error',str(e))
            print(str(e))
            pass
    def VigenereEncrypto(self):
        self.dialog.close()
        text = self.Ui.Source_text.toPlainText()
        key = self.WChild.key.text()
        ptLen = len(text)
        keyLen =  len(key)
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
        self.Ui.Result_text.setText(out)
    def zhalanEncrypto(self):
        self.dialog.close()
        plain = self.Ui.Source_text.toPlainText()
        n = int(self.WChild_zhalan.key.text())
        ans = ''
        for i in range(n):
            for j in range(int(plain.__len__() / n + 0.5)):
                try:
                    ans += plain[j * n + i]
                except:
                    pass
        self.Ui.Result_text.setText(ans)

    #decrypt
    def decrypt(self,decrypt_type):
        try:
            result_text=''
            # print(decrypt_type)
            text = self.Ui.Source_text.toPlainText()
            if text=='':
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
            if decrypt_type == '凯撒密码':
                t = ""
                for c in text:
                    if 'a' <= c <= 'z':  # str是可以直接比较的
                        t += chr(ord('a') + ((ord(c) - ord('a')) -3) % 26)
                    elif 'A' <= c <= 'Z':
                        t += chr(ord('A') + ((ord(c) - ord('A')) - 3) % 26)
                    else:
                        t += c
                result_text=t
            if decrypt_type == '栅栏密码':
                for n in range(2, text.__len__() - 1):
                    ans = ''
                    for i in range(n):
                        for j in range(int(text.__len__() / n + 0.5)):
                            try:
                                ans += text[j * n + i]
                            except:
                                pass
                    result_text+="分为%s栏，解密结果为:%s\n"%(n,ans)
            if decrypt_type == '培根密码':
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
            if decrypt_type == '摩斯密码':
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
            if decrypt_type == '移位密码':
                inputStr = text.lower()
                caseS1 = string.ascii_lowercase * 2
                # caseS1 = string.ascii_uppercase * 2
                result=''
                for j in range(26):
                    result_list = []
                    for i, num in zip(inputStr, range(len(inputStr))):
                        status = caseS1.find(i)
                        if status != -1:
                            result_list.append(caseS1[status + j])
                        else:
                            result_list.append(inputStr[num])
                    text2=("".join(result_list), "向右偏移了{}位".format(j))

                    result+= text2[0]+' '+text2[1]+'\n'
                result_text =result
            if decrypt_type == '云影密码':
                charList = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
                ret = []
                plaintext = [i for i in text.split('0')]
                for i in plaintext:
                    tmp = 0
                    for j in range(len(i)):
                        tmp += int(i[j])
                    ret.append(charList[tmp - 1])
                result_text= ''.join(ret)
            if decrypt_type == '当铺密码':
                try:
                    mapping_data = {}
                    with open('dangpu.data', 'r', encoding='UTF-8') as f:
                        for line in f:
                            ss = line.strip('\n').split(' ')
                            mapping_data[ss[0]] = int(ss[1])
                except Exception as  e:
                    QMessageBox.critical(self, 'Error', 'dangpu.data加载错误！')
                result_text = ''.join(map(lambda x: str(mapping_data[x] - 1), text))
            if decrypt_type == '维吉尼亚密码':
                self.WChild = Ui_Form()
                self.dialog = QtWidgets.QDialog(self)
                self.WChild.setupUi(self.dialog)
                self.dialog.show()
                self.WChild.keyenter.clicked.connect(self.VigenereDecrypto)
            if decrypt_type=='埃特巴什码':
                str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                str2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
                result_text = ""
                for s in text:
                    if s != ' ':
                        result_text = result_text + str1[str2.index(s)]
                    else:
                        result_text = result_text + ' '
            self.Ui.Result_text.setText(result_text)
        except Exception as e :
            # QMessageBox.critical(self,'Error',str(e))
            pass
            # print(str(e))
    def VigenereDecrypto(self):
        self.dialog.close()
        letter_list = string.ascii_uppercase
        letter_list2 = string.ascii_lowercase
        message = self.Ui.Source_text.toPlainText()
        key = self.WChild.key.text()
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
        self.Ui.Result_text.setText(plaintext)
    #Binary
    def Binary(self,Binary_type):
        try:
            result_text=''
            # print(Binary_type)
            text = self.Ui.Source_text.toPlainText()
            if text=='':
                return 0
            if Binary_type == '2->8':
                result = int(text, 2)
                result_text = str(oct(result))
            if Binary_type == '2->10':
                result = int(text, 2)
                result_text=str(result)
            if Binary_type == '2->16':
                result_text=str(hex(int(text,2)))
            if Binary_type == '8->2':
                result = int(text, 8)
                result_text = str(bin(result))
            if Binary_type == '8->10':
                result = int(text, 8)
                result_text = str(result)
            if Binary_type == '8->16':
                result = int(text, 8)
                result_text=str(hex(result))
            if Binary_type == '10->2':
                s = int(text)
                result_text = str(bin(s))
            if Binary_type == '10->8':
                s = int(text)
                result_text = str(oct(s))
            if Binary_type == '10->16':
                s = int(text)
                result_text =str(hex(s))
            if Binary_type == '16->2':
                result_text=str(bin(int(text,16)))
            if Binary_type == '16->8':
                result = int(text, 16)
                result_text = str(oct(result))
            if Binary_type == '16->10':
                result = int(text, 16)
                result_text = str(result)
            if Binary_type == '自定义':
                self.Binary_dialog = Ui_Binary()
                self.dialog = QtWidgets.QDialog(self)
                self.Binary_dialog.setupUi(self.dialog)
                self.dialog.show()
                self.Binary_dialog.enter.clicked.connect(self.Binary_conversion)
            result_text=str(result_text).replace('0o','').replace('0x','').replace('0b','')
            self.Ui.Result_text.setText(result_text)
        except Exception as e :
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
        box.about(self, "About",
                  "\t\t\tAbout\n       此程序为CTF密码学辅助工具，可进行常见的编码、解码、加密、解密操作，请勿非法使用！\n\t\t\tPowered by qianxiao996")
    #作者
    def author(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about(self, "Author", "作者邮箱：qianxiao996@126.com\n作者主页：https://blog.qianxiao996.cn\nGithub：https://github.com/qianxiao996")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec_())
