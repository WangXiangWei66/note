# coding:utf-8
# Author: Wu Xiaofeng
# Data: 2022/6/24 13:42
import pandas as pd
import os
import numpy as np
file_path=r'1653-17.txt'
data = pd.read_csv(file_path, delim_whitespace=True, encoding='gbk')

df2 = pd.DataFrame(np.insert(data.values, 0, values=[1,2,3,4], axis=0))

# define column names of DataFrame
df2.columns = df2.columns

#view updated DataFrame


data.to_excel('./测试结果.xlsx',
                 sheet_name='合格数据',
                 index=False)
# df2.to_excel('./测试结果1.xlsx',
#                  sheet_name='合格数据',
#                  index=False)