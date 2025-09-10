# coding:utf-8
# author:杨淑娟


# 在Python中类里定义的函数称为方法
class Computer(): # 默认继承object类
    # 商品介绍中的内容就是对象的属性
    def __init__(self,proname,proid,weight,place,color,type,system):  # 小括号中的叫方法 的参数，在调用处传入
        self.proname=proname
        self.proid=proid
        self.weight=weight
        self.place=place
        self.color=color
        self.type=type
        self.system=system

    # 商品介绍是信息的展示
    def show(self):
        print(f'商品名称:{self.proname}\t商品编号:{self.proid}\t商品毛重:{self.weight}\t\t商品产地:{self.place}')
        print(f'屏幕包域:{self.color}\t\t类型:{self.type}\t\t系统:{self.system}')

    # 这个方法就是类方法
    @classmethod    # @classmethod  这是类方法的标记符，，只要看到方法出有@classmethod 就是类方法 ，类方法有参数cls
    def fun(cls):
        pass

    @staticmethod  # 这个是静态方法， 静代方法没有参数
    def methond():
        pass



# 创建笔记本的对象 ，创建对象时默认调用__init?__方法，
com=Computer('机械革命蛟龙','100012301235','4.76kg','中国大陆','100%sRGB','高端游戏笔记本','Windows 10 不带Office')
com.show()