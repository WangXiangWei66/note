# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

from multiprocessing import Process  #　准备创建多进程
import os,time
def test(intervalu): #这是一个普通的函数
    print(f'我是第一个子进程{os.getpid()}执行')

    time.sleep(intervalu)
    print(f'子进程{os.getpid()}执行结束')

def test2(interval):
    print(f'我是第二个子进程{os.getpid()}')
    time.sleep(interval) # 休息interval秒
    print('第二个子进程执行结束')
if __name__ == '__main__': #只有单击右键运行该Python文件时，main里的代码才会执行
     # 主进程
     print('''----主进程开始执行-----------''')
     #创建子进程     test是函数的名称，不要加()  test()，方法调用
     p=Process(target=test,args=(3,)) # 创建一个子进程，这个子进程干什么工作呢？让执行点啥？通过target参数指定要执行的函数

     p2=Process(target=test2,args=(2,)) #创建的第二个子进程,第二个子进程的任务执行需要2秒钟执行结束
     # 启动子进程
     p.start()
     p2.start()

     p.join()  # 主进程等待子进程结束，然后主进程再执行
     p2.join() # 主进程等待子进程p2结束，然后主进程再执行
     print('主进程执行结束')

