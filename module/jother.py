# python3
# Jother Encode
#
# a = Jother()
# b =a.toStr("abcd")
# c = a.toScript("abcd")

class Jother():
    def __init__(self):
        self.base = [
            "[]",
            "{}",
            "![]",
            "!![]",
            "~[]",
            "+{}",
            "{}[[]]"
        ]
        self.nums = [
            "+[]",
            "+!![]",
            "!![]+!![]",
            "!![]+!![]+!![]",
            "!![]+!![]+!![]+!![]",
            "!![]+!![]+!![]+!![]+!![]",
            "!![]+!![]+!![]+!![]+!![]+!![]",
            "!![]+!![]+!![]+!![]+!![]+!![]+!![]",
            "!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]",
            "!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]"
        ]

        self.base.append(self.q1(self.q3(self.nums[1]+self.q4(self.q1(self.base[3])+self.q2(self.nums[3])) +
                                         self.q3(self.nums[1])+self.q3(self.nums[0])+self.q3(self.nums[0])+self.q3(self.nums[0]))))
        self.chars = {
            "0": self.q1(self.nums[0]),
            "1": self.q1(self.nums[1]),
            "2": self.q1(self.nums[2]),
            "3": self.q1(self.nums[3]),
            "4": self.q1(self.nums[4]),
            "5": self.q1(self.nums[5]),
            "6": self.q1(self.nums[6]),
            "7": self.q1(self.nums[7]),
            "8": self.q1(self.nums[8]),
            "9": self.q1(self.nums[9]),
            "a": self.q1(self.base[2])+self.q2(self.nums[1]),
            "b": self.q1(self.base[1])+self.q2(self.nums[2]),
            "c": self.q1(self.base[1])+self.q2(self.nums[5]),
            "d": self.q1(self.base[6])+self.q2(self.nums[2]),
            "e": self.q1(self.base[3])+self.q2(self.nums[3]),
            "f": self.q1(self.base[2])+self.q2(self.nums[0]),
            "i": self.q1(self.base[6])+self.q2(self.nums[5]),
            "j": self.q1(self.base[1])+self.q2(self.nums[3]),
            "l": self.q1(self.base[2])+self.q2(self.nums[2]),
            "n": self.q1(self.base[6])+self.q2(self.nums[1]),
            "o": self.q1(self.base[1])+self.q2(self.nums[1]),
            "r": self.q1(self.base[3])+self.q2(self.nums[1]),
            "s": self.q1(self.base[2])+self.q2(self.nums[3]),
            "t": self.q1(self.base[3])+self.q2(self.nums[0]),
            "u": self.q1(self.base[6])+self.q2(self.nums[0]),
            "y": self.q1(self.base[7])+self.q2(self.nums[7]),
            "I": self.q1(self.base[7])+self.q2(self.nums[0]),
            "N": self.q1(self.base[5])+self.q2(self.nums[0]),
            "O": self.q1(self.base[1])+self.q2(self.nums[8]),
            " ": self.q1(self.base[1])+self.q2(self.nums[7]),
            "[": self.q1(self.base[1])+self.q2(self.nums[0]),
            "]": self.q1(self.base[1])+self.q2(self.nums[7]+self.q4(self.nums[7])),
            "-": self.q1(self.base[4])+self.q2(self.nums[0]),
            "+": self.q1(self.q3(self.nums[1]+self.q4(self.q1(self.base[3])+self.q2(self.nums[3]))+self.q3(self.nums[1])+self.q3(self.nums[0])+self.q3(self.nums[0])))+self.q2(self.nums[2])
        }
        self.f = "[]["+self.toStr("sort")+"]["+self.toStr("constructor")+"]"
        self.localstr = "[]+"+self.toScript("return location")
        self.chars["h"] = self.q5(self.localstr)+self.q2(self.nums[0])
        self.chars["p"] = self.q5(self.localstr)+self.q2(self.nums[3])
        self.chars[":"] = self.q5(self.localstr)+self.q2(self.nums[4])
        self.chars["/"] = self.q5(self.localstr)+self.q2(self.nums[6])
        self.rc_unescape = self.toScript("return unescape")
        self.rc_escape = self.toScript("return escape")
        self.chars["%"] = self.rc_escape + \
            "("+self.toStr("[")+")"+self.q2(self.nums[0])

    def q1(self, s):
        return "("+s+"+[])"

    def q2(self, s):
        return "["+s+"]"

    def q3(self, s):
        return "+("+s+"+[])"

    def q4(self, s):
        return "+"+s

    def q5(self, s):
        return "("+s+")"

    def toScript(self, script):
        return self.f+"("+self.toStr(script)+")()"

    def toUnescape(self, charCode):
        return self.rc_unescape + "(" + self.toStr("%" + self.toHex(charCode, 2)) + ")"

    def toHexs(self, charCode):
        return self.toStr("\\x" + self.toHex(charCode, 2))

    def toUnicode(self, charCode):
        return self.toStr("\\u" + self.toHex(charCode, 4))

    def toHex(self, num, d):
        hexs = num.self.toString(16)
        while(len(hexs) < d):
            hexs = "0{}".format(hexs)
        return hexs

    def toChar(self, char):
        charCode = ord(char)
        if self.chars[char] != '':
            return self.chars[char]
        if char == "\\" or char == "x":
            self.chars[char] = self.toUnescape(charCode)
            return self.chars[char]

        unis = self.toUnicode(charCode)
        if charCode < 128:
            unes = self.toUnescape(charCode)
            if len(unis) > len(unes):
                unis = unes
            hexs = self.toHexs(charCode)
            if len(unis) > len(hexs):
                unis = hexs
            self.chars[char] = unis
        return unis

    def toStr(self, str):
        s = ''
        for i in range(len(str)):
            if i == 0:
                s += ''
            else:
                s += "+"
            s += self.toChar(str[i])
        return s
		