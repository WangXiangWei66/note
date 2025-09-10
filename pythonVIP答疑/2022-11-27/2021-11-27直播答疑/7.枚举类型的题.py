# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

# 三个未知量，循环两层，四个未知量，循环三层
#1.  a*b+c=94 a+b*c=95 求a,b,c（

for a in range(95):   # 第一次循环a=0,b=0,c=?  ,a=0,b=1,c=?   a=0,b=2,c=?
    for b in range(95):
        c=94-a*b
        if a+b*c==95:
            print(f'a={a},b={b},c={c}')

# a=31,b=2,c=32   31*2+32=94   31+2*32=95
