# coding:utf-8
# author:杨淑娟

def  fun(a,b,c):
    s=a+b+c
    return s


result=fun(10,20,30)
print(result)

# 异常处理

try:
    file=open('a.txt','r',encoding='utf-8') # 没有创建成功
except Exception as e:
    print(e)
finally:

    print('程序结束')

