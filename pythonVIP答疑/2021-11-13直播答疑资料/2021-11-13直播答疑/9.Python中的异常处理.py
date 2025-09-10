# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

def function_name(level):  # 函数的定义处
    if level<1:          #在Exception 的__init__(self,*args)
        raise Exception(level) #触发异常，创建异常对象 将由调用处进行捕获
    return level

try :
    x=function_name(-10)  #这是调用处     ,执行这句代码时，产生异常 ，跳到13行 ，捕获异常
    print('level=',x)
except Exception as e:    #　产生异常对象    e,类型是Exception
    print('error in level argument',e.args[0])   # 对象名  e   args是一个列表，0表示的是索引
