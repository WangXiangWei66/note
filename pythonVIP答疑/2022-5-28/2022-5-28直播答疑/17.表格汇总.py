# coding:utf-8
# author:杨淑娟
import pandas as pd
df1=pd.read_excel('student.xlsx',sheet_name='Sheet1') # 读取第一个Sheet
df2=pd.read_excel('student.xlsx',sheet_name='Sheet2') # 读取第二个Sheet

df=pd.DataFrame()  # 创建一个空的DataFrame对象
df=pd.concat([df1,df2]) # 拼接Sheet1与Sheet2
print(df)
