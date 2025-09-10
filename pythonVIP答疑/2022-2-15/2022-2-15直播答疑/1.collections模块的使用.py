# coding:utf-8
# author:杨淑娟
import  collections as c
count=c.Counter() # 创建对象 Counter是什么数据类型呢？  对列表中元素进行个数统计
lst=list('helloworld') # 创建一个列表对象
#遍历
for item in lst:
    count[item]+=1 # 个数+1
print(count)


#从文本中读取内容，统计个数
# open('hamlet.txt').read().lower() 从文件中读取数据，全部转成小写,结果是一个字符串类型
import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
print(c.Counter(words).most_common(10))

print('------------------双端队列-(跟list比较像)-------------------')
# 创建队列对象
q=c.deque('hello')
print(q)  # 显示队列中的元素
q.append('java') # 向队尾（右侧）添加元素

print(q)
q.appendleft('html') # 向队列的左侧添加元素
print(q)

q.extend(['python','mysql']) # 解包添加到右侧
print(q)

q.extendleft(['red','blue','orange']) # 解包添加到左侧
print(q)

print(q.pop()) # 从右删除
print(q.popleft()) # 从左删除
print(q)
