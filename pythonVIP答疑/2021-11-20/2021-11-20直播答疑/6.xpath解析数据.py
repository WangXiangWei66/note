# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
from lxml import  etree
s='''<html>
    <head><title>百度一下，就知道</title></head>
    <body>
        <div>
             <h1>欢迎来到马士兵教育</h1>
        </div>
        <div class="main-text">
            大家好，我是Python娟子姐
            <p>每周六直播答疑不见不散</p>
        </div>
        <div>
            <h4>北京市海淀区</h4>
        </div>
    </body>
</html>
'''
e=etree.HTML(s)
a=e.xpath('//div[@class="main-text"]/text()')

b=e.xpath('//div[@class="main-text"]//text()')

print(a)
print('-----------------')
print(b)
