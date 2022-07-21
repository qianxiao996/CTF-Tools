# coding=utf-8
import binascii
import random
import Crypto.Util.Counter

import Crypto
import base64

from Crypto.Cipher import AES

class Class_Aes:

    def buqi_key(self,aes_type,aes_key,aes_zifuji):

        if aes_type == 'AES-128':
            length = 16
        elif aes_type == 'AES-192':
            length = 24
        elif aes_type == 'AES-256':
            length = 32
        else:
            length = 16
        if len(aes_key)>=length:
            return aes_key[:length].encode(),length
        else:

            aes_key = self.aes_buqi_(aes_key.encode(aes_zifuji), length, 'ZeroPadding', 'utf-8')
            return aes_key,length

    def encrypt(self,aes_type,aes_mode, aes_zifuji, aes_tianchong, aes_iv,aes_encode,aes_key,aes_m_text):
        if not aes_key:
            return ['error','AES密钥不能为空!']
        else:
            aes_key,aes_length= self.buqi_key(aes_type,aes_key,aes_zifuji)
            if aes_mode not in ["ECB"]:
                if len(aes_iv) != 16:
                    # 32, 48, or 64
                    return ['error', 'AES偏移长度必须为16位!']
                if not aes_iv:
                    return ['error', '偏移不能为空!']
                else:
                    aes_iv = aes_iv.encode(aes_zifuji)
        if not aes_m_text:
            return ['', '请输入明文!']
        else:
            aes_m_text = self.aes_buqi_(aes_m_text.encode(aes_zifuji), 16, aes_tianchong, aes_zifuji)
        if aes_mode == "CBC":
            cryptor = AES.new(aes_key, AES.MODE_CBC, aes_iv)
        elif aes_mode == "ECB":
            try:
                cryptor = AES.new(aes_key, AES.MODE_ECB)
            except Exception as e:
                print(str(e))
        elif aes_mode == "CFB":
            cryptor = AES.new(aes_key, AES.MODE_CFB, aes_iv)
        elif aes_mode == "CTR":
            ctr = Crypto.Util.Counter.new(128, initial_value=int(binascii.hexlify(aes_iv), 16))
            cryptor = AES.new(aes_key, AES.MODE_CTR, counter=ctr)
        elif aes_mode == "OFB":
            cryptor = AES.new(aes_key, AES.MODE_OFB, aes_iv)
        else:
            return ['error', '加密模式设置错误!']
        return_text = cryptor.encrypt(aes_m_text)
        if aes_encode == 'Base64':
            return_text = str(base64.encodebytes(return_text), encoding=aes_zifuji).strip()

        elif aes_encode == 'Hex':
            return_text = str(binascii.b2a_hex(return_text), encoding=aes_zifuji).strip()
        # print(return_text)
        return ['success', return_text]

    def decrypt(self,aes_type,aes_mode, aes_zifuji, aes_iv,aes_encode,aes_key,aes_m_text):
        if not aes_key:
            return ['error','AES密钥不能为空!']
        else:
            if len(aes_key)<16:
                aes_key = self.aes_buqi_(aes_key.encode(aes_zifuji), 16, 'ZeroPadding', 'utf-8')
            elif 16<len(aes_key)<24:
                aes_key = self.aes_buqi_(aes_key.encode(aes_zifuji), 24, 'ZeroPadding', 'utf-8')
            elif 24<len(aes_key)<32:
                aes_key = self.aes_buqi_(aes_key.encode(aes_zifuji), 32, 'ZeroPadding', 'utf-8')
            elif len(aes_key) > 32:
                return ['error', 'AES密钥最长32位!']
                # return ['error', 'AES密钥应为16、24、32位!']
            else:
                aes_key = aes_key.encode(aes_zifuji)
            if aes_mode not in ["ECB"]:
                if len(aes_iv) != 16:
                    return ['error', 'AES偏移长度必须为16位!']
                if not aes_iv:
                    return ['error', '偏移不能为空!']
                else:
                    aes_iv = aes_iv.encode(aes_zifuji)

        if not aes_m_text:
            return ['error', '请输入密文!']
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
            return ['error', '加密模式设置错误!']
        try:
            return_text = cryptor.decrypt(aes_m_text)
            ret = self._unpad(return_text)
            return_text = ret.decode(aes_zifuji)
            return ['success', return_text]
        except:
            return ['error', '解密失败!']

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]
    def aes_buqi_(self, text, length, aes_tianchong, aes_zifuji):
        if aes_tianchong == "ZeroPadding":
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
        elif aes_tianchong == "Pkcs7":
            # bs = 16
            bs  = length
            # length = len(text)
            # bytes_length = len(text)
            # padding_size = length if (bytes_length == length) else bytes_length
            padding_size = len(text)
            padding = bs - padding_size % bs
            padding_text = chr(padding) * padding
            # print(text+ padding_text.encode(aes_zifuji))
            return (text + padding_text.encode(aes_zifuji))
        elif aes_tianchong == "Iso10126":
            # bs = 16
            bs= length
            padding_size = len(text)
            padding = bs - padding_size % bs
            # * padding-1
            qian_Str = ''
            for i in range(0, padding - 1):
                qian_Str += chr(random.randint(0, 9))
            padding_text = qian_Str + chr(padding)
            return (text + padding_text.encode(aes_zifuji))
        elif aes_tianchong == "AnsiX923":
            # bs = 16
            bs= length
            tianchong_str = '\0'
            padding_size = len(text)
            padding = bs - padding_size % bs
            text = text + (tianchong_str * (padding - 1) + chr(padding)).encode(aes_zifuji)
            return text
        elif aes_tianchong == "No Padding":
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
