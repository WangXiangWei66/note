# 名称：音乐播放器
# 功能：
"""
音乐播放器开机动画
"""
# 作者：@NAVIE

from time import*
from tkinter import *
from math import *
from pctdc import *
opwin=Tk()
opwin.geometry('900x600+165-50')
opwin.title('Music Player')
dawg=Canvas(opwin,bg='#1e90ff',height=600,width=900)
#加载标志，文字说明
lg=logo(dawg,3)
for i in range(2):
    dawg.move(lg[i],270,200)
txt1=dawg.create_text(180,380,fill='white',text='欢迎使用Music Player',\
                     font=('仿宋',40,'bold','italic'),anchor='sw')
txt2=dawg.create_text(390,410,text='Loading',fill='white',\
          font=('仿宋',25,'bold','italic'),anchor='sw')
dot=[]
for i in range(6):
    dot.append(cir(dawg,1/5))
for i in range(6):
    dawg.itemconfig(dot[i],fill='white',outline='')
    dawg.move(dot[i],15*sin(pi*i/4),15-15*cos(pi*i/4))
    dawg.move(dot[i],390,400)
dawg.pack()
t=0
#加载点的动态显示
while t<3:
    for i in range(6):
        dawg.move(dot[i],4.5*cos(pi*i/4+t*pi),4.5*sin(pi*i/4+t*pi))
    t+=0.1
    dawg.update()
    sleep(0.05)
