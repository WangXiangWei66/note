# coding:utf-8
# author:杨淑娟
import  requests
from  bs4 import BeautifulSoup
import mysql.connector
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
class LianjiaSpider():
    def __init__(self):#初始化方法
        self.url='https://bj.lianjia.com/ershoufang/pg{0}/'
        self.headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
                      'Cookie': 'lianjia_uuid=b5a8a48d-f73b-43a4-983f-99c4870f7afa; UM_distinctid=17ee7bd9e00277-02812bd0a091dc-3e644204-1bcab9-17ee7bd9e01d3e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ee7bd9ef1266-047a7a00479167-3e644204-1821369-17ee7bd9ef2e63%22%2C%22%24device_id%22%3A%2217ee7bd9ef1266-047a7a00479167-3e644204-1821369-17ee7bd9ef2e63%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.1378332734.1644565474; _smt_uid=620613e5.1f76779b; _jzqx=1.1653623246.1653623246.1.jzqsr=tj%2Elianjia%2Ecom|jzqct=/ershoufang/c1220039349603132/.-; select_city=360700; lianjia_ssid=2d7bb140-1845-4cf0-8d32-ef632e15f66e; _jzqckmp=1; _gid=GA1.2.1834702161.1659187734; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1658992810,1659187776,1659188379; _qzjc=1; _jzqa=1.2154745539045989600.1653621249.1659187732.1659188379.8; _jzqc=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _qzja=1.1983872435.1659187731939.1659187731939.1659188378635.1659188378635.1659188383898.0.0.0.7.2; _qzjb=1.1659187731939.7.0.0.0; _qzjto=7.2.0; _jzqb=1.2.10.1659188379.1; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1659188384; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMzM4NWE3NjlkM2FkZWIzY2Q1ZDcwYzRlNjBhMjEwMjYwNDdhZjVjNjhhMTQ3ZWVjMjNkNjE5MTgzYjc1NTZkZDQ0OGQ5OGMxMDk4ZTExMzRlNDY0NWNhNjkyYWU5MGQ3ZGQ2YjMyNTU1MjhkZGM3MDgwOGNmNDk2N2Y1ODE2MDlmOWRlMGU2ZWQ1NmVlOGVlOTI4MjA5ZmI4MTU4YzViMGFjNzg1ZjBjNmI2OWU0OTMxNDRlZDEyN2FkZmZkM2VkNzIzNGJmNjJjY2I3NGEwN2Y1ZDczMjc1MjA3Zjg1OGE4ZGZjZDQ3MDI0ZjQwNjQ5YTY3Y2IwODZhNDE1NmI3MFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJkZmQ0NjA5NlwifSIsInIiOiJodHRwczovL2dhbnpob3UubGlhbmppYS5jb20vZXJzaG91ZmFuZy9wZzEvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='}
    def send_request(self,url):#发送请求
        resp=requests.get(url,headers=self.headers)
        if resp.status_code==200:
            return resp

    def parse_html(self):#数据解析
        pass
    def start(self):#数据保存
        for i in range(1,2):
            full_url=self.url.format(i)
            resp=self.send_request(full_url)
            print(resp.text)
if __name__ == '__main__':
    lianjia=LianjiaSpider()
    lianjia.start()