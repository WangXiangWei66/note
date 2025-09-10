# coding:utf-8
# author:杨淑娟
import numpy as np
import pandas as pd
# 二维列表
data=[[100,43,73],[11,18,60],[104,66,54],[30,120,134],[135,77,56],[45,127,63]]

# 列索引
colums=['语文','数学','Python']

# 隐式构造 就是DataFrame构造函数的index参数传递两个或更多的数组
#index是行索引
      # 二维
index=[['Michal','Michal','Kobe','Kobe','James','James'],
       ['Mid','End','Mid','End','Mid','End']]
 # 构造DF对象
df=pd.DataFrame(data,columns=colums,index=index)
print(df)

# 显示构造，使用数组
df1=pd.DataFrame(data=data,index=pd.MultiIndex.from_arrays([['Michal','Michal','Kobe','Kobe','James','James'],
       ['Mid','End','Mid','End','Mid','End']]),columns=colums)
print(df1)

# 显示构造，使用元组
df2=pd.DataFrame(data=data,index=pd.MultiIndex.from_tuples([('Michal','Mid'),('Michal','End'),
                                                            ('Kobe','Mid'),('Kobe','End'),
                                                            ('James','Mid'),('James','End')]),columns=colums)
print(df2)