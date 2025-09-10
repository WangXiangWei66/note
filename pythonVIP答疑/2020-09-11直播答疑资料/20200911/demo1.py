#coding:utf-8
#教育机构 ：马士兵教育
#讲    师：杨淑娟
#写一段爬虫代码
import  requests
resp=requests.get('https://www.lingdianshuwu.com/')
resp.encoding='gbk'
print(resp.text)
# 1. 将百度的源码保存到本地存储 (Python中文件的操作)
file=open('lingdianshuwu.html','w',encoding='gbk')  # text是resp的属性  相当于 姓名是人的属性一样一样地  ,文本文件的后缀叫txt
file.write(resp.text)  #text 表示的是字符串
file.close()

#爬虫百度的图片
resp=requests.get('https://www.baidu.com/img/flexible/logo/pc/result.png')  #图片的url
file=open('logo.png','wb')
file.write(resp.content) # content表示的是二进制
file.close()




