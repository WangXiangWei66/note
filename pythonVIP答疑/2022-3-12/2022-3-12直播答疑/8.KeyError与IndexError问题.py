# coding:utf-8
# author:杨淑娟
d={'age':20,'name':'marry','gender':'男'}
#从字典中取值的方式有两种，(1)使用[] ，（2）使用字典对象的get()方法
#print(d['score']) # 在字典中有key为score的吗？没有吧，所以报错keyerror
# 如何避免KeyError的错误，使用get()
print(d.get('score'))  # 获取元素
print('获取字典中元素的个数使用len:',len(d))

lst=[10,20,30,40]
# 列表的索引 范围，[0,N-1] ,  逆向索引[-N,-1]
# 如何避免IndexError ,可以使用判断  如果   获取的索引在 0到len(lst)-1之间即可避免报IndexError异常
print('获取列表中元素的个数：',len(lst))
