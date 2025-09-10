#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
#　DataFrame类型是pandas模块中非常重要的数据类型，还有一个非常重要数据类型Series
#Series相当于一维数组,DataFrame 相当于二维数组
import random
import  pandas as pd   #　第三方模块，需要安装
lst=[random.random()for i in range(10)] # 一维列表
#print(lst)
df=pd.DataFrame(data=lst,columns=['随机数'],index=['第'+str(i)+'行'for i in range(1,11)]) #是一个类class ，这句代码的意思是创建DataFrame的对象
                # 在创建对象时需要提供一些参数 data,columns 列索引 ，index行索引
                # 这个DataFrame是一个多行1列的
print(df)
print(type(df))
