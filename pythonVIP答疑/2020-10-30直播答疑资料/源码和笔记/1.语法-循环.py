# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
#（1）遍历 列表 -->for...in
lst=[11,22,33,44]
for  item in lst:
    print(item,end='\t')
print('\n-----------------------------------')
for index in range(0,len(lst)):

    print(lst[index],end='\t')
# （2）遍历元组  -->for...in
print('\n-----------------------------------')
t=(11,22,33,44)
for item in t:
    print(item,end='\t')
# (3)遍历字典  -->for...in
print('\n-----------------------------------')
d={'name':'张三','age':20,'gender':'男'}
for item in d.keys():   # 遍历字典中的键
    print(item,end='\t')
print('\n-----------------------------------')
for item in d.values():  # 遍历字典中的值
    print(item,end='\t')
print('\n-----------------------------------')
for item in d.items(): #遍历字典中的key-value对，结果是一个元组类型
    print(item,end='\t')

#（４）遍历集合　　for...in
print('\n-----------------------------------')
s={'hello','python','html','sql','java'}
for item in s:
    print(item,end='\t')
print('\n-----------------------------------')
#（5） 遍历字符序列  for...in
s1='hello,python'
for item in s1:
    print(item,end='\t')

''' while 循环 ,通常   “确定吗？继续吗？” 与两个关键字一起使用,break,continue,通常与if判断在一起'''
print('\n------------------------------------')
while True:  #True 表示的是条件表达式的判断结果，通常与if,break，一起使用，用于退出循环结构
    x=input('请猜一下杨老师的年龄:')
    if x=='18':
        print('猜对了!!!^_^')
        break


print('\n------------------------------------')
a=1
while a<10:  #ａ<10 条件表达式， 这个条件表达式的结果可能是True，也可能是False
    print(a)
    a+=1   # 每循环一次，都要改变一下变量a的值，a在这里是计数器

print('================',a)

