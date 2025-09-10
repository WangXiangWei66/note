# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import  pandas as pd
df=pd.read_excel('my.xlsx',sheet_name='Sheet1')

df2=pd.read_excel('my.xlsx',sheet_name='Sheet2')

print(df)
print('-----------------------')
print(df2)
