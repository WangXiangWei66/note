# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

class Dog: #Ｄｏｇ就是类的名称，简称Dog类
    color ='白色'  #　直接在类里定义的变量　，就是类属性

    def __init__(self,xm):
        self.name=xm  #这个ｓｅｌｆ．ｎａｍｅ就是实例属性


    def show(self): # 使用def定义的函数，位置在Dog类中，所以称为实例方法
        print('哈哈')


