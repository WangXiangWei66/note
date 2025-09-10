# coding:utf-8
# author:杨淑娟
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[[98,28,56,100],[78,43,93,100],[56,95,85,100]]
index=['张三','李四','王五']
columns=['语文','数学','英语','体育']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)

df.drop(df[df['数学']<60].index,inplace=True )
print(df)