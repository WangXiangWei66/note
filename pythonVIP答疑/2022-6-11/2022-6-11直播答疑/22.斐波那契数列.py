# coding:utf-8
# author:杨淑娟

def fun(x):
    if x==1 or x==2:    # 1第一个位置 ，2表示第二个位置
        return 1
    else:
        return fun(x-1)+fun(x-2)   #  从第3个数开始，第一项都等于前两项之和

for i in range(1,51):  # 不是算不出来，是数太多
    print(fun(i),end='\t')
'''

50=  第49个数    +              第48个
49  第48个数+  第47个数
48  第47个数+ 第46个数
'''