# coding=utf-8
import collections
import random
import re
import string

import base36
import base58
import base62
import base64
import base91
import html
import py3base92
import urllib.parse

import execjs
import js2py
from Crypto.Cipher import AES


class Class_Encrypt:

    def func_rot13(self, encode_type, source_text):
        d = {chr(i + c): chr((i + 13) % 26 + c) for i in range(26) for c in (65, 97)}
        result_text = ''.join([d.get(c, c) for c in source_text])
        return [1, result_text,"Rot13"]

    def func_kaisa(self, encode_type, source_text):

        t = ""
        for c in source_text:
            if 'a' <= c <= 'z':  # str是可以直接比较的
                t += chr(ord('a') + ((ord(c) - ord('a')) + 3) % 26)
            elif 'A' <= c <= 'Z':
                t += chr(ord('A') + ((ord(c) - ord('A')) + 3) % 26)
            else:
                t += c
        result_text = t
        return [1, result_text,"凯撒密码"]

    def func_peigen(self, encode_type, source_text):
        CODE_TABLE = {  # 培根字典
            'aaaaa': 'a', 'aaaab': 'b', 'aaaba': 'c', 'aaabb': 'd', 'aabaa': 'e', 'aabab': 'f', 'aabba': 'g',
            'aabbb': 'h', 'abaaa': 'i', 'abaab': 'j', 'ababa': 'k', 'ababb': 'l', 'abbaa': 'm', 'abbab': 'n',
            'abbba': 'o', 'abbbb': 'p', 'baaaa': 'q', 'baaab': 'r', 'baaba': 's', 'baabb': 't', 'babaa': 'u',
            'babab': 'v', 'babba': 'w', 'babbb': 'x', 'bbaaa': 'y', 'bbaab': 'z'
        }
        str = source_text.lower()
        listStr = ''
        for i in str:
            if i in CODE_TABLE.values():
                # 将键、值各化为一个列表，取出i在value的位置后根据下标找到对应的键
                listStr += list(CODE_TABLE.keys())[list(CODE_TABLE.values()).index(i)]
        result_text = listStr.upper()  # 大写输出
        return [1, result_text,"培根密码"]

    def func_mosi(self, encode_type, source_text):

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
        for char in source_text.upper():
            if char in CODE:
                if char == ' ':
                    pass
                else:
                    msg += (CODE[char.upper()] + ' ')
            else:
                return [0, '文本中含有不能识别的字符!',"摩斯密码"]
        result_text = msg

        return [1, result_text,"摩斯密码"]

    def func_yunying(self, encode_type, source_text):
        charList = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        cipher = [i for i in source_text.upper()]
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
        return [1, result_text,"云影密码"]

    def func_dangpu(self, encode_type, source_text):
        mapping_data = [['田'], ['由'], ['中'], ['人'], ['工'], ['大'], ['王'], ['夫'], ['井'], ['羊']]
        try:
            result = []
            for c in source_text:
                c_list = mapping_data[int(c)]
                c_index = random.randint(0, len(c_list) - 1)
                result.append(c_list[c_index])
            result_text = ''.join(result)
        except:
            return [0, '未找到该字符串对应的中文!',"当铺密码"]
        return [1, result_text,"当铺密码"]

    # def yufolunchan_v1(sellf, encode_type, source_text):
    #     BYTEMARK = ['冥', '奢', '梵', '呐', '俱', '哆', '怯', '諳', '罰', '侄', '缽', '皤']
    #     KEY = b'XDXDtudou@KeyFansClub^_^Encode!!'
    #     IV = b'Potato@Key@_@=_='
    #     padding = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    #     cryptor = AES.new(KEY, AES.MODE_CBC, IV)
    #     result = cryptor.encrypt(padding(source_text).encode("utf-8"))
    #     aes_result = base64.b64encode(result).decode("utf-8")
    #     print(aes_result)
    #     truth_table = [
    #         '东', '殺', '諦', '曰', '至', '住', '藥', '忧', '蒙', '迦', '焰', '度', '謹', '妙', '智', '皂',
    #         '药', '經', '牟', '麼', '在', '孝', '界', '诵', '婦', '弟', '蘇', '竟', '德', '粟', '路', '茶',
    #         '栗', '特', '孤', '排', '西', '经', '慈', '行', '游', '訶', '難', '六', '精', '未', '輸', '楞',
    #         '去', '寂', '盧', '过', '故', '金', '安', '羅', '參', '吼', '橋', '央', '即', '曳', '消', '閦',
    #         '倒', '造', '稳', '戒', '藐', '親', '數', '普', '中', '朋', '释', '闍', '解', '夢', '鄉', '五',
    #         '诸', '守', '刚', '彌', '名', '陰', '足', '劫', '帝', '清', '勒', '時', '伊', '求', '戏', '功',
    #         '月', '除', '便', '贤', '宗', '灯', '夫', '者', '毒', '敬', '憐', '室', '号', '信', '姪', '灭',
    #         '以', '通', '方', '遮', '穆', '亿', '百', '昼', '睦', '貧', '殊', '说', '積', '高', '利', '沙',
    #         '僧', '奉', '花', '遠', '他', '亦', '孕', '心', '資', '福', '璃', '毘', '矜', '夷', '惜', '顛',
    #         '藝', '文', '急', '恤', '令', '阿', '放', '涅', '和', '告', '老', '怖', '山', '尼', '舍', '孫',
    #         '濟', '琉', '雙', '进', '廣', '想', '施', '師', '礙', '多', '休', '逝', '印', '愛', '友', '薩',
    #         '先', '槃', '持', '提', '真', '乾', '幽', '此', '尊', '重', '究', '三', '兄', '北', '陵', '瑟',
    #         '树', '紛', '哈', '善', '捐', '须', '胜', '隸', '困', '依', '創', '陀', '修', '万', '捨', '族',
    #         '来', '死', '根', '實', '夜', '拔', '首', '虚', '量', '呼', '师', '耨', '祖', '豆', '下', '各',
    #         '寡', '息', '知', '于', '千', '醯', '殿', '定', '禮', '如', '廟', '王', '数', '宇', '众', '恐',
    #         '盡', '能', '七', '寫', '弥', '宝', '梭', '害', '生', '及', '开', '空', '教', '念', '凉', '护',
    #         '色', '命', '乖', '岚',
    #     ]
    #     alpha_dict = {
    #         '+': 0, '/': 4, '0': 8, '1': 12, '2': 16, '3': 20, '4': 24, '5': 28,
    #         '6': 32, '7': 36, '8': 40, '9': 44, 'A': 48, 'B': 52, 'C': 56, 'D': 60,
    #         'E': 64, 'F': 68, 'G': 72, 'H': 76, 'I': 80, 'J': 84, 'K': 88, 'L': 92,
    #         'M': 96, 'N': 100, 'O': 104, 'P': 108, 'Q': 112, 'R': 116, 'S': 120, 'T': 124,
    #         'U': 128, 'V': 132, 'W': 136, 'X': 140, 'Y': 144, 'Z': 148, 'a': 152, 'b': 156,
    #         'c': 160, 'd': 164, 'e': 168, 'f': 172, 'g': 176, 'h': 180, 'i': 184, 'j': 188,
    #         'k': 192, 'l': 196, 'm': 200, 'n': 204, 'o': 208, 'p': 212, 'q': 216, 'r': 220,
    #         's': 224, 't': 228, 'u': 232, 'v': 236, 'w': 240, 'x': 244, 'y': 248, 'z': 252,
    #         '=': 256,
    #     }
    #
    #     newstr = ''
    #     li = list()
    #     for i in range(len(aes_result)):
    #         li.append(alpha_dict[aes_result[i]])
    #     for i in range(len(li)):
    #         li[i] += (i % 4)
    #     for i in range(len(li)):
    #         newstr += truth_table[li[i]]
    #     return newstr
    #     return msg

    def func_yufolunchan_v2(sellf, encode_type, source_text, key):

        text = source_text.strip().lower()
        if len(key) < 1:
            key = "qianxiao996"
        f = open('./module/yufoluntan_main.js', 'r')
        jsf_code = f.read()
        js = execjs.get()
        # print(jsf_code)
        # print "Using Engine %s" % js.name
        jsf_int = js.compile(jsf_code)
        return_text = jsf_int.call("aes_encrypt", text, key)
        # foYue = {"啰": "e", "羯": "E", "婆": "t", "提": "T", "摩": "a", "埵": "A", "诃": "o", "迦": "O", "耶": "i", "吉": "I",
        #          "娑": "n",
        #          "佛": "N", "夜": "s", "驮": "S", "那": "h", "谨": "H", "悉": "r", "墀": "R", "阿": "d", "呼": "D", "萨": "l",
        #          "尼": "L",
        #          "陀": "c", "唵": "C", "唎": "u", "伊": "U", "卢": "m", "喝": "M", "帝": "w", "烁": "W", "醯": "f", "蒙": "F",
        #          "罚": "g",
        #          "沙": "G", "嚧": "y", "他": "Y", "南": "p", "豆": "P", "无": "b", "孕": "B", "菩": "v", "伽": "V", "怛": "k",
        #          "俱": "K",
        #          "哆": "j", "度": "J", "皤": "x", "阇": "X", "室": "q", "地": "Q", "利": "z", "遮": "Z", "穆": "0", "参": "1",
        #          "舍": "2",
        #          "苏": "3", "钵": "4", "曳": "5", "数": "6", "写": "7", "栗": "8", "楞": "9", "咩": "+", "输": "/", "漫": "=",
        #          "e": "啰",
        #          "E": "羯", "t": "婆", "T": "提", "a": "摩", "A": "埵", "o": "诃", "O": "迦", "i": "耶", "I": "吉", "n": "娑",
        #          "N": "佛",
        #          "s": "夜", "S": "驮", "h": "那", "H": "谨", "r": "悉", "R": "墀", "d": "阿", "D": "呼", "l": "萨", "L": "尼",
        #          "c": "陀",
        #          "C": "唵", "u": "唎", "U": "伊", "m": "卢", "M": "喝", "w": "帝", "W": "烁", "f": "醯", "F": "蒙", "g": "罚",
        #          "G": "沙",
        #          "y": "嚧", "Y": "他", "p": "南", "P": "豆", "b": "无", "B": "孕", "v": "菩", "V": "伽", "k": "怛", "K": "俱",
        #          "j": "哆",
        #          "J": "度", "x": "皤", "X": "阇", "q": "室", "Q": "地", "z": "利", "Z": "遮", "0": "穆", "1": "参", "2": "舍",
        #          "3": "苏",
        #          "4": "钵", "5": "曳", "6": "数", "7": "写", "8": "栗", "9": "楞", "+": "咩", "/": "输", "=": "漫"}
        CODE = {"e": "啰", "E": "羯", "t": "婆", "T": "提",
                "a": "摩", "A": "埵", "o": "诃", "O": "迦",
                "i": "耶", "I": "吉", "n": "娑", "N": "佛",
                "s": "夜", "S": "驮", "h": "那", "H": "谨",
                "r": "悉", "R": "墀", "d": "阿", "D": "呼",
                "l": "萨", "L": "尼", "c": "陀", "C": "唵",
                "u": "唎", "U": "伊", "m": "卢", "M": "喝",
                "w": "帝", "W": "烁", "f": "醯", "F": "蒙",
                "g": "罚", "G": "沙", "y": "嚧", "Y": "他", "p": "南",
                "P": "豆", "b": "无", "B": "孕", "v": "菩",
                "V": "伽", "k": "怛", "K": "俱", "j": "哆",
                "J": "度", "x": "皤", "X": "阇", "q": "室",
                "Q": "地", "z": "利", "Z": "遮", "0": "穆",
                "1": "参", "2": "舍", "3": "苏", "4": "钵",
                "5": "曳", "6": "数", "7": "写", "8": "栗",
                "9": "楞", "+": "咩", "/": "输", "=": "漫",
                }
        msg = ''
        for char in return_text:
            if char in CODE:
                if char == ' ':
                    pass
                else:
                    msg += (CODE[char])
            else:
                return [0, '文本中含有不能识别的字符!',"与佛论禅2.0"]
        # result_text = msg
        # print(msg)
        return [1,"佛又曰：" + msg,"与佛论禅2.0"]

    def func_atbash(self, encode_type, source_text):
        str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        str2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
        result_text = ""
        for s in source_text:
            if s in str1:
                if s != ' ':
                    result_text = result_text + str2[str1.index(s)]
                else:
                    result_text = result_text + ' '
            else:
                return [0, "埃特巴什码只能对英文字母加密!","Atbash密码"]
        return [1, result_text,"Atbash密码"]

    def func_zhalan_w(self, encode_type, source_text, n):
        n = int(n)
        '''加密'''
        array = self.generate_w(source_text, n)
        msg = []
        for row in range(n):  # 将每行的字符连起来
            for col in range(len(source_text)):
                if array[row][col] != '.':
                    msg.append(array[row][col])
        return [1, str(''.join(msg)),"栅栏密码(W型)"]

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

    def func_vigenere(self, encode_type, source_text, key):
        try:
            text = source_text.lower()
            ptLen = len(text)
            keyLen = len(key)
            if keyLen == 0:
                return [0, '请输入一个合法的key!',"维吉尼亚密码"]
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
                return [1, out,"维吉尼亚密码"]

            else:
                return [0, '加密失败!',"维吉尼亚密码"]
        except Exception as e:
            return [0,str(e),"维吉尼亚密码"]

    def func_sifang(self, encode_type, source_text, key1, key2):
        try:
            text = source_text.lower()
            key1 = key1.upper()
            key2 = key2.upper()
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
                return [1, cip,"四方密码"]
            else:
                return [0, '加密失败!',"四方密码"]
        except Exception as  e:
            return [0, str(e),"四方密码"]

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

    def func_fangshe(self, encode_type, source_text, key1, key2):
        try:
            letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 字母表
            text = (source_text.strip())
            # print(text,key2,key1)
            try:
                if (0 == int(key1.isdigit()) or 0 == int(key2.isdigit())):
                    return [0, '输入有误! 密钥为数字!',"仿射密码"]
                if (self.gcd(int(key1), 26) != 1):
                    return [0, '输入有误! key1和26必须互素！',"仿射密码"]
            except:
                return [0, '输入有误!',"仿射密码"]
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
                return [1, ciphertext,"仿射密码"]
        except Exception as  e:
            return [0, str(e),"仿射密码"]

    # 查询明文字母位置
    def find_index(self, x, pla_list):
        for i in range(len(pla_list)):
            for j in range(len(pla_list[i])):
                if pla_list[i][j] == x:
                    return i, j

    def func_zhalan(self, encode_type, source_text, key):
        try:
            n = int(key)
            ans = ''
            for i in range(n):
                for j in range(int(source_text.__len__() / n + 0.5)):
                    try:
                        ans += source_text[j * n + i]
                    except:
                        pass
        except:
            return [0, '请输入正确的分组!',"栅栏密码"]
        if ans != '':
            return [1, ans,"栅栏密码"]
        else:
            return [0, '加密失败!',"栅栏密码"]
    def func_Polybius(self, encode_type, source_text):
        Polybius_dic = {
            'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
            'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 'K': '25',
            'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
            'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
            'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
        }
        result = ''
        for i in source_text:
            result += Polybius_dic.get(i.upper())
        return [1, result,"棋盘密码(ADFGX)"]

    def func_a1z26(self, encode_type, source_text):
        str1 = string.ascii_lowercase
        s = ""
        for i in source_text.lower():
            s += "-{}".format(str1.index(i) + 1)
        result = s[1:]
        return [1, result,"A1z26密码"]
