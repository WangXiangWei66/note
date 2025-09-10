# 教育机构：马士兵教育
# 讲    师：杨淑娟
'''写程序从外往里面写'''
#1）for...in
# for i in range(3):
#     username=input('请输入用户名:')
#     pwd=input('请输入密码:')
#     #进行判断，输入的是否正确
#     if username=='admin' and pwd=='8888':
#         print('登录成功')
#         break   #退出循环
#     else:  #else与if搭配使用的
#         if i<2:
#             print(f'账号和密码不正确，您还有{2-i}次机会') #f表示的是什么 ？Python的三种格式化方式
# else:
#     print('对不起，三次均输入错误，请联系后台管理员!!!')


'''
else的语法搭配使用
if...else   :if判断的结果为False时，执行else部分
for...else  :for循环正常执行结果，中间没有到break,return的情况，执行else部分
while ...else:while循环正常执行结果，中间没有到break,return的情况，执行else部分

== 与id的情况
# 
# 程序的执行顺序，是从上到下执行，编写 程序的顺序是从外往里
# '''
# #2)使用while
# a=1  #记录循环次数
# while  a<4:   # <=3 ,<4
#     username = input('请输入用户名:')
#     pwd = input('请输入密码:')
#     if username == 'admin' and pwd == '8888':
#         print('登录成功')
#         break  # 退出循环
#     else:
#         if a<3:
#             # 字符串的格式化，使用的是字符串的format 方法
#             print('用户名或密码不正确，您还有{}次机会'.format(3-a))
#     a+=1
# else:
#     print('对不起，三次均输入错误，请联系后台管理员!!!')


#3）可以使用函数来实现
# def check(username,pwd):  #username,pwd是函数的形式参数 ,True 或False是函数的返回值
#     if username=='admin' and pwd=='8888':
#         return True
#     return False   #if 判断条件不成立，直接return False
#
# for i in range(3):
#     username=input('请输入用户名:')
#     pwd=input('请输入密码:')
#     #调用验证账户号或密码不正确的函数
#     flag=check(username,pwd)  #验证结果有True或False
#     if flag:  #还可以写成  flag==True
#         print('登录成功!')
#         break
#     else:
#         if i<2:
#          print('账号或密码不正确，您还有{}次机会'.format(2-i))
# else:
#     print('对不起，三次均输入错误，请联系后台管理员!!!')


# 4)使用面向对象
class User(object):
    def __init__(self,username,pwd): #初始化函数   username,pwd 方法的参数
        self.uname=username   #类的属性叫uname
        self.upwd=pwd         #类的属性叫upwd

    def check(self):  # username,pwd是函数的形式参数 ,True 或False是函数的返回值
        if self.uname=='admin' and self.upwd=='8888':
            return True
        return False   #if 判断条件不成立，直接return False

# 准备使用
if __name__ == '__main__':
    for i in range(3):
        username=input('请输入用户名:')
        pwd=input('请输入密码:')
        #创建对象
        user=User(username,pwd)

        flag=user.check() #对象名.方法名，调用验证用户名和密码的方法
        if flag:
            print('登录成功')
            break
        else:
            if i<2:
                print(f'用户名或密码错误，您还有{2-i}次机会')
    else:
        print('三次均错误，请联系管理员')





