#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import requests
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
count=1
for i in range(0,4):
    #f表示的是format格式化字符串
    url=f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9699664265808794570&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%B0%8F%E5%B2%B3%E5%B2%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%B0%8F%E5%B2%B3%E5%B2%B3&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&nojc=&pn={i*30}&rn=30&gsm=3c&1626524595433='
    # 发送请示
    resp=requests.get(url,headers=headers)
    # 进行类型转换，将str类型转成json类型
    result=resp.json() #result是字典类型 ，根据key获取值
    lst=result['data'] # lst列表中的每个元素都是一个字典
    for item in lst: # 遍历这个列表 ，item就是遍历出来的每一个字典
        # 根据key获取值
       # img_url=item['thumbURL']  # 结果为图片的url
        img_url=item.get('thumbURL')
        if img_url!=None:
            # 向图片的url继续发送请求
            resp_img=requests.get(img_url,headers=headers) # 向图片发送请求，响应结果是一张图片，图片是二进制数据
            # 把图片保存到本地磁盘  ， IO流，读写数据
            with open('image/'+str(count)+'.jpg','wb') as file:
                file.write(resp_img.content)
            print('图片'+str(count)+'保存完成')
        count+=1
            




