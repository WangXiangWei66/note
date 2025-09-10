# coding=utf-8
# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
# 开发时间：2020/4/5 15:28
# 任务1：模拟高铁售票系统
import prettytable as pt
# 显示座席

def show_ticket(row_num):
    tb=pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        lst=['第{}行'.format(i+1),'有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)

# 订票
def order_tickt(row_num,row,column):
    tb=pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        if int(row)==i+1:
            lst = ['第{}行'.format(i + 1), '有票', '有票', '有票', '有票', '有票']
            lst[int(column)]='已售'
            tb.add_row(lst)
        else:
            lst = ['第{}行'.format(i + 1), '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)

if __name__ == '__main__':
    row_num=13 #共计13行
    show_ticket(row_num)#显示空座
    choose_num=input('请输入选择的座位,如13,5表示第13排5号座位:')
    try:
        row,column=choose_num.split(',')#根据,进行分割
    except:
        print('输入格式错误，如选择13排5号座位请输入:13,5')
    order_tickt(row_num,row,column)