# coding:utf-8
# author:杨淑娟
# 在Python中 没有方法重载的概念，（方法重载是Java的概念），可以存在同名的方法，后编写的方法会将前面编写的方法进行覆盖

class Worker():
    #初始化方法 ，给对象的实例属性赋初值,只能有一个
    def __init__(s,name,age): # name,age叫方法的局部变量
        s.worker_name=name  # s.worker_name 是类的实例属性
        s.worker_age=age   # s.worker_age是类的实例属性

    #self是实例方法的第一个参数，参数的名称可以自定义，只不过大家习惯叫self,写s可以不？当然可以
    def show(s):
        print(s.worker_name,s.worker_age)
#w=Worker()  # 在去创建这个类的实例对象时，这句代码是错的，因为在创建类的实例对象时，会自动调用__init__方法
             # 而__init__有两个参数 ，name,age 要求调用时传入,s不需要手动传入

w=Worker('杨老师',18)
w.show()
