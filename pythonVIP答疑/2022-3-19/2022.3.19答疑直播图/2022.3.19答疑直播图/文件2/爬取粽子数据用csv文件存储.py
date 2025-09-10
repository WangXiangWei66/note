import requests
import json
import csv


def send_request():
    url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=43839390534&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/105'}
    resp = requests.get(url, headers=headers)
    return resp.text


def parse_html(data):  # 解析数据
    data = data.replace("fetchJSON_comment98(", "").replace(");", '')
    dict_data = json.loads(data)
    comments = dict_data["comments"]
    lst = []
    for comment in comments:
        print(comment)
        comment = comment["content"]
        time = comment['isDelete']
        lst.append([comment, time])
    save(lst)


def save(lst):
    with open("京东csv文件保存粽子数据.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(lst)


def start():
    data = send_request()
    parse_html(data)


if __name__ == '__main__':
    start()
