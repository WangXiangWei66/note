# coding:utf-8
# author:杨淑娟
import datetime


def inputdate():
    indate = input('请输入开始日期:(20200808)后按回车')
    indate = indate.strip()  # 去除空格
    # indate[0:4] 截取分隔 第三位 从0开始
    datestr = indate[0:4] + '-' + indate[4:6] + '-'+ indate[6:]
    return datetime.datetime.strptime(datestr, '%Y-%m-%d')
    # 返回给函数 分割后字符串使用strptime 格式化后的结果


if __name__ == '__main__':
    print('------------------推算日期----------------')
    sdate = inputdate()  # 函数结果格式化返回给sdate参数
    in_num = int(input('输入间隔天数'))
    fdate = sdate + datetime.timedelta(days=in_num)  # timedelta函数表示时间差函数 days表示天
    # 输入时间+修改时间=fdate



    print(f'您推算的日期是{fdate}')
    #print('您推算的日期'+str(fdate).split(' '))   # str+list 报错
    print('您推算的日期' , str(fdate).split(' '))