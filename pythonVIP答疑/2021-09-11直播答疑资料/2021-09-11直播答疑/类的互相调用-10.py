# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

class Student():
    def __init__(self,name,com):
        self.name=name    #com 在这里表示是Computer的对象
        self.computer=com
    def study(self):
        self.computer.open() # 开机
        self.computer.code() # 敲代码
        self.computer.close() # 关机

class Computer():
    def __init__(self,brand,memory): # 品牌和内存
        self.brand=brand  #对象的属性赋值　self.brand是对象的属性,右侧的brand为方法的局部变量
        self.memory=memory
    def open(self):
        print(self.brand,'的计算机正在启动，内存值为:',self.memory)

    def code(self):
        print('正在使用计算机编写代码')

    def close(self):
        print('正在释放内存，计算机正在关闭机')

# 学生使用计算机去学习
#创建测试
#创建计算机类的对象
com=Computer('华为','16GB')
#创建一个学生对象
stu=Student('张三',com)

#学生开始学习
stu.study()
