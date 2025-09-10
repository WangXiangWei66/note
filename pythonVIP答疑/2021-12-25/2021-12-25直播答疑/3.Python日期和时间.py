# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# （1）time对时间进行处理

import time
print(time.time()) # 结果为时间戳，从1970-1-1:00:00:00到当前时间的秒数

print(time.localtime()) # 不给参数，获取到的是当前时间的struct time对象
# 因为中国使用的是东八区
print(time.localtime(1)) # 获取的是指定时间的struct time对象  ，1表示的是1秒  1970-1-1 08:00:01
print(time.gmtime(1)) # 1970-1-1  00:00:01
#strp和strf  ，转换的
#strf  :  将strct time转成 str
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
#strp   将str转成struct time
print(time.strptime('2022-1-1 00:00:01','%Y-%m-%d %H:%M:%S'))

#(2)datetime  对日期和时间的操作，提供了方便的方法
import  datetime
#获取当前时间
print(datetime.datetime.now()) # 获取当前时间
print(datetime.datetime.today()) # 获取当前日期和时间

print(datetime.date.today()) # 获取当前日期
#也有转换的方法，跟字符串去转换
print(datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S'))

print(datetime.datetime.strptime('2021-12-25 20:43:21','%Y-%m-%d %H:%M:%S'))

#calendar， 日历
import calendar
cal=calendar.calendar(2022) # 输出2022年的日历
print(cal)
#输出指定年份，和月份的日历
calendar.prmonth(1999,12)

# 日期推算天数，用datetime
print(datetime.datetime.now()+datetime.timedelta(days=10)) #往后推迟


print(datetime.datetime.now()+datetime.timedelta(days=-10))  # 往前推迟

print(datetime.datetime.now()+datetime.timedelta(hours=-10)) # 往前推迟 10个小时
