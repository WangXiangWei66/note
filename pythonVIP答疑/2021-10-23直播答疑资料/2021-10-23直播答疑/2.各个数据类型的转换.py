# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

#int, float,bool,str,list,元组，字典类型
a=100
str_a=str(a)  #使用内置的str函数   int--->str
print(str_a,type(str_a))

int_a=int("123") #　str－－＞ｉｎｔ ,str要求是数字串
print(int_a,type(int_a))

#float与str之间转换，使用内置的float()函数进行

#int与float之间进行转换，使用的是内置的int()与float()函数

#int与bool之间进行转换,使用是内置的int()和bool()函数
a=98
b=0
bool_a=bool(a)
print(bool_a,type(bool_a)) # 98转成布尔类型为True
print(bool(b),type(bool(b))) #0转成布尔类型为False
#在Python中万物皆对象，每个对象都有一个布尔值，0的布尔值为False，非零的布尔值为True
print(int(True),int(False))

# str与list之间的转换
s='helloworld'
#把str转成列表list，使用的是内置的list函数
lst=list(s)
print(lst)
#将str转成了元组tuple
t=tuple(s)
print(t)
#列表和元组怎么转成str
s1=''.join(lst)
s2=''.join(t)
print(s1)
print(s2)


# 列表中的字符串“字典”
lst=[
    "{'name':'张三','age':20,'gender':'男'}",
    "{'name':'李四','age':30,'gender':'女'}"
]
#如保把列表中的字符串转成字典
for item in lst:  #item在这，是一个迭代变量
    d=dict(eval(item)) # 将字符串转成字典类型【要求是字典格式的字符串】
    print(d,type(d))
#列表可以作为 字典中的“值”，但是不能做“键”，字典中的键要求是不可变对象,str,tuple,int..

d={'name':'张三','score':[90,89,98,76,90]}  # 列表作值
#遍历张三的成绩
for item in d['score']:
    print(item)
