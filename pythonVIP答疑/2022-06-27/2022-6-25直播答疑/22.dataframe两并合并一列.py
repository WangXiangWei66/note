# coding:utf-8
# author:杨淑娟
import  pandas as pd

df=pd.DataFrame(index=[1],columns=['a','b','c'],data=[['hello','world','java']])
print(df)
print('----------------------')
df=df['a']+df['b']   # a列与b列的值进行合并 ，相加即可

print(df)