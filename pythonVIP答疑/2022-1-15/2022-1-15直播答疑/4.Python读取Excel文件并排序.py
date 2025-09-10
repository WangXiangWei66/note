# coding:utf-8
# author:杨淑娟
import pandas as pd # 这是一个第三方模块 pip install pandas
df=pd.read_excel('score.xlsx') # 结果是一个DataFrame类型 ，score.xlsx是Excel的文件名
#print(df)

#排序
#df.sort_values(by='语文',inplace=True,ascending=True) # 升序
df.sort_values(by='语文',inplace=True,ascending=False) #降序
print(df)

df.to_excel('d:/a.xlsx',index=False) # 排序之后的结果进行了保存
