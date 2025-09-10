# coding:utf-8
# author:杨淑娟
# s=eval(input('请输入一个数据:')) #
# print(type(s))

lst=[10,20,30,40,50]
for item in lst:
    print(item)
print('---------------上述代码是正常遍历列表元素--------------------------')
for index,item in enumerate(lst,start=110): # 序号默认从0开始，当前这个循环中的index是从10开始，index是序号，不是索引， 这个序号的开始值，可以自由指定，
    print(index,'--->',item)