#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import wx
def load(event):
    file = open(filename.GetValue(),'r')
    contents.SetValue(file.read())
    file.close()


def save(event):
    file = open(filename.GetValue(), 'w')
    file.write(contents.GetValue())
    file.close()
                           #导入wx包
app = wx.App()                          #创建应用程序对象
win = wx.Frame(None,-1,'install test')  #创建窗体

bkg = wx.Panel(win)
openBtn = wx.Button(bkg,label='Open')  #添加按钮
saveBtn = wx.Button(bkg,label='Save')
filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)

hbox = wx.BoxSizer(wx.HORIZONTAL)
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(openBtn, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveBtn, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
vbox.Add(contents,proportion=1, flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT, border=5)

openBtn.Bind(wx.EVT_BUTTON, load)
saveBtn.Bind(wx.EVT_BUTTON, save)

bkg.SetSizer(vbox)
win.Show()                              #显示窗体
app.MainLoop()


