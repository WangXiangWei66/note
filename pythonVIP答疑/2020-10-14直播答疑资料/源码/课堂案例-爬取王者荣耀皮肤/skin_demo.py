#教育机构 ：马士兵教育
#讲    师：杨淑娟
'''https://pvp.qq.com/web201605/js/herolist.json'''
import requests  #第三方库（用于发送请求的）
import json   #第三方库
resp=requests.get('https://pvp.qq.com/web201605/js/herolist.json')
print(resp.text)
#print(type(resp.text))  #<class 'str'>  resp.text的结果为str字符串类型


json_data=json.loads(resp.text)  #类型转换 将str-->list

#print(type(json_data))   #<class 'list'>

for  hero in  json_data:   #从列表中找到每个英雄的数据 （字典）
   id= hero['ename']  #英雄的编号
   name=hero['cname'] #英雄的名称
   img_resp=requests.get(f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{id}/{id}-bigskin-1.jpg')
   content=img_resp.content  #从响应结果获取二进制数据(在这里表示的是图片数据)
   #在本地进行存储  'skin/'+name+'.jpg'拼接图片保存的路径和名称
   with open('skin/'+name+'.jpg','wb')as file :
       file.write(content)









