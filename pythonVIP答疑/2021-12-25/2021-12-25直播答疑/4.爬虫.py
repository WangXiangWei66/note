# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import requests
url='https://wenshu.court.gov.cn/website/wenshu/181010CARHS5BS3C/index.html?https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=4f15c85351194fe008f5530ecca2febe&s8=04'

resp=requests.get(url)
print(resp.text)


#爬虫使用的第三方模块叫requests
import  requests as pp   # pp就是别名 ，下次再使用是可以直接使用pp
resp=pp.get(url)
