# 教育机构：马士兵教育
# 讲    师：杨淑娟

import  pandas as pd
result=pd.DataFrame()
df1=pd.read_excel('a.xlsx',sheet_name='Sheet1')
#print(df1)
df2=pd.read_excel('b.xlsx',sheet_name='Sheet1')
#print(df2)
#print(df1+df2)  # 合并后累加

result=pd.concat([result,df1]) # 加df1
result=pd.concat([result,df2]) #加ｄｆ２
#print(result.reset_index(drop=True)) # 两个工作表相加合并之后的结果

# 把未成年人提取出来，存储到Excel文件中
result=result.reset_index(drop=True) # 重置索引
newdf=result.loc[result['年龄']<18].reset_index(drop=True)
# 存储到Excel文件中
newdf.to_excel('c.xlsx',index=False)
print(newdf)
