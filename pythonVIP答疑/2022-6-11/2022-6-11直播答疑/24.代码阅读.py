# coding:utf-8
# author:杨淑娟
f=open('test.txt','r',encoding='gbk')
count=0
for line in f:
    if count==2:
        print('葡萄')
        count+=1
        continue
    count+=1
    print(line.strip())
f.close()