#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import pandas as pd
import  random
index=pd.date_range('2021-1-1',periods=15,freq='D') #产生一个从2021-1-1到2021-1-15 ,每次增加一天 Day
#构建一个Ｓｅｒｉｅｓ对象
s=pd.Series([random.randint(1,100)for i in range(15)],index=index)
print(s)
print(type(s))
print('------------------------------')
# ss=s.rolling(3).mean()  #移动窗口计算 平均值#
# print(ss)

# expanding()征用前面全部数据
#ss=s.expanding().sum() # 求和
ss=s.ewm(com=0.5).mean()
print(ss)