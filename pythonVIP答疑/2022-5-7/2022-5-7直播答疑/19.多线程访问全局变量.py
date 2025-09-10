# coding:utf-8
# author:杨淑娟

import threading
from threading import Thread,Lock
import time

ticket=100 # 全局变量

# 线程函数
def task():
    global ticket
    ticket-=1
    time.sleep(1) # threading.current_thread().getName()获取当前线程的名称
    print(threading.current_thread().getName()+f'购买成功，剩余{ticket}张电影票')

if __name__ == '__main__':

    lst=[] # 创建一个列表，  存储线程对象
    for i in range(10):   # 循环10次，创建10个线程对象
        t=Thread(target=task) # 创建线程类对象  ,指定线程要执行的函数为task
        lst.append(t)  # 将线程对象存储到列表中
        t.start()  # 启动线程 、
        #t.join()
    for item in lst: # 遍历列表，线程等待
        item.join() #