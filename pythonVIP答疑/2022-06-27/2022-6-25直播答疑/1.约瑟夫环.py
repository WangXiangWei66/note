# coding:utf-8
# author:杨淑娟
'''一.问题描述

有n个人围成一圈(编号为1~n），从第1号开始进行1、2、3报数，凡报3者就退出，下一个人又从1开始报数......直到最后只剩下一个人为止。
输入整数n，请问最后剩下者原来的位置是多少号？例如，输入10，则输出4。

二.思路分析

n个人进行报数，报数方式为1、2、3，报到3的人退出，之后的人继续进行1、2、3报数，可以把报1、2的人报数之后，放到末尾，这样就把第一个人(报3)删掉，之后继续把报1、2的人放到末尾，继续删掉第一个人，直到剩下最后一人。
'''
n=int(input('请输入总人数:'))                   #输入总人数
a=list(i for i in range(1,n+1)) # 由N个数组成的列表
while True:
    a.append(a[0])
    a.append(a[1])               #总把前两个人放到后面
    a.pop(0)
    a.pop(0)
    a.pop(0)                     #总把前三个人删掉
    if len(a)==1:                #当人数为1，输出编号
        break



print(a)




def josephus(n,k):
     # n代表总人数，K代表报数的数字
      List = list(range(1,n+1))
      index = 0
      while List:
          temp = List.pop(0)
          index += 1
          if index == k:
              index = 0
              continue
          List.append(temp)
          if len(List) == 1:
            print(List)
            break
if __name__ == '__main__':
   josephus(10,3)
