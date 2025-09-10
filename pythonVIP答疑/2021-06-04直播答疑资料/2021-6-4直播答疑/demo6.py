# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import  requests
import sys,io
import  re
from lxml import etree
from bs4 import BeautifulSoup
from pyquery import PyQuery as pd
url='https://www.meishij.net/chufang/diy/?&page=1'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
# 响应结果 str类型的 html
# 爬取
def get_html(url):
    resp=requests.get(url,headers=headers)
    # 解决编码格式问题
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
    return  resp.text



#print(get_html(url)) # 控制台上输出的结是为str类型
print('-------------------------')
#print(type(get_html(url))) # <class 'str'>

# 响应结果为str类型 ，所以可 以使用正则表达式提取数据
def re_test(html): #html是形参
    result=re.findall('<img class="img" alt="(.*?)" src="(.*?)">',html)
    print(result) # 结果是列表类型


# 使用xpath
def xpath_test(html): # html --》str类型
    root=etree.HTML(html) # <class 'lxml.etree._Element'>
    src_lst=root.xpath('//img[@class="img"]//@src')
    alt_lst=root.xpath('//img[@class="img"]//@alt')
    print(src_lst)
    print(alt_lst)

# 使用bs提取数据  bs与xpath提取方式差不多，都 是根据节点元素去掉取 ,xpath效率高，因为xpath的底层是c
def bs_test(html):
    bs=BeautifulSoup(html,'lxml')
    img_lst=bs.find_all('img',class_='img')
    #print(type(img_lst)) #ResultSet
    for img in img_lst:
        #　img为Tag标签类型 ,获取标签的属性
        print(img['src'])
        print(img['alt'])

# 使用pyquery提取数据，要求对CSS非常熟悉

def pyquery_test(html):
    doc=pd(html) # 构造PyQuery的对象
   # print(type(doc))<class 'pyquery.pyquery.PyQuery'>
    #               img标签  .img 是类样式
    img_lst=doc('div.listtyle1 a').find('img.img').items()

    #print(img_lst) #<generator object PyQuery.items at 0x00000200C88F9820>
    for item in img_lst:
        print(item.attr('src'),item.attr('alt'))
pyquery_test(get_html(url))

#（１）　响应结果是str使用正则
# (2) xpath,bs 都是将str转成元素对象类型，但是xpath快
# （3）pyquery, 要求对CSS非常熟悉
