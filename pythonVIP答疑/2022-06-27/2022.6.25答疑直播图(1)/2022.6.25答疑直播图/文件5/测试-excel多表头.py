# coding:utf-8
# Author: Wu Xiaofeng
# Data: 2022/6/24 13:42
import pandas as pd
import os
file_path=r'E:\工作中项目\ADVA数据整理项目\ADVAproject1\脉冲测试\脉冲数据 - 副本\1653-17.txt'
data = pd.read_csv(file_path, delim_whitespace=True, encoding='gbk')

data.to_excel('./测试结果.xlsx',
                 sheet_name='合格数据',
                 index=False)