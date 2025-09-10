# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
# s=eval(input('请输入数据啊'))
# print(s,type(s))


lst=[11,22,33]
lst2=[55,66,77,88]
#lst.append(lst2)
#lst.insert(1,lst2)    1就是元素要插入的位置

# lst.extend(lst2)
# print(lst)
# print(len(lst))
# lst.insert(1,lst2[0])
# print(lst)

def fun(lst):  #计算列表中最大值的索引
    max=0
    max_index=0
    for index in range(len(lst)):
        if lst[index]>max:
            max=lst[index]
            max_index=index
    return  max_index


print(lst)
print(fun(lst))  #最大值的索引是2
lst.insert(2,lst2[0]) #将列表2中索引为0的位置上的元素添加到了最大值这前
print(lst)
