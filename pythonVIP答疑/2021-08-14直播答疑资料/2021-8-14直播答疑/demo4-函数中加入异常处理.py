# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

def calc():
    try:
        a=eval(input('请输入被除数:'))
        b=eval(input('请输入除数:'))
        c=a/b
    except Exception as  e: # 抛出异常对象
        print(e)
    else:
        print('结果:',c) # try...else..finally ,没有异常时的执行顺序
    finally:
        print('无论是否产生异常，我都要执行')

#

calc()
