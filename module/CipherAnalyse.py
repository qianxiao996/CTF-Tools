# GUI 独立程序 密文分析
import importlib
import json
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal
from module.func_binary import Class_Binary
from module.func_decode import Class_Decode
from module.func_encrypt import Class_Encrypt
from module.func_encode import Class_Encode
from module.func_tools import Class_Tools
from module.func_decrypt import Class_Decrypt


class Cipher_Thread(QThread):
    signal = pyqtSignal(list)

    def __init__(self, cryptostr, key1, key2, key3):
        super().__init__()
        self.cryptostr = cryptostr
        self.key1 = key1
        self.key2 = key2
        self.key3 = key3

    def run(self):
        # 识别密文
        # 存放所有可调用的方法
        class_methods_list = []
        # 导入自定义解密插件
        with open("Plugins/Plugins.json", 'r+', encoding='utf-8') as f:
            Crypto_json = json.load(f)
        for i in Crypto_json:
            plugins_filename = "Plugins/" + Crypto_json[i]
            plugins_methods = "Plugins/" + Crypto_json[i][:-3]
            nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(plugins_methods, plugins_filename).load_module()
            # 参数一为类对象，二为方法名
            class_methods_list.append([nnnnnnnnnnnn1, 'run',i])
            # str1 = "import Plugins.{crypto_name}".format(crypto_name=i)
            # exec(str1)
        for i in ["Class_Decode", "Class_Decrypt"]:
            obj = eval(i)
            # 得到所有方法
            a = (dir(obj))
            for j in a:
                # print(j[:5])
                if j[:5] == "func_":
                    class_methods_list.append([obj, j,j.replace('func_','')])

        for i in class_methods_list:
            Function = getattr(i[0], i[1])  # 以字符串的形式执行函数
            Function_canshu_num = Function.__code__.co_argcount
            result=''
            try:
                status=0
                type__ =''
                if Function_canshu_num == 3:
                    status,result,type__= Function(i[0],'utf-8',self.cryptostr)
                elif  Function_canshu_num == 4:
                    status,result,type__= Function(i[0],'utf-8',self.cryptostr,self.key1)
                elif  Function_canshu_num == 5:
                    status,result,type__ = Function(i[0],'utf-8',self.cryptostr,self.key1,self.key2)
                elif  Function_canshu_num == 6:
                    status,result,type__ = Function(i[0],'utf-8',self.cryptostr,self.key1,self.key2,self.key3)
                else:
                    pass

                if status and len(result)>=3:
                    # 发出信号
                    self.signal.emit([1,type__,result])
            except Exception as e:
                pass
                # self.signal.emit([i[2],str(e)])
        self.signal.emit([1,"end",''])
