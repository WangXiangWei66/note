# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 安装pip intall wxpython

import wx
import jieba
import pandas    # 安装方式  pip install pandas
import matplotlib.pyplot as plt  # 安装方式 pip install matplotlib
#使用面向对象的方式编写
# 面向对象三大特征，封装，继承，多态 【与语言无关】
class MyFrame(wx.Frame): # 继承
    #编写初始化的函数
    def __init__(self,parent,id):
        #调用父类的初始化函数  ,窗体的大小，x=800像素，y=600像素
        wx.Frame.__init__(self,parent,id,title='中文小说',size=(800,600))
        #创建面板 (一个容器)
        self.panel=wx.Panel(self)
        # 创建一个按钮和一个多行文本框
        self.open_story=wx.Button(self.panel,label='打开小说',pos=(50,50))
        # 多行文本框
        self.text_story=wx.TextCtrl(self.panel,pos=(50,100),style=wx.TE_MULTILINE,size=(600,400))

        #添加 两个按钮，一个按钮生成柱状图，一个按钮生成饼图
        self.bar = wx.Button(self.panel, label='柱状图', pos=(150, 50)) # 距离窗体左侧的距离150

        self.pie = wx.Button(self.panel, label='饼图', pos=(250, 50)) #距离窗体上面的距离５０

        # 为按钮绑定单击事件
        self.open_story.Bind(wx.EVT_BUTTON,self.OnclickOpen) #self.OnclickOpen自定义的方法

        # 点击柱状图的按钮，生成柱状图
        self.bar.Bind(wx.EVT_BUTTON, self.OnclickBar)

        # 点击饼图的铵钮，生成饼图
        self.pie.Bind(wx.EVT_BUTTON, self.OnclickPie)

    # 获取数据源的方法
    def get_data(self):
        # 数据分析中的，数据可视化
        with open('告别日落.txt', 'r') as file:
            s = file.read()  # 读取全部内容

        lst = jieba.lcut(s)  #
        # print(len(lst)) # 清洗之前词的长度
        # print(lst)
        # 清洗
        # for item in lst:
        #     if len(item)<2 or item=='\u3000' or item=='\n':
        #         lst.remove(item)
        # print(len(lst)) # 清洗之后词的长度

        # 统计词语的个数

        s = set(lst)  # 将lst转成集合 ，去重
        # 统计个数
        d = {}  # key是词，value是词出现的次数
        for item in s:
            d[item] = 0  # 所有键所对象的次数都是0

        # 遍历列表
        for item in lst:
            if item in d:
                d[item] = d.get(item) + 1  # 给键赋值

        # print(d)

        # 转成列表, 每个小列表中有两个元素【key,value】
        new_lst = []

        for item in d:
            if len(item) >= 2:  # 组成词语的中文字数，大于等于2个
                new_lst.append([item, d.get(item)])

        # 对列表进行排序  x是new_lst中的元素，
        new_lst.sort(key=lambda x: x[1], reverse=True)  # 降序，排序的规则，使用小列表中的个数排序

        # print(new_lst)
        new_lst = new_lst[:11]  # 切片获取前10项
        return new_lst
    def OnclickBar(self,event):

       new_lst=self.get_data()

       # 设置画布大小
       plt.figure(figsize=(10, 6))

       # 解决中文乱码
       plt.rcParams['font.sans-serif'] = ['SimHei']

       # 设置x轴和y轴数据
       x_lst = []  # 词语是x轴
       y_lst = []  # 词语出现的次数是y轴

       for item in new_lst:
           x_lst.append(item[0])  # 添加x轴的数据
           y_lst.append(item[1])  # 添加y轴的数据

       x = pandas.Series(x_lst)  # 将列表转成Series类型
       height = pandas.Series(y_lst)

       # 柱子上现出次数
       for a, b in zip(x, height):
           plt.text(a, b, format(b, ','), ha='center', va='center', fontsize=12, color='b', alpha=0.9)
       # 绘图
       plt.bar(x, height, width=0.5, alpha=0.5)

       plt.show()  # 显示

    def OnclickPie(self,event):
       # #数据分析中的，数据可视化
        new_lst=self.get_data()  # 获取数据源
       # 设置画布大小

        plt.figure(figsize=(10, 6))

        # 解决中文乱码
        plt.rcParams['font.sans-serif'] = ['SimHei']

        # 设置x轴和y轴数据
        x_lst = []  # 词语是x轴
        y_lst = []  # 词语出现的次数是y轴

        for item in new_lst:
            x_lst.append(item[0])  # 添加x轴的数据
            y_lst.append(item[1])  # 添加y轴的数据

        label = pandas.Series(x_lst)  # 将列表转成Series类型
        x = pandas.Series(y_lst)

        # 开始画饼图
        plt.pie(x,labels=label,autopct='%1.1f%%')

        plt.show()

    def OnclickOpen(self,event):
        self.text_story.write('') #先把原来内容清掉，再执行写入
        #print('写代码') # 文件读取的代码
        with open('告别日落.txt','r') as file:  #第十五章　文件及IO操作
            s=file.read()
            #print(s)
            #将小说内容显示到多行文本框中
            self.text_story.write(s) # 将字符串s中的数据写入到多行文本框



# 以主函数运行
if __name__ == '__main__':
    app=wx.App()   #初始化应用
    frame=MyFrame(parent=None,id=-1) # 自动生成一个id
    frame.Show() #显示窗体
    app.MainLoop()


