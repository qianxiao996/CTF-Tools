# coding=utf-8
import re

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
from  module.jother import  Jother

class Class_Decode:
    def func_url(self,encode_type,source_text):
        try:
            result_text = str(urllib.parse.unquote(source_text, encode_type))
        except Exception as  e:
            return [0, '解码失败',"Url编码"]
        return [1, result_text.strip(),'Url编码']

    def func_unicode(self,encode_type,source_text):
        try:
            result_text = bytes(source_text, encoding=encode_type).decode('unicode_escape')
        except Exception as  e:
            return [0, '解码失败',"Unicode编码"]
        return [1, result_text.strip(),"Unicode编码"]

    def func_escape_u(self,encode_type,source_text):
        try:
            text = source_text.replace('%u', '\\u').replace('%U', '\\u')
            result_text = bytes(text, encoding=encode_type).decode('unicode_escape')
        except Exception as  e:
            return [0, '解码失败',"Escape_u编码"]
        return [1, result_text.strip(),"Escape_u编码"]
    def func_html(self,encode_type,source_text):
        try:
            result_text = html.unescape(source_text)
        except Exception as  e:
            return [0, '解码失败',"html编码"]
        return [1, result_text.strip(),"html编码"]

    # 得到分割数据 返回list
    def get_split_data(self, text):
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
        return text
    def func_ASCII_2(self,encode_type,source_text):
        try:
            text = self.get_split_data(source_text)
            # print(text)
            result = ''
            for i in text:
                if i != '':
                    # print(i)
                    # print(chr(int(i)))
                    result = result + chr(int(i, 2))
        except Exception as  e:
            # print(str(e))
            return [0, '解码失败',"ASCII(2进制)"]
        return [1, result,"ASCII(2进制)"]

    def func_ASCII_8(self,encode_type,source_text):
        try:
            text = self.get_split_data(source_text)
            # print(text)
            result = ''
            for i in text:
                if i != '':
                    # print(i)
                    # print(chr(int(i)))
                    result = result + chr(int(i, 8))
        except Exception as  e:
            return [0, '解码失败',"ASCII(8进制)"]
        return [1, result,"ASCII(8进制)"]

    def func_ASCII_10(self,encode_type,source_text):
        try:
            text = self.get_split_data(source_text)
            # print(text)
            result = ''
            for i in text:
                if i != '':
                    # print(i)
                    # print(chr(int(i)))
                    result = result + chr(int(i))
        except Exception as  e:
            return [0, '解码失败',"ASCII(10进制)"]

        return [0, result,"ASCII(10进制)"]

    def func_ASCII_16(self,encode_type,source_text):
        try:
            text = self.get_split_data(source_text)
            # print(text)
            result = ''
            for i in text:
                if i != '':
                    # print(i)
                    # print(chr(int(i)))
                    result = result + chr(int(i, 16))
        except Exception as  e:
            return [0, '解码失败',"ASCII(16进制)"]
        return [1, result.strip(),"ASCII(16进制)"]

    def func_jsfuck(self,encode_type,source_text):
        ctx = execjs.compile("""
            function decode(source) {
                output = ''    
                if (source.length > 0) 
                {
                    l = ''

                    if (source.length > 3 && source.slice(source.length-3) == ')()')
                    {
                        //eval-ed
                        s = source.slice(0, source.length - 2)
                        i = s.length

                        //first try----------------------------
                        while (i--) {
                            //if ((l = s.slice(i)).split(')').length == l.split('(').length) break
                            l = s.slice(i)
                            if (l.split(')').length == l.split('(').length) {
                                break;
                            }
                        }
                        //-------------------------------------
                    }
                    else
                    {
                        l = source;
                    }

                    txtResult = eval(l)
                    return txtResult

                }
            }
        """)  # 获取代码编译完成后的对象
        return [1, ctx.call("decode", source_text),"Jsfuck"]

    def func_jjencode(self,encode_type,source_text):
        js = """

            var result =''
            function jjdecode(t)
            {    
                //get string from src


                //clean it
                t.replace(/^\\s+|\\s+$/g, "");

                var startpos;
                var endpos;
                var gv;
                var  gvl;	

                if (t.indexOf("\\"\\'\\\\\\"+\\'+\\",") == 0) //palindrome check
                {
                    //locate jjcode
                    startpos	= t.indexOf('$$+"\\\\""+') + 8;
                    endpos		= t.indexOf('"\\\\"")())()');

                    //get gv
                    gv	= t.substring((t.indexOf('"\\'\\\\"+\\'+",')+9), t.indexOf("=~[]"));
                    gvl	= gv.length;
                }
                else
                {
                    //get gv
                    gv	= t.substr(0, t.indexOf("="));
                    gvl	= gv.length;

                    //locate jjcode
                    startpos	= t.indexOf('"\\\\""+') + 5;
                    endpos		= t.indexOf('"\\\\"")())()');	
                }

                if (startpos == endpos)
                {
                    alert("No data !");
                    return;
                }

                //start decoding
                var data = t.substring(startpos, endpos);

                //hex decode string
                var b=[ "___+", "__$+", "_$_+", "_$$+", "$__+", "$_$+", "$$_+", "$$$+", "$___+", "$__$+", "$_$_+", "$_$$+", "$$__+", "$$_$+", "$$$_+", "$$$$+" ];

                //lotu
                var str_l = "(![]+\\"\\")[" + gv + "._$_]+";
                var str_o = gv + "._$+";
                var str_t = gv + ".__+";
                var str_u = gv + "._+";

                //0123456789abcdef
                var str_hex = gv + ".";

                //s
                var str_s = '"';
                var gvsig = gv + ".";

                var str_quote = '\\\\\\\\\\\\"';
                var str_slash = '\\\\\\\\\\\\\\\\';

                var str_lower = "\\\\\\\\\\"+";
                var str_upper = "\\\\\\\\\\"+" + gv + "._+";

                var str_end	= '"+'; //end of s loop



                while(data != "")
                {
                    //l o t u
                    if (0 == data.indexOf(str_l))
                    {
                        data = data.substr(str_l.length);
                        out("l");
                        continue;
                    }
                    else if (0 == data.indexOf(str_o))
                    {
                        data = data.substr(str_o.length);
                        out("o");
                        continue;
                    }
                    else if (0 == data.indexOf(str_t))
                    {
                        data = data.substr(str_t.length);
                        out("t");
                        continue;
                    }
                    else if (0 == data.indexOf(str_u))
                    {
                        data = data.substr(str_u.length);
                        out("u");
                        continue;
                    }

                    //0123456789abcdef
                    if (0 == data.indexOf(str_hex))
                    {
                        data = data.substr(str_hex.length);

                        //check every element of hex decode string for a match 
                        var i = 0;						
                        for (i = 0; i < b.length; i++)
                        {
                            if (0 == data.indexOf(b[i]))
                            {
                                data = data.substr( (b[i]).length );
                                out(i.toString(16));
                                break;
                            }
                        }
                        continue;
                    }

                    //start of s block
                    if (0 == data.indexOf(str_s))
                    {
                        data = data.substr(str_s.length);

                        //check if "R
                        if (0 == data.indexOf(str_upper)) // r4 n >= 128
                        {
                            data = data.substr(str_upper.length); //skip sig

                            var ch_str = "";				
                            for (j = 0; j < 2; j++) //shouldn't be more than 2 hex chars
                            {
                                //gv + "."+b[ c ]				
                                if (0 == data.indexOf(gvsig))
                                {
                                    data = data.substr(gvsig.length); //skip gvsig	

                                    for (k = 0; k < b.length; k++)	//for every entry in b
                                    {						
                                        if (0 == data.indexOf(b[k]))
                                        {
                                            data = data.substr(b[k].length);
                                            ch_str += k.toString(16) + "";							
                                            break;
                                        }
                                    }						
                                }
                                else
                                {
                                    break; //done
                                }								
                            }

                            out(String.fromCharCode(parseInt(ch_str,16)));
                            continue;
                        }
                        else if (0 == data.indexOf(str_lower)) //r3 check if "R // n < 128
                        {
                            data = data.substr(str_lower.length); //skip sig

                            var ch_str = "";
                            var ch_lotux = ""
                            var temp = "";
                            var b_checkR1 = 0;
                            for (j = 0; j < 3; j++) //shouldn't be more than 3 octal chars
                            {

                                if (j > 1) //lotu check
                                {								
                                    if (0 == data.indexOf(str_l))
                                    {
                                        data = data.substr(str_l.length);
                                        ch_lotux = "l";
                                        break;
                                    }
                                    else if (0 == data.indexOf(str_o))
                                    {
                                        data = data.substr(str_o.length);
                                        ch_lotux = "o";
                                        break;
                                    }
                                    else if (0 == data.indexOf(str_t))
                                    {
                                        data = data.substr(str_t.length);
                                        ch_lotux = "t";
                                        break;
                                    }
                                    else if (0 == data.indexOf(str_u))
                                    {
                                        data = data.substr(str_u.length);
                                        ch_lotux = "u";
                                        break;
                                    }						
                                }

                                //gv + "."+b[ c ]							
                                if (0 == data.indexOf(gvsig))
                                {
                                    temp = data.substr(gvsig.length); 
                                    for (k = 0; k < 8; k++)	//for every entry in b octal
                                    {						
                                        if (0 == temp.indexOf(b[k]))
                                        {
                                            if (parseInt(ch_str + k + "",8) > 128)
                                            {
                                                b_checkR1 = 1;
                                                break;
                                            }								

                                            ch_str += k + "";										
                                            data = data.substr(gvsig.length); //skip gvsig
                                            data = data.substr(b[k].length);
                                            break;
                                        }
                                    }

                                    if (1 == b_checkR1)
                                    {
                                        if (0 == data.indexOf(str_hex)) //0123456789abcdef
                                        {
                                            data = data.substr(str_hex.length);

                                            //check every element of hex decode string for a match 
                                            var i = 0;						
                                            for (i = 0; i < b.length; i++)
                                            {
                                                if (0 == data.indexOf(b[i]))
                                                {
                                                    data = data.substr( (b[i]).length );
                                                    ch_lotux = i.toString(16);
                                                    break;
                                                }
                                            }

                                            break;
                                        }
                                    }								
                                }
                                else
                                {								
                                    break; //done
                                }								
                            }

                            out(String.fromCharCode(parseInt(ch_str,8)) + ch_lotux);
                            continue; //step out of the while loop
                        }
                        else //"S ----> "SR or "S+
                        {

                            // if there is, loop s until R 0r +
                            // if there is no matching s block, throw error

                            var match = 0;
                            var n;

                            //searching for mathcing pure s block
                            while(true)
                            {
                                n = data.charCodeAt( 0 );				
                                if (0 == data.indexOf(str_quote))
                                {
                                    data = data.substr(str_quote.length);
                                    out('"');
                                    match += 1;
                                    continue;
                                }
                                else if (0 == data.indexOf(str_slash))
                                {
                                    data = data.substr(str_slash.length);
                                    out('\\\\');
                                    match += 1;
                                    continue;
                                }
                                else if (0 == data.indexOf(str_end))	//reached end off S block ? +
                                {
                                    if (match == 0)
                                    {
                                        return("+ no match S block: "+data);
                                        return;
                                    }
                                    data = data.substr(str_end.length);

                                    break; //step out of the while loop
                                }
                                else if (0 == data.indexOf(str_upper)) //r4 reached end off S block ? - check if "R n >= 128
                                {						
                                    if (match == 0)
                                    {
                                        return("no match S block n>128: "+data);
                                        return;
                                    }

                                    data = data.substr(str_upper.length); //skip sig

                                    var ch_str = "";
                                    var ch_lotux = "";
                                    for (j = 0; j < 10; j++) //shouldn't be more than 10 hex chars
                                    {

                                        if (j > 1) //lotu check
                                        {								
                                            if (0 == data.indexOf(str_l))
                                            {
                                                data = data.substr(str_l.length);
                                                ch_lotux = "l";
                                                break;
                                            }
                                            else if (0 == data.indexOf(str_o))
                                            {
                                                data = data.substr(str_o.length);
                                                ch_lotux = "o";
                                                break;
                                            }
                                            else if (0 == data.indexOf(str_t))
                                            {
                                                data = data.substr(str_t.length);
                                                ch_lotux = "t";
                                                break;
                                            }
                                            else if (0 == data.indexOf(str_u))
                                            {
                                                data = data.substr(str_u.length);
                                                ch_lotux = "u";
                                                break;
                                            }
                                        }

                                        //gv + "."+b[ c ]				
                                        if (0 == data.indexOf(gvsig))
                                        {
                                            data = data.substr(gvsig.length); //skip gvsig

                                            for (k = 0; k < b.length; k++)	//for every entry in b
                                            {						
                                                if (0 == data.indexOf(b[k]))
                                                {
                                                    data = data.substr(b[k].length);
                                                    ch_str += k.toString(16) + "";							
                                                    break;
                                                }
                                            }						
                                        }
                                        else
                                        {
                                            break; //done
                                        }								
                                    }

                                    out(String.fromCharCode(parseInt(ch_str,16)));
                                    break; //step out of the while loop
                                }
                                else if (0 == data.indexOf(str_lower)) //r3 check if "R // n < 128
                                {
                                    if (match == 0)
                                    {
                                        return("no match S block n<128: "+data);
                                        return;
                                    }

                                    data = data.substr(str_lower.length); //skip sig

                                    var ch_str = "";
                                    var ch_lotux = ""
                                    var temp = "";
                                    var b_checkR1 = 0;
                                    for (j = 0; j < 3; j++) //shouldn't be more than 3 octal chars
                                    {

                                        if (j > 1) //lotu check
                                        {								
                                            if (0 == data.indexOf(str_l))
                                            {
                                                data = data.substr(str_l.length);
                                                ch_lotux = "l";
                                                break;
                                            }
                                            else if (0 == data.indexOf(str_o))
                                            {
                                                data = data.substr(str_o.length);
                                                ch_lotux = "o";
                                                break;
                                            }
                                            else if (0 == data.indexOf(str_t))
                                            {
                                                data = data.substr(str_t.length);
                                                ch_lotux = "t";
                                                break;
                                            }
                                            else if (0 == data.indexOf(str_u))
                                            {
                                                data = data.substr(str_u.length);
                                                ch_lotux = "u";
                                                break;
                                            }								
                                        }

                                        //gv + "."+b[ c ]							
                                        if (0 == data.indexOf(gvsig))
                                        {
                                            temp = data.substr(gvsig.length); 
                                            for (k = 0; k < 8; k++)	//for every entry in b octal
                                            {						
                                                if (0 == temp.indexOf(b[k]))
                                                {
                                                    if (parseInt(ch_str + k + "",8) > 128)
                                                    {
                                                        b_checkR1 = 1;
                                                        break;
                                                    }								

                                                    ch_str += k + "";										
                                                    data = data.substr(gvsig.length); //skip gvsig
                                                    data = data.substr(b[k].length);
                                                    break;
                                                }
                                            }

                                            if (1 == b_checkR1)
                                            {
                                                if (0 == data.indexOf(str_hex)) //0123456789abcdef
                                                {
                                                    data = data.substr(str_hex.length);

                                                    //check every element of hex decode string for a match 
                                                    var i = 0;						
                                                    for (i = 0; i < b.length; i++)
                                                    {
                                                        if (0 == data.indexOf(b[i]))
                                                        {
                                                            data = data.substr( (b[i]).length );
                                                            ch_lotux = i.toString(16);
                                                            break;
                                                        }
                                                    }
                                                }
                                            }								
                                        }
                                        else
                                        {								
                                            break; //done
                                        }								
                                    }

                                    out(String.fromCharCode(parseInt(ch_str,8)) + ch_lotux);
                                    break; //step out of the while loop
                                }	 
                                else if( (0x21 <= n && n <= 0x2f) || (0x3A <= n && n <= 0x40) || ( 0x5b <= n && n <= 0x60 ) || ( 0x7b <= n && n <= 0x7f ) )
                                {
                                    out(data.charAt( 0 ));
                                    data = data.substr( 1 );
                                    match += 1;
                                }

                            }			
                            continue;			
                        }
                    }

                    return("no match : "+data);
                    break;
                }
                return result

            }

            function out(s)
            {
                result+=s;

            }"""  # 获取代码编译完成后的对象
        js_dr = js2py.EvalJs()
        # 执行js代码
        js_dr.execute(js)
        result = js_dr.jjdecode(source_text)
        if 'no match :' in result:
            return [0, result.strip(),'JJEncode']
        return [1, result.strip(),'JJEncode']

    def func_aaencode(self,encode_type,source_text):
        js = """
        function aadecode( text )
        {
            var evalPreamble = "(\uFF9F\u0414\uFF9F) ['_'] ( (\uFF9F\u0414\uFF9F) ['_'] (";
            var decodePreamble = "( (\uFF9F\u0414\uFF9F) ['_'] (";
            var evalPostamble = ") (\uFF9F\u0398\uFF9F)) ('_');";
            var decodePostamble = ") ());";

            // strip beginning/ending space.
            text = text.replace(/^\s*/, "").replace(/\s*$/, "");

            // returns empty text for empty input.
            if (/^\s*$/.test(text)) {
                return "";
            }
            // check if it is encoded.
            if (text.lastIndexOf(evalPreamble) < 0) {
                throw new Error("Given code is not encoded as aaencode.");
            }
            if (text.lastIndexOf(evalPostamble) != text.length - evalPostamble.length) {
                throw new Error("Given code is not encoded as aaencode.");
            }

            var decodingScript = text.replace(evalPreamble, decodePreamble).replace(evalPostamble, decodePostamble);
            return eval(decodingScript);
        }"""  # 获取代码编译完成后的对象
        js_dr = js2py.EvalJs()
        # 执行js代码
        js_dr.execute(js)
        result = js_dr.aadecode(source_text)
        return [1, result.strip(),"AAEncode"]



    def func_base16(self,encode_type,source_text):
        try:
            text = source_text.upper()
            text = base64.b16decode(text.encode(encode_type))
            result_text = str(text, encoding=encode_type)
        except Exception as  e:
            return [0, '解码失败',"Base16"]
        return [1, result_text.strip(),"Base16"]

    def func_base32(self,encode_type,source_text):
        try:
            text = base64.b32decode(source_text.encode(encode_type))
            result_text = str(text, encoding=encode_type)
        except Exception as  e:
            return [0, '解码失败',"Base32"]
    
        return [1, result_text.strip(),"Base32"]

    def func_base36(self,encode_type,source_text):
        try:
            text = base36.dumps(int(source_text))  # 解密
            result_text = str(text)
        except Exception as  e:
            
            return [0, '解码失败',"Base36"]
        return [1, result_text.strip(),"Base36"]

    def func_base58(self,encode_type,source_text):
        try:
            result_text = base58.b58decode(source_text).decode(encode_type)  # 解密
        except Exception as  e:
            return [0, '解码失败',"Base58"]
        return [1, result_text.strip(),"Base58"]

    def func_base62(self,encode_type,source_text):
        try:
            result_text = base62.decode(source_text)
        except:
            return [0, '解码失败',"Base62"]
        return [1, str(result_text).strip(),"Base62"]

    def func_base64(self,encode_type,source_text):
        try:
            text = base64.b64decode(source_text.encode(encode_type))
            result_text = str(text, encoding=encode_type)
        except Exception as  e:
            return [0, '解码失败',"Base64"]
        return [1, result_text.strip(),"Base64"]

    def func_base64_zidingyi(self,encode_type,source_text,n):
        try:
            STANDARD_ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
            CUSTOM_ALPHABET = n.encode()
            DECODE_TRANS = bytes.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)
            result_text = base64.b64decode((source_text.encode()).translate(DECODE_TRANS)).decode()
            return [1, result_text.strip(),"Base64自定义"]
        except Exception as e:
            return [0, str(e),"Base64自定义"]

    def func_bae85_ASCII85(self,encode_type,source_text):
        try:
            result_text = base64.a85decode(source_text).decode(encode_type)  # 解密
        except Exception as  e:
            return [0, '解码失败',"Base85(ASCII85)"]
        return [1, result_text.strip(),"Base85(ASCII85)"]

    def func_bae85_RFC1924(self,encode_type,source_text):
        try:
            result_text = base64.b85decode(source_text).decode(encode_type)  # 解密
        except Exception as  e:
            return [0, '解码失败',"Base85(RFC1924)"]
        return [1, result_text.strip(),"Base85(RFC1924)"]

    def func_base91(self,encode_type,source_text):
        try:
            result_text = base91.decode(source_text).decode(encode_type)
        except Exception as  e:
            return [0, '解码失败',"Base91"]
        return [1, result_text.strip(),"Base91"]

    def func_base92(self,encode_type,source_text):
        try:
            result_text = py3base92.decode(source_text)  # 解密
        except Exception as  e:
            return [0, '解码失败',"Base92"]
        return [1, result_text.strip(),"Base92"]

    def func_Hex_Str(self,encode_type,source_text):
        try:
            text = source_text.replace('0x', '').replace('0X', '')
            result_text = str(bytes.fromhex(text), encoding=encode_type)
        except Exception as e:
            return [0, '解码失败',"Hex->Str"]
        return [1, result_text.strip(),"Hex-Str"]

    def func_shellcode(self,encode_type,source_text):
        try:
            text = source_text.lower()
            if "0x" in text and "\\x" not in text:
                text = text.split('0x')
            elif "\\x" in text and "0x" not in text:
                text = text.split('\\x')
            else:
                result_text = "请输入正确的格式，如：\n\\x61\\x00\\x62\\x00\\x63\n0x610x000x620x000x63"
                return [0, result_text,"Shellcode"]
            result = ''
            for i in text:
                if i != '':
                    result = result + chr(int(i, 16))
            result_text = result
        except Exception as e:
            return [0, '解码失败',"Shellcode"]
        return [1, result_text.strip(),"Shellcode"]

    def func_qwerty(self,encode_type,source_text):
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
            for i in range(0, len(source_text)):
                if source_text[i] != ' ':
                    result_text = result_text + letter.get(source_text[i])
                else:
                    result_text = result_text + ' '
        except Exception as  e:
            return [0, '解码失败',"qwerty编码"]
        return [1, result_text.strip(),"qwerty编码"]

   # 核心价值观编码
    def func_Socialism(sellf, encode_type, source_text):
        values = '富强民主文明和谐自由平等公正法治爱国敬业诚信友善'
        duo = []
        for i in source_text:
            num = values.index(i)
            if num == -1:
                continue
            elif num & 1:
                continue
            else:
                duo.append(num >> 1)
        hexs = []
        i = 0
        while (i < len(duo)):
            if duo[i] < 10:
                hexs.append(duo[i])
            elif duo[i] == 10:
                i += 1
                hexs.append(duo[i] + 10)
            else:
                i += 1
                hexs.append(duo[i] + 6)
            i += 1
        res = ''.join([hex(i)[2:].upper() for i in hexs])
        if len(res) == 0:
            return [0, '解码失败',"核心价值观编码"]

        splited = []
        for i in range(len(res)):
            if i & 1 == 0:
                splited.append('%')
            splited.append(res[i])
        result = urllib.parse.unquote(''.join(splited))
        return [1, result.strip(),"核心价值观编码"]
    def func_jother(sellf, encode_type, source_text):
        # a = Jother()
        # # b =a.toStr("abcd")
        # result = (a.toStr(source_text))

        result = "暂不支持Jother解密，但可以在浏览器按F12打开console，输入密文后回车，可得到解密结果"
        return [0, result,"jother"]
    def func_baijiaxing(sellf, encode_type, source_text):
        CODE = {
            "赵": "0", "钱": "1", "孙": "2", "李": "3", "周": "4", "吴": "5", "郑": "6", "王": "7", "冯": "8", "陈": "9",
            "褚": "a", "卫": "b", "蒋": "c", "沈": "d", "韩": "e", "杨": "f", "朱": "g", "秦": "h", "尤": "i", "许": "j",
            "何": "k", "吕": "l", "施": "m", "张": "n", "孔": "o", "曹": "p", "严": "q", "华": "r", "金": "s", "魏": "t",
            "陶": "u", "姜": "v", "戚": "w", "谢": "x", "邹": "y", "喻": "z", "福": "A", "水": "B", "窦": "C", "章": "D",
            "云": "E", "苏": "F", "潘": "G", "葛": "H", "奚": "I", "范": "J", "彭": "K", "郎": "L", "鲁": "M", "韦": "N",
            "昌": "O", "马": "P", "苗": "Q", "凤": "R", "花": "S", "方": "T", "俞": "U", "任": "V", "袁": "W", "柳": "X",
            "唐": "Y", "罗": "Z", "薛": ".", "伍": "-", "余": "_", "米": "+", "贝": "=", "姚": "/", "孟": "?", "顾": "#",
            "尹": "%", "江": "&", "钟": "*"
        }
        source_text = re.sub('[^\u4e00-\u9fa5]+', '', source_text)
        # source_text = source_text.replace( r"/ ^\s\s * /", '').replace( r"/\s\s *$ /", '')
        cc = [CODE[i] for i in source_text]
        dd = ''.join(cc)
        if dd:
            return [1, 'magnet:?xt=urn:btih:'+dd,"百家姓编码"]
        else:
            return [0, '解码失败',"百家姓编码"]
