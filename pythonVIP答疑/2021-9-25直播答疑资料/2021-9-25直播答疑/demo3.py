# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
from prettytable import PrettyTable
from datetime import datetime
class Account(object):
    def __init__(self,money=0,account_logs=[]):
        self.money=money
        self.account_logs=account_logs

    #存款
    def deposit(self,deposit_money):
        self.money+=deposit_money
        self.account_logs.append([deposit_money,'存钱'])
        print('当前余额为:',self.money)
    # 取款
    def withdraw(self,wd_money):
        if wd_money>self.money:
            print('余额不足')
        else:
            self.money-=wd_money
            self.account_logs.append([wd_money,'取钱'])
            print('当前余额为:',self.money)

    # 详情
    def transaction_log(self):
        field_name=('交易日期','摘要','金额','币种','余额')
        table=PrettyTable(field_names=field_name)
        for item in self.account_logs:
            if item[1]=='存钱':
                item[0]='+{}'.format(item[0])
            else:
                item[0]='-{}'.format(item[0])
            row=[datetime.today(),item[1],item[0],'人民币',self.money]
            table.add_row(row)
        print(table)

def show_menu():
    print('======================银行账户资金交易管理=================')
    print('\t\t\t\t1.存款')
    print('\t\t\t\t2.取款')
    print('\t\t\t\t3.打印交易详情')
    print('\t\t\t\t0.退出')
    print('============================================================')

if __name__ == '__main__':

    account=Account()
    while True:
        show_menu()
        choice=eval(input('请输入您的选择:'))
        if choice==0:
            exit(0)
            print('退出系统')
        elif choice==1:
            flag=True
            while flag:
                deposit_money=eval(input('存款金额:'))
                account.deposit(deposit_money)
                flag=True  if input('是否继续存款?Y/N').lower()=='y' else False
        elif choice==2:
            flag=True
            while flag:
                wd_money = eval(input('取款金额:'))
                account.withdraw(wd_money)
                flag = True if input('是否继续取款?Y/N').lower() == 'y' else False
        elif choice==3:
            account.transaction_log()
        else:
            print('请选择正确的编号')