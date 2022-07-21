# CTF-Tools

![1](https://github.com/qianxiao996/CTF-Tools/blob/master/1.jpg)

一款CTF编码、解码、加密、解密工具。

##### 支持的编码解码:            

- [x] URL

- [x] Unicode

- [x] Escape(%U)

- [x] HtmlEncode

- [x] ACSII(2进制)

- [x] ACSII(8进制)

- [x] ACSII(10进制)

- [x] ACSII(16进制)

- [x] Shellcode

- [x] qwerty(键盘密码)

- [x] Str->Hex

- [x] 图片转base64

- [x] 图片转hex

- [x] JsFuck

- [x] JJEncode

- [x] AAEncode

- [x] jother

- [x] 百家姓编码

- [x] 核心价值观编码

##### 支持的base编码

- [x] Base16

- [x] Base32

- [x] Base36

- [x] Base58

- [x] Base62

- [x] Base64

- [x] Base64(自定义)

- [x] Base85(ASCII85)

- [x] Base85(RFC1924)

- [x] Base91

- [x] Base92

  

##### 支持的加密解密:

- [x] Rot13
- [x] 凯撒密码
- [x] 栅栏密码
- [x] 栅栏密码(W型)
- [x] 培根密码
- [x] 摩斯密码
- [x] 移位密码
- [x] 云影密码
- [x] 当铺密码
- [x] 四方密码
- [x] 仿射密码
- [x] a1z26密码 
- [x] 维尼吉亚密码
- [x] 埃特巴什码
- [x] 与佛论禅 

##### 进制转换:

- [x] 2->8
- [x] 2->10
- [x] 2->16
- [x] 8->2
- [x] 8->10
- [x] 8->16
- [x] 10->2
- [x] 10->8
- [x] 10->16
- [x] 16->2
- [x] 16->8
- [x] 16->10
- [x] 任意进制转换

##### 在线编码网站:

- [x] Jsfuck
- [x] AAencode
- [x] XXencode
- [x] JJencode
- [x] UUencode
- [x] Brainfuck/Ook!
- [x] 敲击码
- [x] 猪圈密码
- [x] 综合网站
- [x] Rabbit

......

##### 插件功能:

须在Plugins目录下的Plugins.json写入插件名称和文件名。

插件模板

```
######################No UI ##########################
# 普通函数不打开ui插件
# def run(source_text,UI_1,UI_2):
#     result='插件测试'
#     return [1,result,"插件测试"]

######################UI 1 ##########################
#打开UI1
# def run(source_text,UI_1,UI_2):
#     #参数解释：1：调用的函数 2：窗口标题 3、label文字
#     UI_1('ui_1_click', '窗口标题', 'Label')
#     return None
# def ui_1_click(text,key1):
#     # 返回结果
#     return  "编码结果"
######################UI 2 ##########################
#打开UI2
def run(source_text,UI_1,UI_2):
    #参数解释：1：调用的函数 2：窗口标题 3、label文字
    UI_2('ui_2_click', '窗口标题', 'Label1',"Label2")
    return None
def ui_2_click(text,key1,key2):
    # 返回结果
    return  "编码结果"

```

