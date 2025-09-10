# coding:utf-8
# author:杨淑娟

try:

    file=open('b.txt','r',encoding='utf-8')
except FileNotFoundError as e: # e表示的是FileNotFoundError异常类的对象
     # 文件不存在的异常
    print(e)
    print('文件不存在')

finally: # 无 论是否产生异常，都要执行的代码
    try:
        file.close()  # 又抛出了一个异常，file is not defined
    except Exception as e:
        print(e)
    finally:
        print('程序结束')