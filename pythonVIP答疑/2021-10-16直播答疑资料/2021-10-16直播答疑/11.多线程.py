# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
#  多线程
import threading,time
#线程的执行体
def test():
    for i in range(3): #线程的执行操作体
        time.sleep(1)
        print(f'线程名称:{threading.current_thread().name}')

if __name__ == '__main__':
    #一个进程中的主线程  CPU调度执行的是进程中的线程
    print('主进程中的主线程开始运行')
    #创建多个线程  ，采用列表生成式 ,创建四个线程
    threads=[threading.Thread(target=test)for i in range(4)]
    for i in threads:  #遍历多个线程的列表，分别启动线程
        i.start() # 启动线程

    # 让主线程挂起，等待，子线程执行完再执行主线程
    for i in threads:
        i.join()
    print('主进程中的主线程执行结束')

#单核CPU，在同一个时间点，只执行一个线程，　调度是随机的，【也有优先级，优先级高低】
#双核CPU，在同一个时间点，有两个线程在执行


