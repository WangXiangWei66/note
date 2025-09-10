# coding:utf-8
# author:杨淑娟
# from functools import reduce
# Tn=0
# Sn=[]
# n=int(input('n='))
# a=int(input('a='))
# for j in range(n):
#     Tn=Tn+a
#     a=a*10
#     Sn.append(Tn)
#     print(Tn)
# S=reduce(lambda x,y:x+y,Sn)
# print(S)

n=eval(input('n='))
a=eval(input('a='))
lst=[]
s=''
sum=0
for i in range(1,n+1):
    s=s+str(a)    #字符串拼接放到列表中
    lst.append(s)
print(lst)

for item in lst:
    sum=sum+eval(item)   # 遍历的结果是str字符串，使用eval类型转换，转成实际的数据类型int,然后累加求和

print(sum)