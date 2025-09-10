# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
#  

import time
print(time.time())
print(time.localtime(1629547979))

import requests
# 使用列表存储的url,如何找到URL之间的规则 F8B7934E-896F-4771-87B6-B4DD92D23D55
urls=[
    'https://access.iisg.amsterdam/iiif/image/F8B7934E-896F-4771-87B6-B4DD92D23D55/full/200,/0/default.jpg?t=1629547979888',
    'https://access.iisg.amsterdam/iiif/image/93614AFB-BE86-47C7-A140-1A5C767481CB/full/200,/0/default.jpg?t=1629547979890',
    'https://access.iisg.amsterdam/iiif/image/264A6F64-202A-468C-9D9A-F200D9ADAD88/full/200,/0/default.jpg?t=1629547979892'
]
count=1
for item in urls:
    resp=requests.get(item)
    with open(str(count)+'.jpg','wb')as file:
        file.write(resp.content)
    count+=1