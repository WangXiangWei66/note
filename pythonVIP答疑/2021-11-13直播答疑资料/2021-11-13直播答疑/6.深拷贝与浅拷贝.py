# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 浅拷贝拷一层
import copy
lst1=[10,20,[40,50]]  # 这个列表有3个元素，两个int类型，为不可变对象，一个为列表类型[40,50]，是可变对象
# # 执行浅拷贝操作
# lst2=copy.copy(lst1)
# print('lst1=',id(lst1)) #2433777987456
# print('lst2=',id(lst2)) #2433778016320
# print('lst1=',lst1)
# print('lst2=',lst2)
# print('不可变对象，无论是深拷贝还是浅拷贝，都不会发生拷贝')
# print('lst1中的子列表=',id(lst1[2])) #  2231171541888
# print('lst2中的子列表=',id(lst2[2])) #2231171541888
# # 如果对子列表中的元素进行更改，二者均产生变化lst1,与lst2
# lst1[2].append(100)
# print('lst1=',lst1)
# print('lst2=',lst2)
# 深拷贝拷多层

lst2=copy.deepcopy(lst1)
print('lst1=',id(lst1)) #2074390102656
print('lst2=',id(lst2)) #2074390102784
print('lst1=',lst1)
print('lst2=',lst2)
print('不可变对象，无论是深拷贝还是浅拷贝，都不会发生拷贝')
print('lst1中的子列表=',id(lst1[2])) # 2074390097344
print('lst2中的子列表=',id(lst2[2])) #2074390102720
# 如果对子列表中的元素进行更改，另外一个不产生变化
lst1[2].append(100)
print('lst1=',lst1)
print('lst2=',lst2)
