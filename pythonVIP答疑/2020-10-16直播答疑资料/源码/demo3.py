#教育机构 ：马士兵教育
#讲    师：杨淑娟
def fac(number):   #number就是要计算的数
    if number==1:   #终止条件
        return 1
    else:  #自己调用自己的情况
        return number*fac(number-1)

print(fac(6))

#兔生兔问题（斐波纳契数列 1,  1,  2,   3,  5, 8,  13 ,21,34,  55,...）
#使用递归计算第7个位置上的数 (这是一个递归，计算数列的)
def fei(index):  #index表示的是第几个位置上
    if index==1 or index==2:    #定义出口条件
        return 1
    else:
        return fei(index-1)+fei(index-2) #自己调用自己
print(fei(7))
print('-----------------------------')
for i in range(1,11):
    print(fei(i),end='\t\t')  #end的含义是 定义print()函数的结束符为\t\t







