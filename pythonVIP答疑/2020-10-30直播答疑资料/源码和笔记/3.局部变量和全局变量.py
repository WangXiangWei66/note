# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
x=100   #  全局变量，可以在任意的函数中使用

def fun():  # def是用于声明函数的关键字

    print(x)   # 输出全局变量x的值


fun() #函数的调用
x=200
fun() #再次调用fun函数

def fun2():
    y=34   # y就是函数中的局变量 ,只能在函数体中使用，出了函数体，就不能使用了
    print(y)
fun2()
#  print(y) #NameError: name 'y' is not defined

# 怎样将局部变量升级为全局变量
def fun3():
    global  z  #使用global 关键字，将z声明为全局变量
    z = 300
    print(z)
fun3()
print(z)

def fun4():
    x=500
    print(x)

fun4()  # 500
print(x) # 200