# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import traceback # 这是一个模块
#自定义异常为
class  MyException (Exception):
    pass

def main():
    methodA()

def methodA():
    methodB()

def methodB():
    methodC()

def methodC():
    raise MyException('自定义异常信息')   # methodC触发了异常，这个异常传给了methodB,
                                     #methodB传给了methodA,最后到main终止，这个过程叫异常的传播轨迹

try:
    main() #调用main执行
except:  #捕获异常
   # traceback.print_exc() # 输出到控制台上    听没听过  错误日志
    traceback.print_exc(file=open('log.txt','a'))

