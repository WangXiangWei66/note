# coding:utf-8
# author:杨淑娟
lst=[10,203,54] # 列表
print(lst[0]) # 根据索引取值

t=(10,30,405,90) # 元组
print(t[0]) # 元组取值

d={0:'hello',1:'world',2:'python'}
print(d[0]) # 字典取值
print(d.get(2)) # 会输出python  ,只能根据key获取value


s='helloworld'
print(s[0]) # 字符串取值

# 集合可以遍历取值不可以使用[]


s={'hello','world','python'} # 集合
print(s,type(s))
lst2=list(s)
print(lst2[0])

#lst2就是列表
s="".join(lst2)
print(s,type(s))

#keys方法是取出字典中所有的key
print(list(d.keys())) # 将字典中所有的key都取出来的，转成列表类型
