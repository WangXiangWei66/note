# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="登录", size=(400, 300))
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel, label="输入用户名和密码", pos=(140, 20))
        self.label_user = wx.StaticText(panel, label="用户名", pos=(50, 50))
        self.text_user = wx.TextCtrl(panel, size=(235, 25), pos=(100, 50), style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label="密  码", pos=(50, 90))
        self.text_password = wx.TextCtrl(panel, size=(235, 25), pos=(100, 90), style=wx.TE_PASSWORD)
        # 设置按钮
        self.bt_confirm = wx.Button(panel, label='确定', pos=(150, 130))
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label='取消', pos=(255, 130))
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        self.bt_registered = wx.Button(panel, label='注册', pos=(45, 130))
        self.bt_registered.Bind(wx.EVT_BUTTON, self.OnclickResistered)

    def OnclickResistered(self, ever):
        """单机注册按钮，执行方法"""

# 函数与方法的区别

    def OnclickSubmit(self, evet):
        """单机确定按钮，执行方法"""
        message = ""
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()
        if username == "" or password == "":
            message = '用户名或密码不能为空'
        elif username == 'admin' and password == 'admin':
            message = '登录成功'
        else:
            message = '用户名和密码不匹配'
        wx.MessageBox(message)

    def OnclickCancel(self, event):
        """单机取消按钮，执行方法"""
        self.text_user.SetValue()
        self.text_password.SetValue()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()