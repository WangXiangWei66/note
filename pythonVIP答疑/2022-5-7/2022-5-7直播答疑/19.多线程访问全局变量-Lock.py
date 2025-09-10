# coding:utf-8
# author:杨淑娟
import threading
from threading import Thread,Lock
import time

ticket=100 # 全局变量

# 线程函数
def task():
    global ticket

    my_lock.acquire()  # 上锁
    ticket-=1
    time.sleep(1)
    print(threading.current_thread().getName()+f'购买成功，剩余{ticket}张电影票')


    my_lock.release()  # 释放锁


if __name__ == '__main__':
    my_lock=Lock() # 创建锁对象
    lst=[]
    for i in range(10):
        t=Thread(target=task) # 创建线程类对象
        lst.append(t)
        t.start()
    for item in lst:
        item.join()