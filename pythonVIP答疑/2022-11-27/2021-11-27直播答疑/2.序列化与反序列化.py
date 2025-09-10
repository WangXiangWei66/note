# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import pickle #内置的，不用安装，导入就可以使用
#序列化的两个方法，dump () 序列化并存储 ,  dumps() 只序列化，不存储
data={'k1':'python','k2':'java'} # 字典

#对字典对象进行序列化
x=pickle.dumps(data)  #将dict转成了bytes类型
print(x,type(x)) #<class 'bytes'>


# 对应的就是反序列化
data2=pickle.loads(x)  #将ｂｙｔｅｓ类型转成了ｄｉｃｔ类型　
print(data2,type(data2)) # <class 'dict'>

print('---------想将序列化的数据进行磁盘存储怎么办？---------------------------')
#
#with open('a.txt','wb') as file:
    #file.write(x) #TypeError: write() argument must be str, not bytes
# 为什么使用with, 被称为上下文管理器，有了with,无需手动close()


#使用另外一对方法，dump() 和load()
file=open('aa.txt','wb') #创建一个文件对象
pickle.dump(data,file)
file.close() #由于没有使用with,所以需要手动关闭文件流

#反序列化回来
with open('a.txt','rb') as file:
    print(file.read())  # 读取的结果是一个字节数据

print(pickle.load(open('aa.txt','rb'))) #使用的load() 反序列化，并从文件中进行读取


print('------------------使用json模块如何完成-----------------------------')
import json
#进行序列化，保存
json.dump({'姓名':'张三'},open('b.txt','w'))

# 读取并反序列化
print(json.load(open('b.txt','r')))

print('只序列与反序列，不想保存到磁盘上，使用带s的方法')

x=json.dumps({'姓名':'张三'},ensure_ascii=False) # dict-->str
print(x,type(x)) #<class 'str'>


# 反序列化，  将str-->dict类型
y=json.loads(x)
print(y,type(y)) #<class 'dict'>

#总结   pickle的dumps（）将  转成bytes类型
#       json的dumps()  转成str类型
#　　　　pickle的loads()  将bytes转成实际的类型
#　　　　json.loads()将str转成实际的数据类型

