# Python port of the Javascript function written by Yosuke HASEGAWA (@hasegawayosuke)
# http://utf-8.jp/public/jjencode.html
# result = (JJEncoder(cryptostr).encoded_text).encode()
# 
__author__ = 'nriva'

import re
from struct import unpack

class JJEncoder(object):

	def __init__(self, text, var_name = "$", palindrome = False):
		if text:
			self.encoded_text = self.__encode(var_name, text)

			if palindrome:
				self.encoded_text = re.split("[,;]$", self.encoded_text)[0]
				self.encoded_text = """\"\'\\\"+\'+\",""" + self.encoded_text + "".join(list(self.encoded_text)[::-1])

	def __encode(self, gv, text):
		r = ""
		n = None
		t = None
		b = [ "___", "__$", "_$_", "_$$", "$__", "$_$", "$$_", "$$$", "$___", "$__$", "$_$_", "$_$$", "$$__", "$$_$", "$$$_", "$$$$"]
		s = ""

		for i in range(len(text)):
			n = ord(text[i])
			if (n == 0x22 or n == 0x5c):
				 s += "\\\\\\" + chr(unpack("b", text[i])[0])
			elif ((0x21 <= n and n <= 0x2f) or (0x3A <= n and n <= 0x40) or ( 0x5b <= n and n <= 0x60 ) or ( 0x7b <= n and n <= 0x7f)):
				s += text[i]

			elif ((0x30 <= n and n <= 0x39) or (0x61 <= n and n <= 0x66)):
				if s:
					r += '"' + s + '"+'

				if n < 0x40:
					tmp_index = n - 0x30
				else:
					tmp_index = n - 0x57

				r += gv + "." + b[ tmp_index ] + "+"
				s = ""

			elif n == 0x6c: # 'l'
				if s:
					r += '"' + s + '"+'

				r += '(![]+"")[' + gv + '._$_]+'
				s = ""

			elif n == 0x6f: # 'o'
				if s:
					r += '"' + s + '"+'

				r += gv + "._$+"
				s = ""
			elif n == 0x74: # 'u'
				if s:
					r += '"' + s + '"+'

				r += gv + ".__+"
				s = ""
			elif n == 0x75: # 'u'
				if s:
					r += '"' + s + '"+'

				r += gv + "._+"
				s = ""
			elif n < 128:
				if s:
					r += '"' + s
				else:
					r += '"'

				r += '\\\\"+' + "".join([self.__f(gv, b, i) for i in [int(x) for x in re.findall("[0-7]", oct(n))[1:]]])
				s = ""
			else:
				if s:
					r += '"' + s
				else:
					r += '"'

				r += '\\\\"+' + gv + "._+" + "".join([self.__g(gv, b, i) for i in [int(x) for x in re.findall("[0-9a-f]", oct(n), re.I)[1:]]])
				s = ""

		if s:
			r += '"' + s + '"+'

		r = (gv + "=~[];" +
		gv + "={___:++" + gv +',$$$$:(![]+"")['+gv+"],__$:++"+gv+',$_$_:(![]+"")['+gv+"],_$_:++"+
		gv+',$_$$:({}+"")['+gv+"],$$_$:("+gv+"["+gv+"""]+"")["""+gv+"],_$$:++"+gv+',$$$_:(!""+"")['+
		gv+"],$__:++"+gv+",$_$:++"+gv+',$$__:({}+"")['+gv+"],$$_:++"+gv+",$$$:++"+gv+",$___:++"+gv+",$__$:++"+gv+"};"+
		gv+".$_="+
		"("+gv+".$_="+gv+'+"")['+gv+".$_$]+"+
		"("+gv+"._$="+gv+".$_["+gv+".__$])+"+
		"("+gv+".$$=("+gv+'.$+"")['+gv+".__$])+"+
		"((!"+gv+')+"")['+gv+"._$$]+"+
		"("+gv+".__="+gv+".$_["+gv+".$$_])+"+
		"("+gv+'.$=(!""+"")['+gv+".__$])+"+
		"("+gv+'._=(!""+"")['+gv+"._$_])+"+
		gv+".$_["+gv+".$_$]+"+
		gv+".__+"+
		gv+"._$+"+
		gv+".$;"+
		gv+".$$="+
		gv+".$+"+
		'(!""+"")['+gv+"._$$]+"+
		gv+".__+"+
		gv+"._+"+
		gv+".$+"+
		gv+".$$;"+
		gv+".$=("+gv+".___)["+gv+".$_]["+gv+".$_];"+
		gv+".$("+gv+".$("+gv+'.$$+"\\""+' + r + '"\\"")())();')

		return r

	def __f(self, a, b, c):
		return a + "." + b[c] + "+"

	def __g(self, a, b, c):
		return a + "." + b[int(c, 16)] + "+"