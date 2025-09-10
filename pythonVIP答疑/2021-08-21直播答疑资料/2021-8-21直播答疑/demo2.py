# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
#  
import urllib.parse
import  requests
import json
import  time
#print(urllib.parse.quote('美女'))

#print(urllib.parse.quote('猫'))
keyword=input('请输入关键字')
qw=urllib.parse.quote(keyword) # 对输入的关键字进行编码，因为地址栏上的中文就进行了编码
url='https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8805771352609664149&ipn=rj&ct=201326592&is=&fp=result&queryWord='+qw+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word='+qw+'&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&nojc=&cg=girl&pn=30&rn=30&gsm=1e&1629549278102='

# 发送请求
#百度进行了反爬，所以要加请求头
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
resp=requests.get(url,headers=headers)
result=json.loads(resp.text) # 将文本str类型转成实际的数据类型，可能是字典
data_lst=result['data'] # 数据的列表
count=0
for item in data_lst: # 遍历的结果是个字典，
    img_url=item['thumbURL']
    # 向图片发送请求
    img_result=requests.get(img_url,headers=headers) # 结果为二进制数据

    with open('imge/'+str(count)+'.jpg','wb') as file:
        file.write(img_result.content) # 音频，视频，图片使用  响应对象.content
    count+=1
    time.sleep(5) # 单位毫秒 seconds
    print('第',count,'张图片，下载完成')