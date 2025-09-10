# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

#列表是可变数据类型
lst=[10,20,30]
print(id(lst))
lst.append(40)
print(id(lst))
print('-------内存地址不变，元素的个数可以改变，可变数据类型------------------')

#字符串是不可变的
s='hello'
print(id(s))
#s[0]='J'
s=s.replace('h','J')
print(id(s))
print('内存地址发生了更改，说明产生了新对象，对原对象没有办法修改，所以是不可变数据类型')

d={'hello':'world',(19,20):'java',10:[10,203,4]}  #元组可以作键，但是列表不行，值可以是任意类型
print(d)