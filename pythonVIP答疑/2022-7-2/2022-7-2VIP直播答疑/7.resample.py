# coding:utf-8
# author:杨淑娟
import pandas as pd
index=pd.date_range('1/1/2022',periods=9,freq='T')  #freq表示采样频率
print(index)   # 结果为datetime64 ,产生了9个时间，开始时间是2022-1-1 ， T -->分钟
# 产生9个datetime对象，每个datetime对象时间相差1分钟

# Series对象与DataFrame对象是Pandas中两个非常重要的对象
series=pd.Series(range(9),index=index)  # 创建一个Series对象, datetime是索引，0-8 是索引对应的值
print(series)

# 一共有9行数据

# 重采样， 就是对这9行数据进行重新处理，现在的频率是每分钟，  重新采样 ，降低频率，每三分钟
# 重采样，降低采样频率为三分钟
series=series.resample('3T').sum()  # 每三分钟
print(series)

