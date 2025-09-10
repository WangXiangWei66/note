# coding:utf-8
# author:杨淑娟

# 替换，  使用列表2中的元素替换列表1中的能被3和5整数的数
def replace_order(lst1,lst2):
    j=0
    for i in range(len(lst1)):
        if i%3==0 or i%5==0:
            # while True:
            lst1[i]=lst2[j]
            j+=1
            if j==len(lst2):
                j=0
            # break
    print(lst1)

l1=list(range(40))  # 产生一个0到39的整数
l2=["java","python","c++","c#","cpp"] # 这个列表中的内容是啥都行

# 函数的功能，是把l1列表中能被3 或5整数的数使用l2中的元素进行替换
replace_order(l1,l2)