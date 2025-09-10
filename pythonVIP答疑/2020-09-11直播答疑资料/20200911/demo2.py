#教育机构 ：马士兵教育
#讲    师：杨淑娟
#Python中常用的数据结构
#(1)元组的使用
a=1
b=1
print(id(a)) #140719890863776
print(id(b)) #140719890863776
print('------------')
a=(11,22,33)
b=(11,22,33)
print(id(a)) #2811823264000
print(id(b)) #2811823264000

print('-----------列表---------------')
a=[11,22,33]
b=[11,22,33]
print(id(a)) #1956718568640
print(id(b)) #1956718568832

print('-------------集合的set （无序）-------------------')
s=set()   #调用内置函数创建空集合对象
s.add(100)
s.add(20)
print(s)
s.remove(100)
print(s)

print('-------------字典 key-value------------')
d={'name':'张三','age':20,'gender':'男'} #字典使用{}定义
d['score']=90  #增，改
d.pop('score')  #删
print(d)
t=(11,22)
#注意事项 ：  不可变对象可以做为key， 也就是说可变对象是不以作为key的
d[t]=100   #元组t可以作为字典的key ，因为这是不可变对象
print(d)
lst=[11,22,33]
#列表可以作键吗? 不可以，因为它是可变对象
#d[lst]=100 #TypeError: unhashable type: 'list'

'''你学过的Python中的数据类型，哪些是可以作为字典的key的?
   (1)元组 tuple
   (2)字符串 str
   (3)int
   (4)float
   (5)bool类型
'''
d[True]=100
s='hello'
print('---------------------遍历(元组和列表，字符串使用索引遍历)---------------')
for i in range(len(t)): #遍历元素
    print(t[i])
for i in range(len(lst)):
    print(lst[i])
for i in range(len(s)):
    print(s[i])
print('---------------------------')
for i in t:
    print(i)  # i表示的是元组中的对象，而不是索引
for i in lst:
    print(i)
for i in s:
    print(i)



d[98.8]=100
print(d)
print('字典的遍历---------------')
for i in d:
    print(i) #i表示的是字典中的key
print('=============================')

for i in d:
    print(d[i],d.get(i))

for i in d.keys():
    print(i)
for i in d.values():
    print(i)

for i in d:
    print(i,'---->',d.get(i))