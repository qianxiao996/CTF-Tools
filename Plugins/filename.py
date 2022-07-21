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
