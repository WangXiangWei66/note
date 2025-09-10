# coding:utf-8
# author:杨淑娟
import requests
from lxml import  etree
#url='https://www.icourse163.org/channel/3002.htm?cate=-1&subCate=-1'
url='https://www.icourse163.org/web/j/channelBean.getCustomCourseModuleVo.rpc?csrfKey=fdc77d88ee0d48aebfa9f07059a172eb'
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
resp=requests.post(url,headers=headers)
print(resp.text)
#
# e=etree.HTML(resp.text)
# text=e.xpath('//div[@class="Y8tgZ"]/div[1]')
# print(text)
