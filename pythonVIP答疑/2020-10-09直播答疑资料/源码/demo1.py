#教育机构 ：马士兵教育
#讲    师：杨淑娟
import math   #导入一个名称为 math的模块 （Python解释器自带的一个用于数学运算的模块）
#定义一个函数
def getarea(r):   #def用于用声明一个函数（def是声明函数的关键字）  getarea是函数的名称  r函数的参数（形式参数）
    area=math.pi*r*r   #函数体 （用于实现功能的代码）
    return area        #return 用于结束函数，area是一个返回值， 用于提供给调用处使用

#使用函数的过程称为函数的调用,根据函数的名称就可以调用该函数

circl_area=getarea(4)
print('圆的面积的为:',circl_area)
print('----------------上面的求圆的面积的函数称为有名称的函数，下面的代码是Python中没有名称的函数称为匿名函数------------------------------------------')

x=lambda r2:math.pi*r2*r2   #x 的作用是用于调用lambda表达式（调用匿名函数时使用）  r2是匿名函数的参数，   ：之后的内容为函数体
print('圆的面积为:',x(4))


print('-------------根据索引获取列表中每个元素的值--------------------------')
lst=[10,203,4,434,556]
for i in lst:
    print(i)
lst2=['hello','world','java']
for i in lst2:
    print(i)
print('----------------将遍历列表内容的功能编写一个函数--------------------')
def print_lst(args_lst):  #变量的命名规则，要求是字母（中文），数字，下划线，但是不能以数字开头，不能是Python的关键字，如果变量的名称由两个或两个以上的单词组成，要求使用_进行分隔
    for i in args_lst:
        print(i)
print('----------------调用函数遍历列表中的内容-----------------------')
print_lst(lst)
print_lst(lst2)

print('-------------------将遍历函数的过程使用匿名函数--------------------------------')

for i in range(len(lst)):  #range(len(lst))将产生一个 从0开始到 len(lst)的一个整数数据， lst的元素的个数为5，产生一个[0,5）之间的整数序列
    result=lambda index:lst[index]   #index是lambda表达式的参数 (形式参数)
    print(result(i))       #使用result调用匿名函数（lambda表达式）  i lambda的实际参数

print('--------------------字典元素的排序-------------------------------------')
student_score=[{'name':'张三','score':90},
               {'name':'李四','score':100},
               {'name':'王五','score':87}]
#对lst列表进行排序
print('排序之前:',lst)
lst.sort()  #调用lst对象的sort()方法进行排序
print('排序之后',lst)

#student_score列表进行排序
print('排序之前',student_score)  #x表示是lambda的形式参数， 实参是 student_score
student_score.sort(key=lambda x:x['score'])  #sort方法，可以指定一个key function (键函数，而这个键函数使用的是匿名函数)，这个匿名函数将对列表中的每一项应用一次，并对其进行排序
print('排序之后',student_score)

'''
51行代码中的key=lambda x:x['score']   称为一个key  function ， 匿名函数就是一个排序的规则 ，这个规则会对列表中的每个元素执行一次
'''










