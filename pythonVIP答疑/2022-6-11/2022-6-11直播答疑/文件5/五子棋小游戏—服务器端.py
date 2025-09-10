#基于UDP的网络五子棋游戏
#服务器端  白子 后出子
from tkinter import *
from tkinter.messagebox import *
import socket
import threading
import os

root = Tk()
root.title("网络五子棋——服务器端")
imgs = [PhotoImage(file='./img/BlackStone.png'),
        PhotoImage(file='./img/WhiteStone.png')]
turn = 0
Myturn = -1

def callexit(event):  #退出
    pos='exit|'
    sendMessage(pos)
    os._exit(0)

#走棋
def callpos(event):
    global turn
    global Myturn
    if Myturn == -1:
        Myturn = turn
    else:
        if(Myturn!=turn):
            showinfo(title="提示", message="还未轮到您走棋！")
            return
    x = (event.x) // 40  #换算棋盘坐标，除以像素
    y = (event.y) // 40
    print("click at", x, y, turn)
    if map[x][y]!=" ":
        showinfo(title="提示", message="此处已有棋子！")
    else:
        img1 = imgs[turn]
        cv.create_image((x*40+20, y*40+20), image = img1)
        cv.pack()
        map[x][y] = str(turn)
        pos = str(x)+","+str(y)
        sendMessage("move|"+pos)
        print("服务器走的位置:", pos)
        lbl1["text"]="服务器走的位置:"+pos

        if CheckWin(x, y)==True:
            if turn==0:
                showinfo(title="提示", message="黑方你赢了！")
                sendMessage("over|黑方赢了")
            else:
                showinfo(title="提示", message="白方你赢了！")
                sendMessage("over|白方你赢了")
        if turn == 0:
            turn = 1
        else:
            turn = 0

def drawOtherChess(x, y):
    global turn
    img1 = imgs[turn]
    cv.create_image((x*40+20, y*40+20),image = img1)
    cv.pack()
    map[x][y] = str(turn)

    if turn == 0:
        turn = 1
    else:
        turn = 0

def drawQipan():
    for i in range(15):
        cv.create_line(20 + 40 * i, 20, 20 + 40 * i, 580)
        cv.create_line(20, 20 + 40 * i, 580, 20 + 40 * i)
    cv.create_oval(135, 135, 145, 145, fill = 'black')
    cv.create_oval(135, 455, 145, 465, fill='black')
    cv.create_oval(465, 135, 455, 145, fill='black')
    cv.create_oval(455, 455, 465, 465, fill='black')
    cv.create_oval(295, 295, 305, 305, fill='black')
    cv.pack()

def CheckWin(x,y):  #判断输赢
    flag = False
    count = 1
    color = map[x][y]
    #横向判断
    i = 1
    while color == map[x + i][y]:
        count = count + 1
        i = i + 1
    i = 1
    while color == map[x - i][y]:
        count = count + 1
        i = i + 1
    if count >= 5:
        flag = True

    # 纵向判断
    i2 = 1
    count2 = 1
    while color == map[x][y + i2]:
        count2 = count2 + 1
        i2 = i2 + 1
    i2 = 1
    while color == map[x][y - i2]:
        count2 = count2 + 1
        i2 = i2 + 1
    if count2 >= 5:
        flag = True

    # y=x方向判断
    i3 = 1
    count3 = 1
    while color == map[x + i3][y - i3]:
        count3 = count3 + 1
        i3 = i3 + 1
    i3 = 1
    while color == map[x - i3][y + i3]:
        count3 = count3 + 1
        i3 = i3 + 1
    if count3 >= 5:
        flag = True

    # y=-x方向判断
    i4 = 1
    count4 = 1
    while color == map[x + i4][y + i4]:
        count4 = count4 + 1
        i4 = i4 + 1
    i4 = 1
    while color == map[x - i4][y - i4]:
        count4 = count4 + 1
        i4 = i4 + 1
    if count4 >= 5:
        flag = True

    return flag

def print_map():
    for j in range(15):
        for i in range(15):
            print (map[i][j], end=' ')
        print("w")

def receiveMessage():  #接受客户发来的消息
    global s
    while True:
        global addr
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        a = data.split("|")
        if not data:
            print("Client has exited!")
            break
        elif a[0] == 'join':
            print("Client has linked!")
            lbl1['text'] = "Client has linked! 请您走棋！"
        elif a[0] == 'exit':
            print("Client has exited!")
            lbl1['text'] = "Client has exited! 游戏结束！"
        elif a[0] == 'over':
            print("对方获胜!")
            lbl1['text'] = data.split("|")[0]
            showinfo(title="提示", message = data.split("|")[1])
        elif a[0] == 'move':
            print('received:', data, 'from', addr)
            p = a[1].split(",")
            x = int(p[0])
            y = int(p[1])
            print(p[0], p[1])
            lbl1["text"] = "客户端走的位置:"+p[0]+','+p[1]
            drawOtherChess(x, y)
    s.close()

def sendMessage(pos):  #发送消息
    global s
    global addr
    s.sendto(pos.encode(), addr)

def startNewThread():
    thread = threading.Thread(target = receiveMessage, args=())
    thread.Daemon = True
    thread.start()


map = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]for y in range(15)]
cv = Canvas(root, bg='peru', width=600, height=600)
drawQipan()
cv.bind("<Button-1>", callpos)
cv.pack()
lbl1 = Label(root, text = "服务器端", bg='silver')
lbl1.pack()
btn1 = Button(root, text = "退出游戏")
btn1.bind("<Button-1>", callexit)
btn1.pack()
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost', 8000))
addr = ('localhost', 8000)
startNewThread()
#receiveMessage()
root.mainloop()

