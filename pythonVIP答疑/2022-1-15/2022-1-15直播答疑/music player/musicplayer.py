# 名称：音乐播放器
# 功能：
"""
单击相应按钮实现播放，暂停，上一曲，下一曲
快捷键：
Ctrl+方向上键：上一曲
Ctrl+方向下键：下一曲
空格键：暂停/播放
"""
# 作者：@NAVIE


import os
from oppct import * #开始动画以及根窗口
from random import *
#加载播放库
import pygame
pygame.init()
pygame.mixer.init()
#处理函数
def plyac1():#播放动画
    global dp,step_orange,flag_orange
    if dp==PLAY:
        step_orange+=0.01
        if step_orange<10 and flag_orange:
            for i in range(len(mscnote_1)):
                dawg.move(mscnote_1[i], 0.12, -0.12 * 1 / 3 * step_orange)
                dawg.itemconfig(mscnote_1[i],state='normal')
            if step_orange>10:
                flag_orange=False
        else :
            for i in range(len(mscnote_1)):
                dawg.move(mscnote_1[i], 0.12, 0.12 * 1 / 25 * step_orange)
                dawg.itemconfig(mscnote_1[i],state='normal')
            if step_orange>20:
                step_orange, flag_orange= 0, True
                for i in range(len(mscnote_1)):
                    dawg.move(mscnote_1[i],-240,129)
                    dawg.itemconfig(mscnote_1[i],state='normal')
    else:
        for i in range(len(mscnote_1)):
            dawg.itemconfig(mscnote_1[i],state='hidden')
def plyac2():
    global dp,step_green,flag_green
    if dp==PLAY:
        step_green+=0.01
        if step_green<10 and flag_green:
            for i in range(len(mscnote_2)):
                dawg.move(mscnote_2[i], -0.12, -0.12*1/3*step_green)
                dawg.itemconfig(mscnote_2[i],state='normal')
            if step_green>7.6:
                flag_green=False
        else :
            for i in range(len(mscnote_2)):
                dawg.move(mscnote_2[i], 0.2, 0.02*1/6*step_green)
                dawg.itemconfig(mscnote_2[i],state='normal')
            if step_green>27:
                step_green, flag_green= 0, 1
                for i in range(len(mscnote_2)):
                    dawg.move(mscnote_2[i],-296.6,4.6)
                    dawg.itemconfig(mscnote_2[i], state='normal')
    else:
        for i in range(len(mscnote_2)):
            dawg.itemconfig(mscnote_2[i],state='hidden')
def autoplaymd():#自动播放模式
    global song_now
    if dec_m.get()=='one':
        c=namelst.index(song_now)
    elif dec_m.get()=='slide':
        if namelst.index(song_now)==len(namelst)-1:c=0
        else:c=namelst.index(song_now)+1
        song_now=namelst[c]
    elif dec_m.get()=='rand':
        song_now=choice(namelst)
        c=namelst.index(song_now)
    if dp == PLAY:
        songlst.select_clear(0, len(namelst) - 1)
        songlst.select_set(c)
        play()
def play():#播放函数
    global song_now,dp,totaltime,lyricsl
    pygame.mixer.music.load(loadpt_mc+song_now)
    pygame.mixer.music.play()
    playnow_screen.config(text='当前曲目：'+song_now)
    ls=loadpt+'/line/'+patch(song_now)
    if patch(song_now) in os.listdir(loadpt_ln):
        with open(ls,encoding='utf-8') as f:
            lntxt=f.readlines()
        contain=''.join(lntxt[1:])
        totaltime=(eval(lntxt[0][0])*10+eval(lntxt[0][1]))*60+eval(lntxt[0][3])*10+eval(lntxt[0][4])
    else:
        contain='无歌词'
        totaltime=0
    txts.delete(1.0,'end')
    txts.insert('end',contain)
    if totaltime:
        lyricsl['run']=1/(len(lntxt)-1)
        lyricsl['step']=(1-lyricsl['run'])/totaltime/910
    else:
        lyricsl['run']=1
        lyricsl['step']=0
    tip.config(fg='#eed2ee')
    dp=PLAY
def patch(n):#字符转换
    s=''
    for i in n:
        if i!='.':
            s+=i
        else :
            s+='.txt'
            break
    return s
#操作事件
def sndaw(text):#播放音量
    pygame.mixer.music.set_volume(eval(deca.get()))
def plorps(event):#播放暂停
    global dp
    if dawg.itemcget(bn1[0][1],'state')=='hidden' and dp == PLAY:
        pl='normal';ps='hidden';dp=PAUSE
        pygame.mixer.music.pause()
    else:
        if song_now!='':
            pl = 'hidden';ps = 'normal'
            if dp == PAUSE:
                pygame.mixer.music.unpause()
            elif dp == END:
                play()
            dp=PLAY
        else :
            pl='normal';ps='hidden'
            tip.config(fg='red')
    ptccg(pl,ps)
def lasty(event):#上一曲
    global song_now
    if song_now!='':
        if dec_m.get()=='rand':
            song_now = choice(namelst)
            c=namelst.index(song_now)
        else:
            if namelst.index(song_now)==0:c=len(namelst)-1
            else:c=namelst.index(song_now)-1
        song_now=namelst[c]
        songlst.select_clear(0,len(namelst)-1)
        songlst.select_set(c)
        if dp==PLAY: play()
    else :tip.config(fg='red')
def nexty(event):#下一曲
    global song_now
    if song_now!='':
        if dec_m.get()=='rand':
            song_now = choice(namelst)
            c=namelst.index(song_now)
        else:
            if namelst.index(song_now)==len(namelst)-1:c=0
            else:c=namelst.index(song_now)+1
        song_now=namelst[c]
        songlst.select_clear(0,len(namelst)-1)
        songlst.select_set(c)
        if dp==PLAY: play()
    else :tip.config(fg='red')
def select(event):#选择播放
    global song_now
    song_now=songlst.get(songlst.curselection())
    play()
    ptccg("hidden","normal")
def ptccg(pl,ps):#修改图标
    dawg.itemconfig(bn1[0][1], state=pl)
    dawg.itemconfig(bn1[1][0], state=ps)
    dawg.itemconfig(bn1[1][1], state=ps)
#主函数
def Music_Play():
    while(True):
        if not (pygame.mixer.music.get_busy()) and song_now:
            autoplaymd()
        plyac1()
        plyac2()
        if dp == PLAY:
            txts.yview_moveto(lyricsl['run'])
            lyricsl['run']+=lyricsl['step']
        dawg.update()


#全局变量
song_now=''
lyricsl={'run':0,'step':0}
PAUSE=0
PLAY=1
END=-1
dp=END
#动画效果变量
step_orange=0
flag_orange=True
step_green=0
flag_green=True

#加载播放界面和按钮----------------------------------------
dawg.delete(ALL)
dawg.config(bg='#87cefa')
met=fang(dawg,36)
dawg.itemconfig(met,fill='#eed2ee',outline='')
dawg.move(met,380,0)
disk=cir(dawg,12)
dawg.itemconfig(disk,fill='#5e5e5e',outline='')
dawg.move(disk,450,68)
lg1=logo(dawg,2)
for i in range(2):
    dawg.move(lg1[i],480,210)
bn1=btn(dawg)
for i in range(len(bn1)):
    for j in range(len(bn1[i])):
        dawg.move(bn1[i][j],553,380)
dec_m=StringVar()
item=StringVar()
deca=StringVar()
dec_m.set('one')
mod_modeselect=LabelFrame(dawg,text='模式选择',font=('仿宋',14,'bold'),bg='#87cefa')
mod_modeselect.place(x=515,y=480)
Radiobutton(mod_modeselect,text='单曲循环',font=('仿宋',14,'bold'
            ),bg='#87cefa',variable=dec_m,value='one'
            ).pack(expand=1,ipadx=50)
Radiobutton(mod_modeselect,text='顺序播放',font=('仿宋',14,'bold'
            ),bg='#87cefa',variable=dec_m,value='slide'
            ).pack(expand=1,ipadx=50)
Radiobutton(mod_modeselect,text='随机播放',font=('仿宋',14,'bold'
            ),bg='#87cefa',variable=dec_m,value='rand'
            ).pack(expand=1,ipadx=50)
mod_playlist=LabelFrame(dawg,text='播放列表',font=('仿宋',16,'bold'),bg='#87cefa')
mod_playlist.place(x=50,y=40)
mod_lyrics=LabelFrame(dawg,text='歌词',font=('仿宋',16,'bold'),bg='#87cefa')
mod_lyrics.place(x=50,y=360)
mod_sound=LabelFrame(dawg,text='音量',font=('仿宋',16,'bold'),bg='#87cefa')
mod_sound.place(x=820,y=450)
playnow_screen=Label(dawg,text='当前曲目：',fg='#9400d3')
playnow_screen.place(x=200,y=20)
#移动的音符
mscnote_1=mcsgn(dawg,1/2)
mscnote_2=mcsgn(dawg,1/2)
for i in range(len(mscnote_1)):
   dawg.move(mscnote_1[i],515,160)
for i in range(len(mscnote_2)):
   dawg.move(mscnote_2[i],515,160)
for i in range(len(mscnote_2)):
   dawg.itemconfig(mscnote_2[i],fill='green',outline='green')
#------------------------------------------------


#快捷键绑定------------------------------------------
#播放暂停切换
opwin.bind('<space>',plorps)
for i in range(2):
    for j in range(2):
        dawg.tag_bind(bn1[i][j],'<1>',plorps)
#播放上\下一曲
opwin.bind('<Control-Up>',lasty)
opwin.bind('<Control-Down>',nexty)
for i in range(3):
    dawg.tag_bind(bn1[2][i],'<1>',lasty)
for i in range(3):
    dawg.tag_bind(bn1[3][i],'<1>',nexty)
#音量调节
scl=Scale(mod_sound,from_=1,to=0,resolution=0.1,variable=deca,command=sndaw,bg='#87cefa')
scl.set(1)
scl.pack()


#加载音乐文件----------------------
loadpt=os.getcwd()
if 'music' not in os.listdir(os.getcwd()):
    os.mkdir(loadpt+'\\music\\')
if 'line' not in os.listdir(os.getcwd()):
    os.mkdir(loadpt+'\\line\\')
loadpt_mc=loadpt+'\\music\\'
loadpt_ln=loadpt+'\\line\\'
namelst=os.listdir(loadpt_mc)
songlst=Listbox(mod_playlist,listvariable=item,width=40,height=16,bg='#c1ffc1',font=('仿宋',12,'bold'))
for i in namelst:
    songlst.insert('end',i)
songlst.grid()
songlst.bind('<Double-Button-1>',select)
sl_sgl=Scrollbar(mod_playlist,bg='#bcd2ee')
sl_sgl.grid(row=0,column=1,sticky=NW+SE)
songlst['yscrollcommand']=sl_sgl.set
sl_sgl['command']=songlst.yview
#加载歌词显示(txt类型)
contain='无歌词'
txts=Text(mod_lyrics,width=45,height=15,bg='#9aff9a',font=('宋体',10))
txts.insert('end',contain)
txts.grid()
sl_xs=Scrollbar(mod_lyrics,bg='#bcd2ee')
sl_xs.grid(row=0,column=1,sticky=NW+SE)
txts['yscrollcommand']=sl_xs.set
sl_xs['command']=txts.yview
#提示
tip=Label(dawg,text='您未选中任何歌曲，无法播放',font=('仿宋',16,''),bg='#eed2ee',fg='#eed2ee')
tip.place(x=480,y=380)

try:
    Music_Play()
except:
    pass

