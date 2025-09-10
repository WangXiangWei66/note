#小豆首席的优秀学员
#ID:bond666
#开发时间：2022/3/27 21:00
#希望老师讲解下如何实在多次订票
import prettytable as pt
#显示坐席
file='高铁座位.txt'
'''
def show_ticket(row_num):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    # print(tb)
    # s = tb.get_string()
    # with open(file, 'a+',encoding='utf-8') as f:
    #     f.write(tb.get_string())
#订票
def order_ticket(row_num,row,column):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        if int(row)==i+1:
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(column)]='已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)
    with open(file, 'w',encoding='utf-8') as f:
        f.write(tb.get_string())
def order_ticket_again(row_num,row,column):

if __name__ == '__main__':

    row_num=13
    # show_ticket(row_num)     # 以下代码用于刷新座位

    choose_num=input('请输入选择的座位,如13,5表示13排5号座位')
    try:
        row,column=choose_num.split(',')
    except:
        print('输入个是有误,如13排5号座位,应该输入"13,5"')
    order_ticket(row_num,row,column)
    '''
#从文件读取第一次订票后的座位信息,将第二次选的 3,1 座位'已售'写入文件
with open(file, 'r',encoding='utf-8') as f:
    lst=f.readlines()
    print(lst)
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    row=3
    column=1
    for i in range(16):
        if i<3:
            pass
        elif row+2 == i:
            lst_new = lst[i].strip().replace(' ','').strip('|').split('|')
            # lst1 = lst[i].strip().strip('|').split('|')
            # print('lst1',lst1)
            # print('****',lst_new)
            # print('----',lst[i])
            lst_new[int(1)] = '已售'
            print('*****',lst_new)
            tb.add_row(lst_new)
        else:
            lst_new = lst[i].strip().replace(' ','').strip('|').split('|')
            print('+++++', lst_new)
            tb.add_row(lst)
    print(tb)