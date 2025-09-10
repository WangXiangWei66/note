#教育机构 ：马士兵教育
#讲    师：杨淑娟
# Python中一切皆对象
a=10
b=10
c=10
print(id(a),type(a),a)
print(id(b),type(b),b)
print(id(c),type(c),c)
print('-'*50)
lst1 = [11,22,33]  #列表
lst2=[11,22,33]  #列表
lst3=lst1  # 说白了，这是赋值，将lst1的地址（引用）赋给了lst3
print(id(lst1),type(lst1),lst1)
print(id(lst2),type(lst2),lst2)
print(id(lst3),type(lst3),lst3)
print(id(11),id(22),id(33))