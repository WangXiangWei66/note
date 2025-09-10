# coding:utf-8
# author:杨淑娟
import threading
import time

# 第一种创建线程的方式
class HelloThread(threading.Thread):
    def run(self):  # 要重写父类的run方法
        print(threading.currentThread().getName(),'正在执行')



# 第二种创建线程的方式
def func():
    print(threading.currentThread().getName(),'正在执行----------')



if __name__ == '__main__':
    for i in range(5):
        hellothread=HelloThread()  # 创建类的对象
        hellothread.start()   # 启动线程



    for i in range(5):
        hellothread=threading.Thread(target=func)  # 使用target指定线程要执行的代码在func函数中
        hellothread.start() # 启动线程

