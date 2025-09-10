#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

x=3 #全局变量

def changed():
    global x  # 在
    x=5
    return x # 函数中修改全局变量的值时，你需要使用到global

print(changed()) # 5
print(x) # 全局 变量

y=10
def fun():
    print(y)

fun()

print('----------------------------------')
lst=[90]

def fun2():  # lst为什么不需加上global关键字呢？因为函数内，函数外lst的地址没有更改
    lst.append(10)
    lst.append(20) # 请问，是不是修改lst的值？
    print(lst)
fun2()
print(lst)


lst2=[90,10]
def fun3():
    lst2=[100,300]
    lst2.append(1000)
    print('--------',lst2)  # lst2是局部变量
fun3()
print(lst2)

print('---------------------------------')
