#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 介绍一下Series ，DataFrame, Panel
# Panel 最新的版本已经把Panel移除了
# Series与DataFrame 是pandas中的非常重要的两个数据类型
# Series相当于一维数组
# DataFrame 相当于二维数组
import  pandas as pd # 第三方模块，用于数据分析
s=pd.Series([10,30,40,43]) # [10,30,40,43]
print(s)
print(type(s))
print('----------------------------------------')
df=pd.DataFrame(
    [
        ['张三',90,98,67],
        ['李四',100,97,76],
        ['王五',67,54,89],
        ['陈六', 34, 87, 83]
    ],
    columns=['姓名','语文','数学','英语']
)

print(df)
print(type(df))
# 将DataFrame数据存储到Excel中
df.to_excel('学生.xlsx',index=False)
