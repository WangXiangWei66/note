# coding:utf-8
# author:杨淑娟

import datetime
def inputdate():
    indate=input('请输入开始日期(20200808)后按回车:')
    indate=indate.strip()
    datester=indate[0:4]+'-'+indate[4:6]+'-'+indate[6:]
    return datetime.datetime.strptime(datester,'%Y-%m-%d')

print('-----------------推算几天后的日期-----------------')
sdate=inputdate()
in_num=int(input('请输入间隔数:'))
fdate=sdate+datetime.timedelta(days=in_num)
print('您推算的日期是:'+str(fdate))
print('您推算的日期是:',str(fdate).split(' ')) # 劈分之后的结果是列表
print('您推算的日期是:',str(fdate).split(' ')[0])
print('您推算的时间是:',str(fdate).split(' ')[1])