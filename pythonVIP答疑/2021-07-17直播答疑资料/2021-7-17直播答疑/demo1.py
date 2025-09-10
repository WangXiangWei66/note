#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import pandas as pd
data=[[54,66,89],[65,36,77],[55,98,46]]
name=["zhangsan","lisi","wangwu"]
index=["1001","1005","1103"]
df=pd.DataFrame(data,index=index,columns=name)
print(df)
#print(df.loc[(df["zhangsan"]>60) & (df["wangwu"]>60)]) # 正常输出
#print(df.loc[(df["zhangsan"]>60) and (df["wangwu"]>60)])

print(df['zhangsan']>60) # 判断的结果不是一个值，而是一组值
print(type(df['zhangsan']>60)) #<class 'pandas.core.series.Series'>

print(1 and 2 ) # 2
print(1 & 2)  # 0

# python中判断条件时使用 and  ,pandas中 使用&
print(2>1 and 4>3) # True
print(df.loc[(df["zhangsan"]>60) & (df["wangwu"]>60)]) #



