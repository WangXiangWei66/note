# 教育机构：马士兵教育
# 讲    师：杨淑娟
import  demo
filename='a.txt'
def save():
    s={'username':'admin','pwd':'8888'}
    with open(filename,'a+',encoding='utf-8')as file:
        file.write(str(s)) #将字典转成str类型

#编写函数读取
def read():
    with open(filename,'r',encoding='utf-8') as file:
       res= file.readline()  #读出来的是str类型
       res=eval(res)
       #print(res,type(res))
       return res   #编写函数返回值

if __name__ == '__main__':
    #需要使用到demo中的User类
    res=read()

        #创建对象
    user=demo.User(res.get('username'),res['pwd'])  #使用到demo.py中的User类
    if user.check():
        print('登录成功')

    else:
        print('对不起，账号或密码不正确')






