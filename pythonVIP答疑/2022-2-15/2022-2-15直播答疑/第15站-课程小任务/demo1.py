#教育机构 ：马士兵教育
#讲    师：杨淑娟
#开发时间：2020/4/5 13:17
#任务1：记录用户登录日志
import time
def show_info():
    print('输入提示数字，执行相应操作: 0.退出  1.查看登录日志')
#读录日志
def write_loginfo(username):
    with open ('log.txt','a') as file:
        s='用户名名:{0},登录时间:{1}'.format(username,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        file.write(s)

#读取日志
def read_loginfo():
    with open('log.txt','r')as file:
        while True:
            line=file.readline()
            if line=='':
                break #退出循环s
            else:
                print(line)#输出一行内容

#以主程序方式运行
if __name__ == '__main__':
    username=input('请输入用户名:')
    pwd=input('请输入密码:')
    if 'admin'==username and 'admin'==pwd:
        print('登录成功')
        write_loginfo(username) #写入日志
        show_info() #提示信息
        num=int(input('输入操作数字:'))
        while True:
            if num==0:
                print('退出成功')
                break
            elif num==1:
                print('查看登录日志')
                read_loginfo()
                show_info()
                num = int(input('输入操作数字:'))
            else:
                print('您输入的数字有误')
                show_info()
                num = int(input('输入操作数字:'))
    else:
        print('用户名或密码不正确 ')