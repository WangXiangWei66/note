# coding:utf-8
# author:杨淑娟
'''银行取钱问题 '''
import threading
import time
class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self.balance = balance

# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 账户余额大于取钱数目
    if account.balance >= draw_amount:
        # 吐出钞票
        print(threading.current_thread().name\
            + "取钱成功！吐出钞票:" + str(draw_amount))
        time.sleep(1)  # 关键问题 在这  ，休眠一秒
        # 修改余额
        account.balance -= draw_amount
        print("\t余额为: " + str(account.balance))
    else:
        print(threading.current_thread().name\
            + "取钱失败！余额不足！")
# 创建一个账户
acct = Account("1234567" , 1000)

# 模拟两个线程对同一个账户取钱       # acct不能带括号，带括号是手动调用，不带括号是系统调用
threading.Thread(name='甲', target=draw , args=(acct , 800)).start()
threading.Thread(name='乙', target=draw , args=(acct , 800)).start() # 不是信用卡，不可以透支的
# 所以带来了线程的安全性问题 ，银行亏钱了，^  _  ^   ，不高兴啊
# 解决方案，一个人取钱的时候，先把账户锁定，另一个账户需等待，等一个操作完，再操作第二个
# 12306春运抢票时，。。。在排队，请稍后。。。 查询无需加锁（所以查询的数据不够准确，脏数据），

