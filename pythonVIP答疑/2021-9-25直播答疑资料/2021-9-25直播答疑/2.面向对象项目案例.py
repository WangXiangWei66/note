# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
from prettytable import  PrettyTable
from datetime import datetime
class Account(object):
    # 类中的第一个方法通常为初始化方法，给对象的属性进行赋值的
                     # money=0,account_logs=[]默认值参数
    def __init__(self,money=0,account_logs=[]): # 局部变量money和account_logs
        self.money=money # 等号的左侧是属性，右侧是局部变量
        self.account_logs=account_logs

    def deposit(self,deposit_money): # 参数为存储金额
        #存款的时候，余额增加
        self.money+=deposit_money
        # 上句代码相当于self.money=self.money+deposit_money
        #存款完成产生交易日志
        self.account_logs.append([deposit_money,'存款'])
        print('当前余额为:',self.money)

    def withdraw(self,wd_money): #参数为取款金额
        if wd_money>self.money:
            print('余额不足')
        else:
            #取款的时候余额减少
            self.money-=wd_money
            self.account_logs.append([wd_money, '取款'])
            print('当前余额为:', self.money)


    #打印交易详情
    def  transaction_log(self):
        field_name=['交易日期','摘要','金额','币种','余额']  # 做为二维表格的标题
        ptable=PrettyTable(field_names=field_name)
        for item in self.account_logs: # 遍历的item 为一个列表
            if item [1]=='存款':
                item[0]='+{}'.format(item[0])
            else:
                item[0] = '-{}'.format(item[0])

            #创建一个行对象
            row=[datetime.today(),item[1],item[0],'人民币',self.money]
            # 将行添加到表格中
            ptable.add_row(row)
        #输出即可
        print(ptable)



# 编写菜单
def menu():
    print('----------------银行账户资金交易管理--------------------')
    print('\t\t\t1.存款')
    print('\t\t\t2.取款')
    print('\t\t\t3.打印详情')
    print('\t\t\t0.退出')

# 开始测试(以下代码只有在单击右键运行时才执行)
if __name__ == '__main__':
    #创建对象
    account=Account()
    while True:
        menu() # 调用系统菜单
        choice=eval(input('请输入您的选择')) #eval()什么意思？
        if choice==1:
            flag=True
            while flag:
                deposit_money=eval(input('请输入存款金额:'))
                #调用存款的方法
                account.deposit(deposit_money)
                # 为什么要转成小写，目的是什么？
                flag=True if input('是否继续存款?Y/N').lower()=='y' else False

        elif choice==2:
            flag=True
            while flag:
                wd_money=eval(input('请输入取款金额:'))
                # 调用Account中的取款方法
                account.withdraw(wd_money)
                flag = True if input('是否继续取款?Y/N').lower() == 'y' else False
        elif choice==3:
            account.transaction_log()
        elif choice==0:
            exit(0)
            print('退出系统')
        else:
            print('请选择正确的编号')





# 目前该项目可提升的地方  1.时间不合适【都相同】，应该改成取款或存款的时间
                     #   2.时间的格式yyyy-MM-dd hh:mm:ss
                     #   3.余额的显示 【应该显示每次操作之后的余额】
                     # 修改的位置，每次操作之后，应该是存款，取款的函数处

