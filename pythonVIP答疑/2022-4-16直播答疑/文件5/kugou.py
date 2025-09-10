# _*_coding:utf-8_*_
# @Time: 2022/4/14  19:46
import json, requests
from lxml import etree

base_url = 'https://www.kugou.com/yy/singer/index/%s-%s-1.html'
# ---------------通过url获取该页面的内容，返回xpath对象
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


# ---------------通过url获取该页面的内容，返回xpath对象
def get_xpath(url, headers):
    try:
        response = requests.get(url, headers=headers)
        return etree.HTML(response.text)
    except Exception:
        print(url, '该页面没有相应！')
        return ''


# --------------------通过歌手详情页获取歌手简介
def parse_info(url):
    html = get_xpath(url, headers)
    info = html.xpath('//div[@class="intro"]/p/text()')
    return info


# --------------------------写入方法
def write_json(value):
    with open('kugou.json', 'a+', encoding='utf-8') as file:
        json.dump(value, file,ensure_ascii=False,indent=4)
        #json.dump(value, file)

# -----------------------------用ASCII码值来变换abcd...
for j in range(97, 124):
    # 小写字母为97-122，当等于123的时候我们按歌手名单的其他算，路由为null
    if j < 123:
        p = chr(j)
    else:
        p = "null"
    for i in range(1, 6):
        response = requests.get(base_url % (i, p), headers=headers)
        # print(response.text)
        html = etree.HTML(response.text)
        # 由于数据分两个url，所以需要加起来数据列表
        name_list1 = html.xpath('//ul[@id="list_head"]/li/strong/a/text()')
        sing_list1 = html.xpath('//ul[@id="list_head"]/li/strong/a/@href')
        name_list2 = html.xpath('//div[@id="list1"]/ul/li/a/text()')
        sing_list2 = html.xpath('//div[@id="list1"]/ul/li/a/@href')
        singer_name_list = name_list1 + name_list2
        singer_sing_list = sing_list1 + sing_list2
        # print(singer_name_list,singer_sing_list)
        for i, name in enumerate(singer_sing_list):
            item = {}
            item['名字'] = name
            item['歌单'] = singer_name_list[i]
            write_json(item)
