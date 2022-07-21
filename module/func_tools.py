# coding=utf-8
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


class Class_Tools:


    def func_str_chaifen(self,encode_type,source_text,length):
        try:
            changdu = int(length)
        except:
            return [0, '请输入一个数字!',"字符拆分"]

        if changdu > len(source_text):
            return [0, '分割长度大于字符串长度!',"字符拆分"]
        else:
            text = [source_text[i:i + changdu] for i in range(0, len(source_text), changdu)]
            # text = re.findall(r'.{'+str(changdu)+'}', text)
            return_text = ' '.join(text)
        return [1, str(return_text),"字符拆分"]
    def func_str_split(self,encode_type,source_text,split_str):
        text = source_text.split(split_str)
        return_text = ' '.join(text)
        return [1, str(return_text.strip()),"字符分割"]

    def func_str_tongji(self,encode_type,source_text):
        s = ''
        l = len(source_text)
        for x in range(0, l):
            if not source_text[x] in s:
                s += source_text[x]
        result = {d: 0 for d in s}
        for d in source_text:
            for alpha in s:
                if d == alpha:
                    result[alpha] = result[alpha] + 1

        result1 = sorted(result.items(), key=lambda x: x[1], reverse=True)
        return_text = '大->小:\n字符：'
        for x in result1:
            return_text += str(x[0])
        return_text+='\n次数：'
        for x in result1:
            return_text += str(x[1])
        return_text += '\n\n小->大:\n字符：'
        result2 = sorted(result.items(), key=lambda x: x[1], reverse=False)
        for x in result2:
            return_text += str(x[0])
        result2 = sorted(result.items(), key=lambda x: x[1], reverse=False)
        return_text+='\n次数：'
        for x in result2:
            return_text += str(x[1])
        return_text += '\n\n'
        for x in result1:
            return_text += x[0] + ":" + str(x[1]) + '\n'
        return [1, return_text,"字符统计"]

    def func_str_re(self,encode_type,source_text):
        text = source_text.strip()
        return [1, str(text[::-1]),"字符替换"]
