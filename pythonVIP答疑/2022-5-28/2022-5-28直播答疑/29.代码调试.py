# coding:utf-8
# author:杨淑娟
def f():
    i=1
    while i<6:
        n = input('我心里有个[1-100]的整数请你猜一猜:')
        if int(n)==76:
           print('猜对了')
           break
        elif int(n)<76:
             print('小了')
             i+=1
             continue

        else:
            print('大了')
            i+=1
            continue
        print('没机会了')

f()
