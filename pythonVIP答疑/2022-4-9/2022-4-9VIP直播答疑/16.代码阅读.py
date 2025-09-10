# coding:utf-8
# author:杨淑娟

a=10
b=20
a,b=b,a  #解包赋值 ，b的值 赋给了a,把a的值赋给了b
print(a,b)

lst_1=[3,2,5,7,8,1,5]

#先看= 右侧的代码  ， 等号右侧的代码有两句，中间使用 逗号分隔
# 先查最里层，再看最外层
print(min(lst_1)) #找到列表中的最小值  1
print(lst_1.index(min(lst_1))) # 最小值的索引是5
#获取最小值
print(lst_1[lst_1.index(min(lst_1))])  #在列表中获取了最小值


#将最小值与最后一个元素进行交换
#lst_1[-1],lst_1[5]=lst_1[5],lst_1[-1]
lst_1[-1],lst_1[lst_1.index(min(lst_1))] =lst_1[lst_1.index(min(lst_1))],lst_1[-1]
print(lst_1)

#下一句代码是将最大值最第一个元素进行交换  (最大值没有交换成功)
print('最大值的索引：',lst_1.index(max(lst_1)))
#lst_1[0],lst_1[lst_1.index(max(lst_1))] =lst_1[lst_1.index(max(lst_1))],lst_1[0] # 这样写换不成功
#这样写换成功了
#lst_1[0],lst_1[4] =lst_1[lst_1.index(max(lst_1))],lst_1[0]
print(lst_1)

#为什么？在列表中交换元素的时候， 找到这个值，可以与这个值之后的任何交换，但是不能与这个值之前的交换
# 因为最大值的索引是4， 可以与索引4之后的任何值交换，但是不能与索引4之前的值交换
lst_1[-4],lst_1[lst_1.index(max(lst_1))] =lst_1[lst_1.index(max(lst_1))],lst_1[-4]
print(lst_1)