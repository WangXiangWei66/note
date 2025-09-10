# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
def fun(name):  #外层函数
    def inner_fun(age): # 内层函数
        print('name:',name,'age:',age)
    return  inner_fun  #返回的是一个函数对象

# 调用
obj=fun('张三')  # fun的返回结果是inner_fun是一个函数对象，所以obj就是那个内层的函数

#调用内层函数,并传参
obj(20)

