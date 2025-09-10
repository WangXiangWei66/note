# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

# (1)函数的参数是局部变量，只能在函数内部使用
# （函数的参数的类型 ）
'''
函数定义处的参数：形式参数【只是起到占位符的作用】--》简称形参
函数调用处的参数：实际参数  --》简称实参


'''
# （1）最最最最普通 的位置参数    ，定义多少个，调用传多少，
#（2）关键字参数   ，在传参的时候要求关键字不能写错
print('hello') #传了一个参数
print('hello','world') #传了两个参数
print('hello','world','2022','北京') # 传了4个参数

#可不可以自己定义函数，可以传递的参数个数不定
def fun(*args):
    pass
#　查看源代码，　ctrl+鼠标左键点击

'''
 ATM机使用过吗？
 IPO 问题描述法
 I-->Input  输入  --》（输入部分都可以定义为参数）
            取款/取款， 输入账号和密码  ---》所以账号和密码就可以作为ATM机这个程序的参数
 P -->process 处理
 O -->Output 输出
             输出方式有两种： 1）自己输出--》咱使用print  
                              2）别人输出-->咱使用返回值， 由调用处输出
            什么情况下 自己输出，使用print，什么情况下，别人输出，使用return
    
    想： 我的处理过程，其它人会用吗？，其他人会用就使用return,其他人不会用就使用print
         如果不确定，就使用return
         使用return :程序的处理结果 两种状态 ，return True ,return False
                     程序的处理结果有三种状态： 正数，负数和 0   （1，-1，0）
                     程序的处理结果有一种状态： 直接return 结果（值）
                     程序的处理结果有三种及三种以上状态，直接return结果（值）
'''
#举个例子　，登录功能
def login(user_name,pwd):
    if user_name=='ysj' and pwd=='8888':
        return True
    else:
        return False
    #因为成功和失败是两种状态，所以可以使用True或False表示

#程序员A调用该函数
if login(input('请输入用户名'),input('请输入密码')):
    print('登录成功')
else:
    print('登录失败')

#程序员B调用该函数

for i in range(3):
    if login(input('请输入用户名'),input('请输入密码')):
        print('系统正在登录,请稍后')
        break
    else:
        print('对不起，账号或密码不正确')







