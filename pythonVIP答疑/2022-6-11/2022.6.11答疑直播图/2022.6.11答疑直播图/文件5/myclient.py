import wx
from socket import *
import threading

class MsbClient(wx.Frame):
    def __init__(self,c_name):
        wx.Frame.__init__(self,None,id=101,title='%s的客户端界面'%c_name,pos=wx.DefaultPosition,size=(400,470))
        p1=wx.Panel(self)#在窗口中初始化一个面板
        #在面板里面会放一些按钮，文本框，文本输入框等，把这些对象统一放入一个盒子里面
        box=wx.BoxSizer(wx.VERTICAL)#在盒子里面垂直方向自动排版

        g1=wx.FlexGridSizer(wx.HORIZONTAL)
        conn_button=wx.Button(p1,size=(200,40),label="连接")
        dis_conn_button=wx.Button(p1,size=(200,40),label="断开")
        g1.Add(conn_button,1,wx.TOP|wx.LEFT)
        g1.Add(dis_conn_button,1,wx.TOP|wx.RIGHT)
        box.Add(g1,1,wx.ALIGN_CENTER)

        #创建聊天内容的文本框，不能写消息
        self.text = wx.TextCtrl(p1, size=(400, 250), style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.text, 1, wx.ALIGN_CENTER)                              #创建聊天文本框，可以写
        self.input_text = wx.TextCtrl(p1, size=(400, 100), style=wx.TE_MULTILINE)
        box.Add(self.input_text, 1, wx.ALIGN_CENTER)
        #最后创建两个按钮，分别发送和充值
        g2 = wx.FlexGridSizer(wx.HORIZONTAL)
        clear_button = wx.Button(p1, size=(200, 40), label="重置")
        send_button = wx.Button(p1, size=(200, 40), label="发送")
        g2.Add(clear_button,1,wx.TOP|wx.LEFT)
        g2.Add(send_button,1,wx.TOP|wx.RIGHT)
        box.Add(g2,1,wx.ALIGN_CENTER)

        p1.SetSizer(box)
        '''以上代码完成了客户端界面（窗口）'''
        self.Bind(wx.EVT_BUTTON,self.connect_to_server,conn_button)
        self.Bind(wx.EVT_BUTTON,self.send_to,send_button)
        self.Bind(wx.EVT_BUTTON,self.go_out,dis_conn_button)
        self.Bind(wx.EVT_BUTTON, self.reset,clear_button)
        self.name=c_name
        self.isConnected=False
        self.client_socket=None
    def connect_to_server(self,event):
        print("客户端%s，开始连接服务器"%self.name)
        if not self.isConnected:
            server_host_port=('Localhost',8888)
            self.client_socket=socket(AF_INET,SOCK_STREAM)
            self.client_socket.connect(server_host_port)
            self.client_socket.send(self.name.encode('utf-8'))
            t=threading.Thread(target=self.receive_data)
            t.setDaemon(True)
            self.isConnected=True
            t.start()

    def receive_data(self):
        print("客户端准备接收服务器数据")
        while self.isConnected:
            data=self.client_socket.recv(1024).decode('utf-8')
            self.text.AppendText('%s\n'%data)
    def send_to(self,event):
        if self.isConnected:
            info=self.input_text.GetValue()
            if info!='':
                self.client_socket.send(info.encode('utf-8'))
                self.input_text.SetValue('')
    def go_out(self,event):
        self.client_socket.send('A^disconnect^B'.encode('utf-8'))
        self.isConnected=False

    def reset(self,event):
        self.input_text.Clear()

if __name__ == '__main__':
    app=wx.App()
    name=input("请输入客户端名字：")
    MsbClient(name).Show()
    app.MainLoop()#循环刷新显示



