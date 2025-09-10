# coding:utf-8
# author:杨淑娟
import pandas as pd
import re  # 内置模块re用于处理正则表达式
lst=[[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]] # 二维列表
index=[1,2,3,4]   # 列表，  index ,行索引
columns=['我们','我和你','你','他']  # 列索引
df=pd.DataFrame(lst,index=index,columns=columns) # 创建DataFrame对象
print(df)
x=[]  # 创建一个空列表， 准备存储要删除的列索引
for item in columns:  # 遍历列索引
    match=re.match('我.*',item)   # 使用正则，匹配出所有的与 ‘我’有关的match对象
    if match!=None:
        x.append(match.group())  # 将匹配到的与“我”有关的列索引存储到列表中
print(x)
# 删除从df 中columns中将x 中的列索引全部删除
df=df.drop(columns=x)
print(df)