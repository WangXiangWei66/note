# coding:utf-8
# author:杨淑娟

import  pandas as pd
df=pd.read_excel('工作簿去重.xlsx')
print(df)

df=df.drop_duplicates() # 去掉表格中的重复数据
print(df)