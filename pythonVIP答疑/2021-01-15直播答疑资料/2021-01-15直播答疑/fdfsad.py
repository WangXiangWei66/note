# 教育机构：马士兵教育
# 讲    师：杨淑娟
#爬虫 ，发送请求，需要使用的第三方库叫requests
import requests
import json  #JSON模块
url='https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10781560497821027116&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E7%BE%8E%E5%A5%B3&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=girl&pn=30&rn=30&gsm=1e&1610715673698='
# 百度图库可能会的反爬虫，模拟浏览器的操作，添加一个请求头
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

#发送请滶
resp=requests.get(url,headers=headers)
print(type(resp.text)) #str类型

#print(resp.text)   输出的字符串是由{}开始和结束的，有两种处理方式
#(1)使用response自带的json方法
# data=resp.json()  #得到的是dict类型  ,使用eval()报错.  null...
# print(type(data))
#(2)使用的json模块的loads方法
data=json.loads(resp.text)  # dict类型
print(type(data))

# s='{"name":"张三"}' #JSON格式的字符
# print(type(s)) #str类型
# data=eval(s) #  #（2）使用eval()的函数，去掉字符串左右的引号得到实际的数据类型
# print(type(data))
#

#数据格式转换完成之后，要进行数据提取
lst=data['data'] #结果为列表， 遍历列表中的每个元素，每个元素的数据类型又是一个字字典
image_urls=[]
for item in lst:  #每一个item就是一个字典
    img_url=item.get('thumbURL')  #item['thumbURL']结果出现KeyError: 说明thumbURL键不存在,解决方案，可以使用
       # 方法get从字典中获取元素，None
    if img_url!=None:

        #print(img_url)
        image_urls.append(img_url) #将图片的Url存储到列表中

#发请求，请求图片
count=1
for item in image_urls:
    img_rep=requests.get(item,headers=headers) #图片是一个二进制数据，使用content ，响应对象的content
    # 保存到本地
    with open('img/'+str(count)+'.jpg','wb') as f:
        f.write(img_rep.content)
    count+=1


