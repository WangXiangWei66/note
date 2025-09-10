# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import  pandas as pd
df1=pd.read_excel('student1.xlsx')
df2=pd.read_excel('student2.xlsx')
print(df1)
print(df2)
print('----------内连接操作----------')
new_df=pd.merge(df1,df2,on='编号')
print(new_df)

print('-------左外连接合并------')
new_df=pd.merge(df1,df2,how='left')  # how 就是关键字参数
print(new_df)

print('-------右外连接合并------')
new_df=pd.merge(df1,df2,how='right')
print(new_df)