# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

print('老师说:\'大家好\'') #引号套引号，要求是英文的
print(type('hello'))
print(type(False))

# Python中一切皆对象，每个对象都有一个布尔值
#在Python中哪些象的布尔值为假False
#0，0.0  ,空字符串，空列表，空元组，空字典，False，空集合,None
print(bool(None))
print(bool('0'))#True

#空字典
#空集合
d={}  #空字典
s=set()#空集合
s2=set({}) #空集合

print(bool(d),type(d))
print(bool(s),type(s))
#print(bool(Null))

# 浮点数的精度问题
#(1)使用round()
print(round(3.1415926,2))  #2 保留2位小数

#(2)使用格式化字符串实现
print('{0:.2f}'.format(3.1415926)) #


