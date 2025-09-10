# coding:utf-8
# author:杨淑娟

def quit():
    print('quit函数')

def insert(s):
    print('s的值为:',s)

def search():
    return '我是查询函数'


#使用这三个函数 作为字典中的值  def是Python中一关键 字，用于定义函数

d={0:quit,1:insert,2:search}  # 函数 作为字典中的值， 不能加括号，因为加上括号quit()就是函数 的调用

#字典取值
d.get(0)() # 获取key0的值 ,获取到的值是一个函数 就可以直接调用 ,就是调用quit()

#带参数的调用
d[1]('helloworld')  # 实际上就是在调用insert函数

#调用带返回值的
print(d[2]()) # 这个就是在调用 search函数
print(d.get(2)()) # 也是在调用 search函数