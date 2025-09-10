# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 1月23日，星期六，晚8:00肖老师直播答疑【正则，线程，网络编程】
for   i in range(5):
    print('A -------------------------') #缩进层次相同的为并列关系
    if i<3:
        print('C----------------') #C 是if中的
    print('B -------------------------')

# for与print是嵌套关系，  for循环中嵌套了print
print(100)                 #-->
print(100,'hello')         #-->
print(100,'hello','world') #-->以上三个都与print函数中的 *args参数有关
print('--------------------------------------')
# 自定义函数，要求参数是个数可以变的位置形参
def fun(*args):
    print(args)  #结果是一个元组类型

fun(100)
fun(100,'hello')
fun(100,'hello','world')


#总结
def fun2(*args,**kwargs):  #第一个是个数可变的位置形参，第二个是个数可变的关键字形参
    print(args)   #输出结果是一个元组
    print(kwargs) #输出是一个字典

fun2(1,2,3,a=11,b=22)

class A():
    def show(self):
        print('A')
class B():
    def show(self):
        print(B)
class C (A,B):  #优先级别，，A高于B
    pass

c=C()
c.show()




