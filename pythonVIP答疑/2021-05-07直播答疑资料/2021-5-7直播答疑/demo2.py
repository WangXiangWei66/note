# 教育机构：马士兵教育
# 讲    师：杨淑娟

# 9.将数据提取到同一个工作簿新的sheet表中的index是错乱的怎么重新设置？
import pandas as pd
#创建一个DataFrame对象
data=[39,53,45,67,23,44]
       #data=data是关键字参数赋值，左边的data是DataFrame（）方法定义时的参数名称,
       # 右边的data是自己起的变量名
df=pd.DataFrame(data=data,columns=['年龄']) # columns列索引，相当于表格的表头
print(df) # 0,1,2,3,4,5 称为行索引 ，相当于有6行一列的表格
# 对年龄这列的数据进行排序
df=df.sort_values(by='年龄').reset_index(drop=True) #重新设置索引，并将原索引删除
# 将数据保存到Excel文件
df.to_excel('a.xlsx',index=False) # 将DataFrame数据导出到Excel时，不保留行索引，加入参数index=False
print(df)
