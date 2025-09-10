# coding:utf-8
# author:杨淑娟
dict1=dict(aa=12,bb=12,cc=15)
d={}
print('键\t值')
count=0
for item in dict1.keys():
    print(item,dict1[item])
    if dict1[item]==12:
        continue
    d[item]=dict1.get(item)

    count+=1 # 目的是啥？

print(f'总共执行了{count}次，字典d的元素个数:{len(d)}')
print(d)