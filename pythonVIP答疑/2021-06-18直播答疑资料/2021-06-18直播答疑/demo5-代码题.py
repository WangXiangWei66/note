#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import requests
from lxml import etree
lst=[]
dd=0
for item in range(219,300):
    url=f'https://pic.netbian.com/new/index_{item}.html'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Referer': 'https://pic.netbian.com/'}
    resp=requests.get(url,headers=headers)
    resp.encoding='gbk'
    #print(resp.text)
    e=etree.HTML(resp.text)
    urll=e.xpath('//ul[@class="clearfix"]/li/a/@href')
    #print(urll)
    for it in urll:
        a='https://pic.netbian.com'+it

        url=a
        respp = requests.get(url, headers=headers)
        d=etree.HTML(respp.text)
        url3=d.xpath('//div[@class="photo-pic"]/a/img/@src')
    for i in url3:
        k='https://pic.netbian.com'+i
        print(a)
        url_=k
        resp=requests.get(url_,headers=headers)
        # d = 0
        # for ii in resp:
        #     d += 1
        #print(resp)'''
        with open('picture/'+str(dd)+'_图片_'+'.jpg','wb')as file:
            file.write(resp.content)
        print('正在下载第%d张'% dd)
        dd+=1
print('下载完成')


