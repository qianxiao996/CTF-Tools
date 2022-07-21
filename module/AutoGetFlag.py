# GUI 独立程序 密文分析
import importlib
import json,time,os,sys
from treelib import Tree
from PyQt5.QtCore import QThread, pyqtSignal

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from module.func_binary import Class_Binary
from module.func_decode import Class_Decode
from module.func_encrypt import Class_Encrypt
from module.func_encode import Class_Encode
from module.func_tools import Class_Tools
from module.func_decrypt import Class_Decrypt
# 识别密文
def Cipherase(cryptostr, key1, key2, key3):

    all_jiemi_result = []
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
            if Function_canshu_num == 3:
                result = Function(i[0], 'utf-8', cryptostr)
            elif Function_canshu_num == 4:
                result = Function(i[0], 'utf-8', cryptostr, key1)
            elif Function_canshu_num == 5:
                result = Function(i[0], 'utf-8', cryptostr, key1, key2)
            elif Function_canshu_num == 6:
                result  = Function(i[0], 'utf-8', cryptostr, key1,key2,key3)
            else:
                pass
        except:
            pass
        if  result and len(result)>=3 and result[0]  and result[1] and result[1]!=cryptostr and len(str(cryptostr)) > len(str(result[1])):
            #密码名称，解密结果
            all_jiemi_result.append([result[2],cryptostr,result[1]])
    return all_jiemi_result

class AutoGetFlag(QThread):
    signal = pyqtSignal(list)

    def __init__(self, cryptostr, key1, key2, flag_str):
        super().__init__()
        self.cryptostr = cryptostr
        self.key1 = key1
        self.key2 = key2
        self.flag_str = flag_str

    def run(self):
        self.depth=10
        # 识别密文
        #0 识别成功 解密结果  解密类型
        result = Cipherase(self.cryptostr, self.key1, self.key2, self.flag_str)
        # result=[]
        # for i in result_list:
        #     result.append([i[2],i[0],i[1]])
        #
        # if self.log:
        ###################
        # 生成第一个父子节点
        FandS_node = []  # 0为父节点，其他为子节点，格式为 [ ["parent","name1","name2"],[...] ]
        temp_FS_node = []

        cry_path = Tree()
        tree = cry_path.create_node(tag='Path',)  # 解密路线树
        for i in result:
            test = cry_path.create_node(tag=i[0], parent=tree)
            temp_FS_node.append(test.identifier)
            FandS_node.append(temp_FS_node)
        ###############
        Flag = False  # 判断flag存不存在的关键词
        self.res = ''
        filename = ''
        cry_cryptostr = ''
        depth_s = True
        if self.depth != '':
            depth_num = int(self.depth) - 1
        else:
            depth_num=9
        while(len(result) != 0 and len(result) < 100 and depth_s and not  Flag):
            # 每轮广度遍历时初始化变量
            temporary = []
            result_dict = {}
            temp_FandS_node = []
            for i in result:
                # print(i)
                try:
                    self.res = i[2]
                    if self.flag_str in i[2]:
                        # print(i[2])
                        # self.signal.emit([1,i[2]])
                        Flag =True
                        self.res = i[2]
                        # if self.log:
                        cry_path.create_node(
                            tag=i[2], parent=FandS_node[result.index(i)][0], data=i[1])
                        #########3
                        break
                except:
                    pass
                # 密文分析后的cryptoname
                # aaa_result = []
                aaa_result = Cipherase(i[2], self.key1, self.key2, self.flag_str)
                # for j in fenxi_result:
                #     aaa_result.append([j[2], j[0], j[1]])
                # 不需要导日志则不必要生成crypto_name与name的字典
                temp_FS_node = []
                # # if self.log and len(FandS_node) != 0:
                if  len(FandS_node) != 0:
                    for j in aaa_result:
                        # print(i)
                        # print(result.index(i))
                        test = cry_path.create_node(
                            tag=j[0], parent=FandS_node[result.index(i)][0], data=j[2])
                        temp_FS_node.append(test.identifier)
                        temp_FandS_node.append(temp_FS_node)
                temporary.extend(aaa_result)
            if Flag:
                break
            result = temporary
            FandS_node = temp_FandS_node
            if self.depth != '':
                depth_num = depth_num - 1
                if depth_num > 0:
                    depth_s = True
                else:
                    depth_s = False
        # print(["查找完成！"])
        now2 = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
        cry_path_name = "./{}.txt".format(now2)
        cry_path.save2file(cry_path_name)
        # 读取解析树
        try:
            with open(cry_path_name, "r", encoding="utf-8") as f:
                cry_tree = f.read()
            os.remove(cry_path_name)
        except:
            pass
        len_k = ''
        for k in cry_path.paths_to_leaves():
            if len(k) > len(len_k):
                len_k = k
        # if Flag == False:
        #     cry_path.create_node(
        #         tag=self.flag_str + "【无法解密】", parent=len_k[-1])
        # 最长解密链 max_long_cry
        test_m = []
        for m in len_k:
            test_m.append(cry_path.get_node(m).tag)
        if Flag == False:
            test_m.append(self.flag_str)
        max_long_cry = ' -> '.join(test_m)

        # 最终密文
        cry_fin = cry_path.get_node(len_k[-1]).data
        textaaa = "\nflag关键词：{}\n\n密钥1：{}\n\n密钥2：{}\n\n深度：{}\n\n初始密文：{}\n\n解析树：\n{}\n最长解密链：\n{}\n\n最终密文：\n{}\n\n最终解密结果：\n{}\n\n".format(
                self.flag_str, self.key1,self.key2,self.depth, self.cryptostr, cry_tree, max_long_cry, cry_fin,self.res)
        if not Flag:
            self.signal.emit([0,textaaa])
        else:
            self.signal.emit([1,textaaa])
