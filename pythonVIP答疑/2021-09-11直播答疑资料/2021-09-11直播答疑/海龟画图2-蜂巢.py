# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

from turtle import *
import random


# 画一个六边形
def onesix(l, x, y):
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    circle(l, steps=6)
    rgb = colorrgb()
    color('black', rgb)
    end_fill()


# 产生颜色的随机数
def colorrgb():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


# 画r圈六边形
def rsix(l, r):
    xyset = set()
    findxy(r, xyset)
    print(xyset)
    for x, y in xyset:
        onesix(l, x, y)


# 找到r圈六边形中每个六边形的xy坐标
# 数据用集合是因为不重复
def findxy(r, xyset=set()):
    x, y = 0, 0
    xyset.add((x, y))
    for i in range(r):
        xyempty = set()
        for x, y in xyset:
            # 这里用到了round函数是因为如果不取小数，最后会因为计算的基数不同，两个相同的坐标得出来的值不同
            # 虽然图的结果差不多，可是会导致集合有重复元素，而导致重复画一个六边形，就像
            # 51.939439493943901  51.9394394939439
            xyempty.add((round(x + (3 ** 0.5) * l, 10), round(y, 10)))
            xyempty.add((round(-x - (3 ** 0.5) * l, 10), round(y, 10)))
            xyempty.add((round(x + (3 ** 0.5) * l / 2, 10), round(y + 3 * l / 2, 10)))
            xyempty.add((round(-x - (3 ** 0.5) * l / 2, 10), round(y + 3 * l / 2, 10)))
            xyempty.add((round(x + (3 ** 0.5) * l / 2, 10), round(-y - 3 * l / 2, 10)))
            xyempty.add((round(-x - (3 ** 0.5) * l / 2, 10), round(-y - 3 * l / 2, 10)))
        xyset |= xyempty


# tracer(False) #不要动画，不知道为什么用了这句语句后，最后一笔总是写不了，有个六边形会少一个边
#turtle.speed(100)  # 速度会很慢
#hideturtle()
l = 20  # 一个六边形的边的长度
r = 6  # 蜂窝的圈数
rsix(l, r)
done()