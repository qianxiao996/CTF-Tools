# coding=utf-8
import re
from random import random
from module.jother import Jother
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


class Class_Encode:

    def func_url(self, encode_type, source_text):
        text = source_text.encode(encode_type)
        result_text = urllib.parse.quote(text)
        return [1, result_text,"Url"]

    def func_unicode(self, encode_type, source_text):
        text = source_text.encode('unicode_escape')
        result_text = str(text, encoding=encode_type)
        return [1, result_text,"Unicode"]

    def func_escape_u(self, encode_type, source_text):
        text = source_text.encode('unicode_escape')
        result_text = str(text, encoding=encode_type).replace('\\u', '%u')
        return [1, result_text,"Escape_u"]

    def func_html(self, encode_type, source_text):
        result_text = html.escape(source_text)
        return [1, result_text,"html"]

    def func_ASCII_2(self, encode_type, source_text):
        result = ''
        for i in source_text:
            s = int(ord(str(i)))
            re = str(bin(s)).replace('0b', '')
            result += str(re) + ' '
        result_text = str(result)
        return [1, result_text.strip(),"ASCII(2进制)"]

    def func_ASCII_8(self, encode_type, source_text):
        result = ''
        for i in source_text:
            s = int(ord(str(i)))
            re = str(oct(s)).replace('0o', '')
            result += str(re) + ' '
        result_text = str(result)
        return [1, result_text.strip(),"ASCII(8进制)"]

    def func_ASCII_10(self, encode_type, source_text):
        result = ''
        for i in source_text:
            result = str(result) + str(ord(str(i))) + ' '
        result_text = str(result)
        return [1, result_text.strip(),"ASCII(10进制)"]

    def func_ASCII_16(self, encode_type, source_text):
        result = ''
        for i in source_text:
            s = int(ord(str(i)))
            re = str(hex(s)).replace('0x', '')
            result += str(re) + ' '
        result_text = str(result)
        return [1, result_text.strip(),"ASCII(16进制)"]

    def func_base16(self, encode_type, source_text):
        text = source_text.lower()
        text = base64.b16encode(text.encode(encode_type))
        result_text = str(text, encoding=encode_type)
        return [1, result_text,"Base16"]

    def func_base32(self, encode_type, source_text):
        text = base64.b32encode(source_text.encode(encode_type))
        result_text = str(text, encoding=encode_type)
        return [1, result_text,"Base32"]

    def func_base36(self, encode_type, source_text):
        result_text = str(base36.loads(source_text))
        return [1, result_text,"Base36"]

    def func_base58(self, encode_type, source_text):
        result_text = base58.b58encode(source_text.encode(encode_type)).decode()  # 加密
        return [1, result_text,"Base58"]

    def func_base62(self, encode_type, source_text):
        try:
            text = base62.encode(int(source_text))
        except:
            return [0, 'base62只能对数字编码',"Base62"]
        # print(text)
        # result_text = str(text, encoding='utf-8')
        return [1, text,"Base62"]

    def func_base64(self, encode_type, source_text):
        text = base64.b64encode(source_text.encode(encode_type))
        result_text = str(text, encoding=encode_type)
        return [1, result_text,"Base64"]

    def func_base64_zidingyi(self, encode_type, source_text, n):
        try:
            STANDARD_ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
            CUSTOM_ALPHABET = n.encode(encode_type)
            encode_typeTRANS = bytes.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
            result_text = base64.b64encode(source_text.encode(encode_type)).translate(encode_typeTRANS).decode()
            return [1, result_text,"Base64(自定义)"]
        except Exception as e:
            return [0, str(e),"Base64(自定义)"]

    def func_bae85_ASCII85(self, encode_type, source_text):
        result_text = base64.a85encode(source_text.encode(encode_type)).decode(encode_type)  # 加密
        return [1, result_text,"Base85(ASCII85)"]

    def func_bae85_RFC1924(self, encode_type, source_text):
        result_text = base64.b85encode(source_text.encode(encode_type)).decode()  # 加密
        return [1, result_text,"Base85(RFC1924)"]

    def func_base91(self, encode_type, source_text):
        result_text = base91.encode(source_text.encode(encode_type))  #
        return [1, result_text,"Base91"]

    def func_base92(self, encode_type, source_text):
        result_text = py3base92.encode(source_text)
        return [1, result_text,"Base92"]

    def func_Str_Hex(self, encode_type, source_text):
        result = ''
        for i in source_text:
            single = str(hex(ord(str(i))))
            result = result + single
        result_text = (str(result)).replace('0x', '')
        return [1, result_text,"Str->Hex"]

    def func_shellcode(self, encode_type, source_text):
        result = ''
        for i in source_text:
            single = str(hex(ord(str(i))))
            result = result + single
        result_text = (str(result)).replace('0x', '\\x')
        return [1, result_text,"Shellcode"]

    def func_qwerty(self, encode_type, source_text):
        str1 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        str2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result_text = ""
        for s in source_text:
            if s in str1:
                if s != ' ':
                    result_text = result_text + str1[str2.index(s)]
                else:
                    result_text = result_text + ' '
            else:
                return [1, 'Qwerty只能对字母加密!', "Qwerty密码"]
        return [1, result_text,"Qwerty密码"]
        # print(str(e))

    def func_jsfuck(self, encode_type, source_text):
        ctx = execjs.compile("""
    /*! JSFuck 0.4.0 - http://jsfuck.com */
    
    function JSFuck(code){
    
    var USE_CHAR_CODE = "USE_CHAR_CODE";
    
    var MIN = 32, MAX = 126;
    
    var SIMPLE = {
      'false':      '![]',
      'true':       '!![]',
      'undefined':  '[][[]]',
      'NaN':        '+[![]]',
      'Infinity':   '+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]]+[+[]])' // +"1e1000"
    };
    
    var CONSTRUCTORS = {
      'Array':    '[]',
      'Number':   '(+[])',
      'String':   '([]+[])',
      'Boolean':  '(![])',
      'Function': '[]["fill"]',
      'RegExp':   'Function("return/"+false+"/")()'
    };
    
    var MAPPING = {
      'a':   '(false+"")[1]',
      'b':   '([]["entries"]()+"")[2]',
      'c':   '([]["fill"]+"")[3]',
      'd':   '(undefined+"")[2]',
      'e':   '(true+"")[3]',
      'f':   '(false+"")[0]',
      'g':   '(false+[0]+String)[20]',
      'h':   '(+(101))["to"+String["name"]](21)[1]',
      'i':   '([false]+undefined)[10]',
      'j':   '([]["entries"]()+"")[3]',
      'k':   '(+(20))["to"+String["name"]](21)',
      'l':   '(false+"")[2]',
      'm':   '(Number+"")[11]',
      'n':   '(undefined+"")[1]',
      'o':   '(true+[]["fill"])[10]',
      'p':   '(+(211))["to"+String["name"]](31)[1]',
      'q':   '(+(212))["to"+String["name"]](31)[1]',
      'r':   '(true+"")[1]',
      's':   '(false+"")[3]',
      't':   '(true+"")[0]',
      'u':   '(undefined+"")[0]',
      'v':   '(+(31))["to"+String["name"]](32)',
      'w':   '(+(32))["to"+String["name"]](33)',
      'x':   '(+(101))["to"+String["name"]](34)[1]',
      'y':   '(NaN+[Infinity])[10]',
      'z':   '(+(35))["to"+String["name"]](36)',
    
      'A':   '(+[]+Array)[10]',
      'B':   '(+[]+Boolean)[10]',
      'C':   'Function("return escape")()(("")["italics"]())[2]',
      'D':   'Function("return escape")()([]["fill"])["slice"]("-1")',
      'E':   '(RegExp+"")[12]',
      'F':   '(+[]+Function)[10]',
      'G':   '(false+Function("return Date")()())[30]',
      'H':   USE_CHAR_CODE,
      'I':   '(Infinity+"")[0]',
      'J':   USE_CHAR_CODE,
      'K':   USE_CHAR_CODE,
      'L':   USE_CHAR_CODE,
      'M':   '(true+Function("return Date")()())[30]',
      'N':   '(NaN+"")[0]',
      'O':   '(NaN+Function("return{}")())[11]',
      'P':   USE_CHAR_CODE,
      'Q':   USE_CHAR_CODE,
      'R':   '(+[]+RegExp)[10]',
      'S':   '(+[]+String)[10]',
      'T':   '(NaN+Function("return Date")()())[30]',
      'U':   '(NaN+Function("return{}")()["to"+String["name"]]["call"]())[11]',
      'V':   USE_CHAR_CODE,
      'W':   USE_CHAR_CODE,
      'X':   USE_CHAR_CODE,
      'Y':   USE_CHAR_CODE,
      'Z':   USE_CHAR_CODE,
    
      ' ':   '(NaN+[]["fill"])[11]',
      '!':   USE_CHAR_CODE,
      '"':   '("")["fontcolor"]()[12]',
      '#':   USE_CHAR_CODE,
      '$':   USE_CHAR_CODE,
      '%':   'Function("return escape")()([]["fill"])[21]',
      '&':   '("")["link"](0+")[10]',
      '\\'':  USE_CHAR_CODE,
      '(':   '(undefined+[]["fill"])[22]',
      ')':   '([0]+false+[]["fill"])[20]',
      '*':   USE_CHAR_CODE,
      '+':   '(+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]])+[])[2]',
      ',':   '([]["slice"]["call"](false+"")+"")[1]',
      '-':   '(+(.+[0000000001])+"")[2]',
      '.':   '(+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]]+[+[]])+[])[+!+[]]',
      '/':   '(false+[0])["italics"]()[10]',
      ':':   '(RegExp()+"")[3]',
      ';':   '("")["link"](")[14]',
      '<':   '("")["italics"]()[0]',
      '=':   '("")["fontcolor"]()[11]',
      '>':   '("")["italics"]()[2]',
      '?':   '(RegExp()+"")[2]',
      '@':   USE_CHAR_CODE,
      '[':   '([]["entries"]()+"")[0]',
      '\\\\':  USE_CHAR_CODE,
      ']':   '([]["entries"]()+"")[22]',
      '^':   USE_CHAR_CODE,
      '_':   USE_CHAR_CODE,
      '`':   USE_CHAR_CODE,
      '{':   '(true+[]["fill"])[20]',
      '|':   USE_CHAR_CODE,
      '}':   '([]["fill"]+"")["slice"]("-1")',
      '~':   USE_CHAR_CODE
    };
    
    var GLOBAL = 'Function("return this")()';
    
    function fillMissingChars(){
      for (var key in MAPPING){
        if (MAPPING[key] === USE_CHAR_CODE){
          MAPPING[key] = 'Function("return unescape")()("%"'+ key.charCodeAt(0).toString(16).replace(/(\\d+)/g, "+($1)+\\"") + '")';
        }
      }
    }
    
    function fillMissingDigits(){
      var output, number, i;
    
      for (number = 0; number < 10; number++){
    
        output = "+[]";
    
        if (number > 0){ output = "+!" + output; }
        for (i = 1; i < number; i++){ output = "+!+[]" + output; }
        if (number > 1){ output = output.substr(1); }
    
        MAPPING[number] = "[" + output + "]";
      }
    }
    
    function replaceMap(){
      var character = "", value, original, i, key;
    
      function replace(pattern, replacement){
        value = value.replace(
          new RegExp(pattern, "gi"),
          replacement
        );
      }
    
      function digitReplacer(_,x) { return MAPPING[x]; }
    
      function numberReplacer(_,y) {
        var values = y.split("");
        var head = +(values.shift());
        var output = "+[]";
    
        if (head > 0){ output = "+!" + output; }
        for (i = 1; i < head; i++){ output = "+!+[]" + output; }
        if (head > 1){ output = output.substr(1); }
    
        return [output].concat(values).join("+").replace(/(\\d)/g, digitReplacer);
      }
    
      for (i = MIN; i <= MAX; i++){
        character = String.fromCharCode(i);
        value = MAPPING[character];
        if(!value) {continue;}
        original = value;
    
        for (key in CONSTRUCTORS){
          replace("\\\\b" + key, CONSTRUCTORS[key] + '["constructor"]');
        }
    
        for (key in SIMPLE){
          replace(key, SIMPLE[key]);
        }
    
        replace('(\\\\d\\\\d+)', numberReplacer);
        replace('\\\\((\\\\d)\\\\)', digitReplacer);
        replace('\\\\[(\\\\d)\\\\]', digitReplacer);
    
        replace("GLOBAL", GLOBAL);
        replace('\\\\+""', "+[]");
        replace('""', "[]+[]");
    
        MAPPING[character] = value;
      }
    }
    
    function replaceStrings(){
      var regEx = /[^\\[\\]\\(\\)\\!\\+]{1}/g,
        all, value, missing,
        count = MAX - MIN;
    
      function findMissing(){
        var all, value, done = false;
    
        missing = {};
    
        for (all in MAPPING){
    
          value = MAPPING[all];
    
          if (value.match(regEx)){
            missing[all] = value;
            done = true;
          }
        }
    
        return done;
      }
    
      function mappingReplacer(a, b) {
        return b.split("").join("+");
      }
    
      function valueReplacer(c) {
        return missing[c] ? c : MAPPING[c];
      }
    
      for (all in MAPPING){
        MAPPING[all] = MAPPING[all].replace(/\\"([^\\"]+)\\"/gi, mappingReplacer);
      }
    
      while (findMissing()){
        for (all in missing){
          value = MAPPING[all];
          value = value.replace(regEx, valueReplacer);
    
          MAPPING[all] = value;
          missing[all] = value;
        }
    
        if (count-- === 0){
          console.error("Could not compile the following chars:", missing);
        }
      }
    }
    
    function encode(input, wrapWithEval, runInParentScope){
      var output = [];
    
      if (!input){
        return "";
      }
    
      var r = "";
      for (var i in SIMPLE) {
        r += i + "|";
      }
      r+=".";
    
      input.replace(new RegExp(r, 'g'), function(c) {
        var replacement = SIMPLE[c];
        if (replacement) {
          output.push("[" + replacement + "]+[]");
        } else {
          replacement = MAPPING[c];
          if (replacement){
            output.push(replacement);
          } else {
            replacement =
              "([]+[])[" + encode("constructor") + "]" +
              "[" + encode("fromCharCode") + "]" +
              "(" + encode(c.charCodeAt(0) + "") + ")";
    
            output.push(replacement);
            MAPPING[c] = replacement;
          }
        }
      });
    
      output = output.join("+");
    
      if (/^\\d$/.test(input)){
        output += "+[]";
      }
    
      if (wrapWithEval){
        if (runInParentScope){
          output = "[][" + encode("fill") + "]" +
            "[" + encode("constructor") + "]" +
            "(" + encode("return eval") +  ")()" +
            "(" + output + ")";
        } else {
          output = "[][" + encode("fill") + "]" +
            "[" + encode("constructor") + "]" +
            "(" + output + ")()";
        }
      }
    
      return output;
    }
    
    fillMissingDigits();
    fillMissingChars();
    replaceMap();
    replaceStrings();
    
    var js_fuck_payload = encode(code,1);
    return js_fuck_payload;
    };
                """)  # 获取代码编译完成后的对象

        result = ctx.call("JSFuck", source_text, '1')
        return [1, result,"Jsfuck"]
        # f = open('./module/jsfuck.js', 'r')
        # jsf_code = f.read()
        # js = execjs.get()
        # # print(jsf_code)
        # # print "Using Engine %s" % js.name
        # jsf_int = js.compile(jsf_code)
        # return_text = jsf_int.call("JSFuck", text, '1')
        # return(return_text)

    def func_jjencode(self, encode_type, source_text):
        js = """
        function keyup( t )
        {
        var _prev;
            var v = "$";
            var p = false;
            var r;
    
            if( _prev != ( t + "\\0" + v + "\\0" + p ) || true ){
                r = jjencode( v, t );
                if( p ){
                    r = r.replace( /[,;]$/, "" );
                    r = "\\"\\'\\\\\\"+\\'+\\"," + r + ",\\'," + r.split("").reverse().join("") +",\\"+\\'+\\"\\\\\\'\\"";
                }
                return r 
    
            }
    
        }
        function jjencode( gv, text )
        {
            var r="";
            var n;
            var t;
            var b=[ "___", "__$", "_$_", "_$$", "$__", "$_$", "$$_", "$$$", "$___", "$__$", "$_$_", "$_$$", "$$__", "$$_$", "$$$_", "$$$$", ];
            var s = "";
            for( var i = 0; i < text.length; i++ ){
                n = text.charCodeAt( i );
                if( n == 0x22 || n == 0x5c ){
                    s += "\\\\\\\\\\\\" + text.charAt( i ).toString(16);
                }else if( (0x21 <= n && n <= 0x2f) || (0x3A <= n && n <= 0x40) || ( 0x5b <= n && n <= 0x60 ) || ( 0x7b <= n && n <= 0x7f ) ){
                //}else if( (0x20 <= n && n <= 0x2f) || (0x3A <= n == 0x40) || ( 0x5b <= n && n <= 0x60 ) || ( 0x7b <= n && n <= 0x7f ) ){
                    s += text.charAt( i );
                }else if( (0x30 <= n && n <= 0x39 ) || (0x61 <= n && n <= 0x66 ) ){
                    if( s ) r += "\\"" + s +"\\"+";
                    r += gv + "." + b[ n < 0x40 ? n - 0x30 : n - 0x57 ] + "+";
                    s="";
                }else if( n == 0x6c ){ // 'l'
                    if( s ) r += "\\"" + s + "\\"+";
                    r += "(![]+\\"\\")[" + gv + "._$_]+";
                    s = "";
                }else if( n == 0x6f ){ // 'o'
                    if( s ) r += "\\"" + s + "\\"+";
                    r += gv + "._$+";
                    s = "";
                }else if( n == 0x74 ){ // 'u'
                    if( s ) r += "\\"" + s + "\\"+";
                    r += gv + ".__+";
                    s = "";
                }else if( n == 0x75 ){ // 'u'
                    if( s ) r += "\\"" + s + "\\"+";
                    r += gv + "._+";
                    s = "";
                }else if( n < 128 ){
                    if( s ) r += "\\"" + s;
                    else r += "\\"";
                    r += "\\\\\\\\\\"+" + n.toString( 8 ).replace( /[0-7]/g, function(c){ return gv + "."+b[ c ]+"+" } );
                    s = "";
                }else{
                    if( s ) r += "\\"" + s;
                    else r += "\\"";
                    r += "\\\\\\\\\\"+" + gv + "._+" + n.toString(16).replace( /[0-9a-f]/gi, function(c){ return gv + "."+b[parseInt(c,16)]+"+"} );
                    s = "";
                }
            }
            if( s ) r += "\\"" + s + "\\"+";
    
            r = 
            gv + "=~[];" + 
            gv + "={___:++" + gv +",$$$$:(![]+\\"\\")["+gv+"],__$:++"+gv+",$_$_:(![]+\\"\\")["+gv+"],_$_:++"+
            gv+",$_$$:({}+\\"\\")["+gv+"],$$_$:("+gv+"["+gv+"]+\\"\\")["+gv+"],_$$:++"+gv+",$$$_:(!\\"\\"+\\"\\")["+
            gv+"],$__:++"+gv+",$_$:++"+gv+",$$__:({}+\\"\\")["+gv+"],$$_:++"+gv+",$$$:++"+gv+",$___:++"+gv+",$__$:++"+gv+"};"+
            gv+".$_="+
            "("+gv+".$_="+gv+"+\\"\\")["+gv+".$_$]+"+
            "("+gv+"._$="+gv+".$_["+gv+".__$])+"+
            "("+gv+".$$=("+gv+".$+\\"\\")["+gv+".__$])+"+
            "((!"+gv+")+\\"\\")["+gv+"._$$]+"+
            "("+gv+".__="+gv+".$_["+gv+".$$_])+"+
            "("+gv+".$=(!\\"\\"+\\"\\")["+gv+".__$])+"+
            "("+gv+"._=(!\\"\\"+\\"\\")["+gv+"._$_])+"+
            gv+".$_["+gv+".$_$]+"+
            gv+".__+"+
            gv+"._$+"+
            gv+".$;"+
            gv+".$$="+
            gv+".$+"+
            "(!\\"\\"+\\"\\")["+gv+"._$$]+"+
            gv+".__+"+
            gv+"._+"+
            gv+".$+"+
            gv+".$$;"+
            gv+".$=("+gv+".___)["+gv+".$_]["+gv+".$_];"+
            gv+".$("+gv+".$("+gv+".$$+\\"\\\\\\"\\"+" + r + "\\"\\\\\\"\\")())();";
    
            return r;
        }"""  # 获取代码编译完成后的对象
        js_dr = js2py.EvalJs()
        # 执行js代码
        js_dr.execute(js)
        result = js_dr.keyup(source_text)
        return [1, result,"JJEncode"]

    def func_aaencode(self, encode_type, source_text):
        js = """
        function aaencode( text )
        {
            var t;
            var b = [
                "(c^_^o)",
                "(ﾟΘﾟ)",
                "((o^_^o) - (ﾟΘﾟ))",
                "(o^_^o)",
                "(ﾟｰﾟ)",
                "((ﾟｰﾟ) + (ﾟΘﾟ))",
                "((o^_^o) +(o^_^o))",
                "((ﾟｰﾟ) + (o^_^o))",
                "((ﾟｰﾟ) + (ﾟｰﾟ))",
                "((ﾟｰﾟ) + (ﾟｰﾟ) + (ﾟΘﾟ))",
                "(ﾟДﾟ) .ﾟωﾟﾉ",
                "(ﾟДﾟ) .ﾟΘﾟﾉ",
                "(ﾟДﾟ) ['c']",
                "(ﾟДﾟ) .ﾟｰﾟﾉ",
                "(ﾟДﾟ) .ﾟДﾟﾉ",
                "(ﾟДﾟ) [ﾟΘﾟ]"
                ];
            var r = "ﾟωﾟﾉ= /｀ｍ´）ﾉ ~┻━┻   //*´∇｀*/ ['_']; o=(ﾟｰﾟ)  =_=3; c=(ﾟΘﾟ) =(ﾟｰﾟ)-(ﾟｰﾟ); "; 
    
            if( /ひだまりスケッチ×(365|３５６)\\s*来週も見てくださいね[!！]/.test( text ) ){
                r += "X=_=3; ";
                r += "\\r\\n\\r\\n    X / _ / X < \\"来週も見てくださいね!\\";\\r\\n\\r\\n";
            }
            r += "(ﾟДﾟ) =(ﾟΘﾟ)= (o^_^o)/ (o^_^o);"+
                "(ﾟДﾟ)={ﾟΘﾟ: '_' ,ﾟωﾟﾉ : ((ﾟωﾟﾉ==3) +'_') [ﾟΘﾟ] "+
                ",ﾟｰﾟﾉ :(ﾟωﾟﾉ+ '_')[o^_^o -(ﾟΘﾟ)] "+
                ",ﾟДﾟﾉ:((ﾟｰﾟ==3) +'_')[ﾟｰﾟ] }; (ﾟДﾟ) [ﾟΘﾟ] =((ﾟωﾟﾉ==3) +'_') [c^_^o];"+
                "(ﾟДﾟ) ['c'] = ((ﾟДﾟ)+'_') [ (ﾟｰﾟ)+(ﾟｰﾟ)-(ﾟΘﾟ) ];"+
                "(ﾟДﾟ) ['o'] = ((ﾟДﾟ)+'_') [ﾟΘﾟ];"+
                "(ﾟoﾟ)=(ﾟДﾟ) ['c']+(ﾟДﾟ) ['o']+(ﾟωﾟﾉ +'_')[ﾟΘﾟ]+ ((ﾟωﾟﾉ==3) +'_') [ﾟｰﾟ] + "+
                "((ﾟДﾟ) +'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ ((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+"+
                "((ﾟｰﾟ==3) +'_') [(ﾟｰﾟ) - (ﾟΘﾟ)]+(ﾟДﾟ) ['c']+"+
                "((ﾟДﾟ)+'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ (ﾟДﾟ) ['o']+"+
                "((ﾟｰﾟ==3) +'_') [ﾟΘﾟ];(ﾟДﾟ) ['_'] =(o^_^o) [ﾟoﾟ] [ﾟoﾟ];"+
                "(ﾟεﾟ)=((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟДﾟ) .ﾟДﾟﾉ+"+
                "((ﾟДﾟ)+'_') [(ﾟｰﾟ) + (ﾟｰﾟ)]+((ﾟｰﾟ==3) +'_') [o^_^o -ﾟΘﾟ]+"+
                "((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟωﾟﾉ +'_') [ﾟΘﾟ]; "+
                "(ﾟｰﾟ)+=(ﾟΘﾟ); (ﾟДﾟ)[ﾟεﾟ]='\\\\\\\\'; "+
                "(ﾟДﾟ).ﾟΘﾟﾉ=(ﾟДﾟ+ ﾟｰﾟ)[o^_^o -(ﾟΘﾟ)];"+ 
                "(oﾟｰﾟo)=(ﾟωﾟﾉ +'_')[c^_^o];"+//TODO
                "(ﾟДﾟ) [ﾟoﾟ]='\\\\\\"';"+ 
                "(ﾟДﾟ) ['_'] ( (ﾟДﾟ) ['_'] (ﾟεﾟ+";
            r += "(ﾟДﾟ)[ﾟoﾟ]+ ";
            for( var i = 0; i < text.length; i++ ){
                n = text.charCodeAt( i );
                t = "(ﾟДﾟ)[ﾟεﾟ]+";
                if( n <= 127 ){
                    t += n.toString( 8 ).replace( /[0-7]/g, function(c){ return b[ c ] + "+ "; } );
                }else{
                    var m = /[0-9a-f]{4}$/.exec( "000" + n.toString(16 ) )[0];
                    t += "(oﾟｰﾟo)+ " + m.replace( /[0-9a-f]/gi, function(c){ return b[ parseInt( c,16 ) ] + "+ "; } );
                }
                r += t;
    
            }
            r += "(ﾟДﾟ)[ﾟoﾟ]) (ﾟΘﾟ)) ('_');";
            return r;
    
    
        }"""
        js_dr = js2py.EvalJs()
        # 执行js代码
        js_dr.execute(js)
        result = js_dr.aaencode(source_text)
        return [1, result,"AAEncode"]

    def func_Socialism(self, encode_type, source_text):

        values = '富强民主文明和谐自由平等公正法治爱国敬业诚信友善'
        strs = "0123456789ABCDEF"
        pattern = re.compile(r"[A-Za-z0-9\-\_\.\!\~\*\'\(\)]")
        str1 = ''
        for i in source_text:
            if pattern.match(i) == None:
                str1 += urllib.parse.quote(i.encode())
            else:
                str1 += hex(ord(i))[2:]

        concated = str1.replace('%', '').upper()
        duo = []
        for i in concated:
            n = strs.index(i)
            if n < 10:
                duo.append(n)
            elif random() >= 0.5:
                duo.append(10)
                duo.append(n - 10)
            else:
                duo.append(11)
                duo.append(n - 6)
        result = ''.join([values[2 * i] + values[2 * i + 1] for i in duo])
        return [1, result,"核心价值观编码"]

    def func_jother(sellf, encode_type, source_text):
        a = Jother()
        result = (a.toScript(source_text))
        return [1, result,"Jother"]

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
        source_text = re.sub('[\u4e00-\u9fa5]', '', source_text)
        # source_text = source_text.replace( r"/ ^\s\s * /", '').replace( r"/\s\s *$ /", '')
        CODE = dict((value, key) for key, value in CODE.items())
        cc = [CODE[i] for i in source_text]
        dd = ''.join(cc)
        return [1, dd,"百家姓编码"]
