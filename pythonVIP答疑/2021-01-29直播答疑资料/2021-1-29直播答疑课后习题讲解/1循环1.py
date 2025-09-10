# 教育机构：马士兵教育
# 讲    师：杨淑娟
'''
循环分两类
1）遍历循环  for...in
2）无限循环  while
'''
#1. 使用for
for i in range(97,123):  # range(start,end)    [start,end)
    print(chr(i),'--->',i)  #chr() ,ord()

#print(chr(97)) #a    chr将unicode值转成对应的字符

print('----------------------------------')
# 2.while循环
x=97
while x<123:
    print(chr(x),'--->',x)
    x+=1  #每次累加1

print('----------------------------------')
#3.使用无限循环，使用break去控制
y=97
while True :   # while 2
    print(chr(y),'-->',y)
    y+=1
    if y==123:
        break

'''
 Python一切皆对象，每个对象都有一个布尔值
 0 --》False，  非0的布尔值为True
 
'''
