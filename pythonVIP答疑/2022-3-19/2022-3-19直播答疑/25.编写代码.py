# coding:utf-8
# author:杨淑娟
#n=eval(input('请输入项数'))
#a=eval(input('请输入数据'))
n=5
a=2
lst=[]
s=0
for i in range(1,n+1):
    lst.append(str(a)*i) # 字符串拼接
print(lst)

for item in lst:
    s+=int(item)  # 再转成int计算
print(s)
