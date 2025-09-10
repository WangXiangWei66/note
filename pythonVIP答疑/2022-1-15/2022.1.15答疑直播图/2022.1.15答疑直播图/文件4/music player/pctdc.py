# 名称：音乐播放器
# 功能：
"""
音乐播放器的基本图标元素
"""
# 作者：@NAVIE

def logo(dw,i=1):
    n1=dw.create_polygon(50,70,50+i*20,70-i*30,50+i*20,70-5*i,\
                        50+35*i,70-i*30,50+45*i,70,\
                        50+35*i,70-15*i,50+21*i,70-i*10,50+11*i,70-15*i,fill='#ff00ff')
    n2=dw.create_polygon(50+50*i,70,50+95*i,\
                         70-30*i,50+50*i,70-5*i,\
                         50+55*i,70-25*i,50+95*i,70,50+50*i, 70-30*i,fill='#ff00ff')
    return [n1,n2]
def cir(dw,i=1):
    n=dw.create_oval(50,50,50+20*i,50+20*i)
    return n
def fang(dw,i=1):
    n=dw.create_rectangle(60,60,60+10*i,60+10*i)
    return n
def btn(dw):
    bzp=dw.create_oval(50,50,90,90,fill='#6959cd',outline='#6959cd')
    bzl=dw.create_oval(50,50,90,90,fill='#6959cd',outline='#6959cd')
    bzr=dw.create_oval(50,50,90,90,fill='#6959cd',outline='#6959cd')
    p=dw.create_polygon(60,58.4,60,81.6,80,70,fill='white',outline='white')
    p1=dw.create_polygon(60,58.4,60,81.6,80,70,fill='white',outline='white')
    _p=dw.create_polygon(60,70,80,81.6,80,58.4,fill='white',outline='white')
    t1=dw.create_rectangle(60,60,66.7,80,fill='white',outline='white',state='hidden')
    t2=dw.create_rectangle(80,80,73.3,60,fill='white',outline='white',state='hidden')
    t11=dw.create_rectangle(60,60,66.7,80,fill='white',outline='white')
    t21=dw.create_rectangle(80,80,73.3,60,fill='white',outline='white')
    zp=[bzp,p]
    zt=[t1,t2]
    zl=[bzl,_p,t11]
    zr=[bzr,p1,t21]
    n=[zp,zt,zl,zr]
    for i in range(len(n)):
        if i == 0 or i == 1:
            c = 0
        elif i == 2:
            c = -1
        else:
            c = 1
        for j in range(len(n[i])):
            dw.move(n[i][j], 48 * c, 0)
    return n
def mcsgn(dw,i=1):
    bottom=dw.create_oval(80,80,80+40*i,80+20*i,fill='#ee7600',outline='#ee7600',state='hidden')
    rcbar=dw.create_polygon(80+40*i,80+10*i,80+50*i,80\
                            -50*i,80+38*i,80-45*i,\
                            80+28*i,80+5*i,fill='#ee7600',outline='#ee7600',state='hidden')
    sec_1=dw.create_polygon(80+40*i,80-44*i,80+70*i,80-44*i,80+75*i\
                        ,80-49*i,80+45*i,80-49*i,fill='#ee7600',outline='#ee7600',state='hidden')
    sec_2=dw.create_polygon(80+40*i,80-20*i,80+60*i,80-20*i,80+65*i\
                            ,80-25*i,80+45*i,80-25*i,fill='#ee7600',outline='#ee7600',state='hidden')
    pic=[bottom,rcbar,sec_1,sec_2]
    return pic
if __name__=='__main__':
    from tkinter import *
    opwin=Tk()
    opwin.geometry('900x600+165-50')
    dawg=Canvas(opwin,bg='Blue',height=600,width=900)
    test_fun = mcsgn(dawg,1/2)
    for i in test_fun:
        dawg.itemconfig(i,state='normal')
    dawg.pack()
    dawg.mainloop()

