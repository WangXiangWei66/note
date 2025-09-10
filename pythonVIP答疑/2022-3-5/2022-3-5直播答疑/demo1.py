# coding:utf-8
# author:杨淑娟
print(1) # int类型，整数
print(1.) # float类型
print(1.,'hello') #  这个.  当成了浮点数的点
print('1.','hello') # 这个1. 表示的是序号 排序的意思，所以是字符串，
print('''---------------eval函数的使用--------------------''')
helloworld='一起向未来'
x=eval(input('请输入一个数:'))#  没有加eval的时候x的数据类型是str
print(type(x))  # ‘helloworld’  ，去除字符串的引号  helloworld    这被看作是Python中的变量
print(x)