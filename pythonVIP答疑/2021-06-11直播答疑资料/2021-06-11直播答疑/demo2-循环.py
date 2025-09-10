# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
#(1)银行取款
balance=5000 # 余额
for i in range(3):   #0,1,2
    pwd=input('请输入银行卡密码:')
    if pwd=='888888':
        print('---------------可以取款')
        while True:
            money=eval(input('请输入取款金额:'))  # 转成实际的类型
            if money<=balance:
                balance-=money
                print('取款成功，余额为:',balance)
            else:
                print('对不起余额不足!!')
            answer=input('您还继续吗？y/n')
            if answer=='n':
                print('谢谢您的使用!!!')
                break # 退出while

        break  # 退出for
    else:
        print('密码不正确')



