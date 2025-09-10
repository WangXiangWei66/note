# 教育机构：马士兵教育
# 讲    师：杨淑娟

class Student: # 类
    city='石家庄'
    pass

# Student就是类对象
stu=Student()  # stu就是实例对象
print(Student.city) # 类对象调用类属性

def fun():  # 函数
    pass
print(type(Student)) #<class 'type'>
print(type(fun)) #<class 'function'>
# Python中一切皆对象

x=10     # 变量
print(type(x)) #<class 'int'>
print(type(print)) #<class 'builtin_function_or_method'>

if x<100:  #python中的代码块
    print(x)
else:
    x+=10

print('helloworld') #输出语句

 # 创建range类的对象1，10，2传到了__init__的特殊方法
t=range(1,10,2) # 从1开始，到10结束，步长为 2    结果为1，3，5，7，9
print(t) #range(1, 10, 2)
print(type(t))  #<class 'range'> 说明range是一个类
# 要想看到t中具体的数据，可以使用内置函数list()转成列表类型
ls=list(t)
print(ls)




























