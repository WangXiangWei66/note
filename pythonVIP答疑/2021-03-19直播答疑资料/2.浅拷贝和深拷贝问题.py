# 教育机构：马士兵教育
# 讲    师：杨淑娟
#　不可变对象都不会产生拷贝（整数，字符串，元组等）
# 浅拷贝
# 列表的切片的操作产生浅拷贝 （外壳变了，心没变）
lst=[11,22,[44,6],88] # lst列表中有4个元素，其中三个是不可变对象，嵌套列表[44,6]是可变对象
# 切片操作 ，将产生新的 列表对象
lst2=lst[::] # 切片操作与赋值操作是相同的？不相同
lst3=lst   # 在赋值 的过程中没有产生新的对象，就没有发生拷贝
print(lst,id(lst))
print(lst2,id(lst2))
print(lst3,id(lst3)) # lst3与lst 地址相同
lst[0]=100
print(lst)
print(lst2) # 不变的
print(lst3)
print('------------------------------copy模块中的copy方法')
import copy
lst4=copy.copy(lst) # 浅拷贝
print(lst,id(lst))
print(lst4,id(lst4))
print('----------------深拷贝是外壳变，心也变--------------------------------')
lst5=copy.deepcopy(lst) # deep单词表示的是深的意思
print(lst,id(lst))
print(lst5,id(lst5)) # 100，200，88是不可变对象
print(id(lst[0])) # 100
print(id(lst5[0])) # 100   因为100是整数 ，属于不可变量对象，不可变对象不会发和拷贝
print(id(lst[2])) # [44,6]  列表，列表是可变对象
print(id(lst5[2])) #　２８，２９行代码中ｉｄ的值不相等，说明“心”也进行了拷贝
#lst6=[100,22,[44,6],88] # 一个新的列表对象


