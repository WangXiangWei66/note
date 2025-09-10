# 教育机构：马士兵教育
# 讲    师：杨淑娟
# python一切毕对象，所以列表中存储的是对象的内存地址（列表的底层数据结构是分离式顺序表），
# 散列式的底层数据结构是哈希表
import sys
lst=[11,'hello',33]
print(hex(id(lst))) # 获取列表的内存地址，将内存地址转成址六进制
print(hex(id(lst[0]))) # 获取11的内存地址
print(hex(id(lst[1])))

# 如何查询对象点用内存空间的大小， sys.getsizeof()
print(sys.getsizeof(lst[0])) #11这个整数占用内存空间的大小  28 bytes
print(sys.getsizeof(lst[1])) # hello占用内存空间的大小 54 bytes

print('--------------------------------------------')
# 11这个对象与hello这个对象的内存地址占用了多少内存空间呢？
print(sys.getsizeof(id(lst[0]))) #３２bytes
print(sys.getsizeof(id(lst[1]))) #32bytes

lst2=[] # 空列表 ，底层开辟了一个8个空间的位置用于存储元素