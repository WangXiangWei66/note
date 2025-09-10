# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

import requests
start_url="https://www.zhihu.com/api/v4/members/lisanshui1230/articles"
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"

}
resp=requests.get(start_url,headers=headers)
print(resp.text)
data=resp.json()
print(data)
