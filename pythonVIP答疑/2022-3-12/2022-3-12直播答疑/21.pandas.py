# coding:utf-8
# author:杨淑娟
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[['张三',45,65,100],['李四',56,45,50],['王五',67,67,76]]

index=[i for i in range(3)] # 行索引

columns=['姓名','语文','数学','英语']  # 列索引

 # 创建DataFrame对象
df=pd.DataFrame(data=data,index=index,columns=columns)

print(df)
# 追加 ，行的增加
df=df.append({'姓名':'三三','语文':20,'数学':30,'英语':30},ignore_index=True)
print(df)
# 插入
# 新增一列
df['政治']=[20,30,30,40]
print(df)
# 在指定位置 上插入一列数据
df.insert(1,'历史',[30,50,60,70])
print(df)

# 如果非得在在指定行插入一行数据， 操作方法，可以使用 切片， 切两片，   第一片  +  插入的数据  + 第二片 ，实际上concat拼接