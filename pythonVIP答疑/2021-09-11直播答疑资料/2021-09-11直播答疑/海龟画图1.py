# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import turtle
import random
color=["red","pink","blue","green","black"]
turtle.up()
turtle.goto(300,0)
for i in range(6):
    turtle.color(random.choice(color))
    turtle.down()
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.up()
    turtle.goto(300-(i+1)*150,0)