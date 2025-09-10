import wx
from socket import *
import threading
import time
class MsbServer(wx.Frame):

    def __init__(self):
        """创建窗口"""
        wx.Frame.__init__(self, None, id=102, title='老肖的服务器界面' ,pos=wx.DefaultPosition, size=(400, 470))
        p1 = wx.Panel(self)  # 在窗口中初始化一个面板
        # 在面板里面会放一些按钮，文本框，文本输入框等，把这些对象统一放入一个盒子里面
        box = wx.BoxSizer(wx.VERTICAL)  # 在盒子里面垂直方向自动排版

        g1 = wx.FlexGridSizer(wx.HORIZONTAL)
        start_server_button = wx.Button(p1, size=(133, 40), label="启动")
        record_save_button = wx.Button(p1, size=(133, 40), label="聊天记录保存")
        stop_server_button = wx.Button(p1, size=(133, 40), label="停止")
        g1.Add(start_server_button, 1, wx.TOP | wx.LEFT)
        g1.Add(record_save_button, 1, wx.TOP | wx.RIGHT)
        g1.Add(stop_server_button, 1, wx.TOP | wx.RIGHT)
        box.Add(g1, 1, wx.ALIGN_CENTER)

        self.text = wx.TextCtrl(p1, size=(400, 400), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.text, 1, wx.ALIGN_CENTER)
        p1.SetSizer(box)

        self.isOn=False
        self.host_port=('',8888)
        self.server_socket=socket(AF_INET,SOCK_STREAM)
        self.server_socket.bind(self.host_port)
        self.server_socket.listen(5)
        self.session_thread_map={}#存放所有的服务器绘画线程
        self.Bind(wx.EVT_BUTTON,self.start_server,start_server_button)
        self.Bind(wx.EVT_BUTTON, self.save_record,record_save_button)

    def start_server(self,event):

        print('服务器开始启动')
        if not self.isOn:
            self.isOn=True
            #启动服务器的主线程
            main_thread=threading.Thread(target=self.do_work)
            main_thread.setDaemon(True)#设置为守护线程
            main_thread.start()

    def do_work(self):
        print("服务器开始工作")
        while self.isOn:
            session_socket,client_addr=self.server_socket.accept()
            #服务器首先接收客户端噶过来的第一条消息，我们规定第一条消息为客户端的名字
            username=session_socket.recv(1024).decode('utf-8')#接收客户端名字
            #创建会话线程
            session_thread=SessionThread(session_socket,username,self)
            self.session_thread_map[username]=session_thread
            session_thread.start()
            self.show_info_and_send_client("服务器通知","欢迎%s进入聊天室！"%username,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        self.server_socket.close()

        #服务器端会话线程的类

    def show_info_and_send_client(self,source,data,data_time):
        send_data='%s:%s\n时间：%s\n'%(source,data,data_time)
        self.text.AppendText('-----------------------\n%s'%send_data)
        for client in self.session_thread_map.values():
            if client.isOn:
                client.user_socket.send(send_data.encode('utf-8'))
    def save_record(self,event):
        record=self.text.GetValue()
        with open("record.txt","w+") as f:
            f.write(record)

class SessionThread(threading.Thread):
    def __init__(self,socket,un,server):
        threading.Thread.__init__(self)
        self.user_socket=socket
        self.username=un
        self.server=server
        self.isOn = True  # 会话线程是否启动
    def run(self):
        print('客户端%s，已经和服务器连接成功，服务器启动一个会话线程'%self.username)
        while self.isOn:
            data=self.user_socket.recv(1024).decode('utf-8')
            if data=='A^disconnect^B':
                self.isOn=False
                self.server.show_info_and_send_client("服务器通知","%s离开聊天室！"%self.username,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
            else:
                self.server.show_info_and_send_client(self.username,data,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        self.user_socket.close()#保持和客户端会话的端口关闭
        # self.isOn=True#会话线程是否启动

if __name__ == '__main__':
    app = wx.App()
    MsbServer().Show()
    app.MainLoop()  # 循环刷新显示