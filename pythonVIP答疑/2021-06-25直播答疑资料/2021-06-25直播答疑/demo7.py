# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 操作Excel文件pandas最方便
import  pandas as pd   #pands是专门用于处理数据分析的模块
df=pd.read_excel('成绩表.xlsx',sheet_name='Sheet1') # 读取Excel文件中的名称为Sheet1的表
#print(df)

#排序， 按照数学成绩降序排序
new_df=df.sort_values(by='数学',ascending=False) # ascending=False降序,ascending=True升序
print(new_df)
