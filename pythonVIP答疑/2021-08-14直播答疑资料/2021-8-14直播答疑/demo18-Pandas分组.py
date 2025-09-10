# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import  pandas as pd
df=pd.read_excel('测试.xlsx')
# 分组统计

df1=df.groupby(df['关键字']).size()
print(df1)