# coding:utf-8
# author:杨淑娟
# (1)数据拼接，pd.concat，是pandas级的函数，用来拼接或合并数据，既可横向拼接也可以纵向拼接

import pandas as pd
df1=pd.DataFrame(columns=['姓名','语文成绩'],data=[['张三',76],['李四',80],['王五',87],['陈六',90]])
print(df1)

df2=pd.DataFrame(columns=['姓名','数学成绩'],data=[['张三',98],['李四3',70],['王五3',85],['陈六3',88]])
print(df2)

df3=pd.DataFrame(columns=['姓名','英语成绩'],data=[['麻七1',88],['陈格2',78],['王三3',58],['马六3',85]])
print(df3)
#  横向拼接 （列增加了，行增加了）
df=pd.concat([df1,df2,df3]) # 将df1,df2,df3 三个DataFrame对象，有一个相同的列索引【姓名】
print(df)

# 行叠拼      根据df1重新创建一个DataFrame对象                ，根据df2重新创建一个DataFrame对象
df=pd.concat([pd.DataFrame(df1.values,columns=['姓名','成绩']),pd.DataFrame(df2.values,columns=['姓名','成绩']),
              pd.DataFrame(df3.values,columns=['姓名','成绩'])]) # 根据df3重新创建一个DataFrame对象
 # 这三个DataFrame对象， 列索引 是相同的  （姓名,成绩），列索引相同进行 “行拼”行加，列不增加
 # 就相当于有三个“表结构相同的表格”进行合并
print(df)



# (2)数据并联-pd.merge()   相当于sql中的表连相查询
df=pd.merge(df1,df2,on='姓名') # 内联接
print(df)

# merge既是pandas的方法也是dataFrame的方法
df=df1.merge(df2,on='姓名') # 内联接
print(df)

