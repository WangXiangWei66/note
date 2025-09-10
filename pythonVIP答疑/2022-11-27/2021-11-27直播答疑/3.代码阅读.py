# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

lst=[1,10,2,3,3,3,2,5,2,1]  #
# while True:
#     for item in lst:
#         if lst.count(item)>1:
#             lst.remove(item)
#     break  #加了ｂｒｅａｋ退出while循环,但是功能没实现
# print(lst)
#列表元素的去重
#(1)
new_lst=[]
for item in lst:
    if item not in new_lst: # 结果item不在新列表中，则添入
        new_lst.append(item)
print(new_lst)


# （2）通过集合去重
s=set(lst)  # set的特点是无序的
#print(list(s))
lst2=list(s)
# 如何使用set，依然有序
lst2.sort(key=lst.index)  # 加了一句排序
print(lst2)