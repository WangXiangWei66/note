#教育机构 ：马士兵教育
#讲    师：杨淑娟
# 列表的切片操作
lst=[11,22,33,44,55,66]
# 切片的三个参数[start:stop:step]

# 切片之后将产生一个新的列表
lst1=lst[::-1] # 倒序 start采用默认值  列表中最后一个元素  ,  stop 采用了默认值 第一个元素 , step 步长为 -1

print(lst1)

print('普通的增，删，改操作')
lst.append(77)   # 在列表的末尾 添加一个元素 77

lst.remove(66)  # 删除66

lst[0]=100 # 修改

lst.insert(0,200) #在索引为0的位置上插入200
print(lst)

lst2=[99,88,10]
print(lst)

lst3=lst+lst2  # 为什么可以执行"+"的操作啊
#print(lst3)
print(lst.__add__(lst2))  # 与lst+lst2的结果相同     因为后面会讲到面向对象 的类与对象

