# -*- coding: UTF-8 -*-
# 文件名  : demo_1.py



# url = 'https://wenku.baidu.com/view/dcfab8bff705cc175527096e.html'

import json
import requests
import re
from selenium import webdriver
import time


def open_url(url):
    print('开始自动查询网页')
    browser = webdriver.Chrome()

    browser.get(url)
    print('等待5秒')
    time.sleep(2)

    # 下面这个语句并不是查找“继续阅读”按钮所在位置，而是更上面的元素，因为按照原本元素位置滑动窗口会遮挡住
    eles = browser.find_element_by_xpath('//*[@id="html-reader-go-more"]/div[1]/div[3]/div[1]')
    browser.execute_script('arguments[0].scrollIntoView();', eles)
    print('等待2秒')
    time.sleep(2)

    # 点击“继续阅读”按钮
    browser.find_element_by_xpath('//*[@id="html-reader-go-more"]/div[2]/div[1]/span/span[2]').click()
    print('已显示文档所有内容')


def fetch_url(url):
    '''网页源代码'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    session = requests.session()
    resp = session.get(url, headers=headers).content.decode('utf8')
    return resp


def get_id(resp):
    url_id = re.findall(r"docId.*?\:.*?\'(.*?)\'\,", resp)[0]
    return url_id


def get_type(resp):
    url_type = re.findall(r"docType.*?\:.*?\'(.*?)\'\,", resp)[0]
    return url_type


def get_title(resp):
    url_title = re.findall(r"title.*?\:.*?\'(.*?)\'\,", resp)[0]
    return url_title


def parse_txt(id):
    '''id: 之前爬取的 docid'''

    url1 = 'https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id={}'.format(id)
    content1 = fetch_url(url1)
    md5 = re.findall('"md5sum":"(.*?)"', content1)[0]
    pn = re.findall('"totalPageNum":"(.*?)"', content1)[0]
    rsign = re.findall('"rsign":"(.*?)"', content1)[0]

    url2 = 'https://wkretype.bdimg.com/retype/text/' + id + '?rn=' + pn + '&type=txt' + md5 + '&rsign=' + rsign
    content2 = json.loads(fetch_url(url2))
    result = ''
    for items in content2:
        for item in items:
            result = result + item['c'].replace('\\r', '\r').replace('\\n', '\n')
    return result


def save_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        print('已保存为:' + filename)


def parse_doc(content):
    result = ''
    url_list = re.findall('(https.*?0.json.*?)\\\\x22}', content)
    url_list = [addr.replace("\\\\\\/", "/") for addr in url_list]
    for url in url_list[:-5]:
        content = fetch_url(url)
        y = 0
        txtlists = re.findall('"c":"(.*?)".*?"y":(.*?),', content)
        for item in txtlists:
            if not y == item[1]:
                y = item[1]
                n = '\n'
            else:
                n = ''
            result += n
            result += item[0].encode('utf-8').decode('unicode_escape', 'ignore')
    return result


def main():
    url1 = input('请输入需要爬取的文库地址:')
    # open_url(url1)
    resp = fetch_url(url1)
    Id = get_id(resp)
    Type = get_type(resp)
    Title = get_title(resp)
    if Type == 'txt':
        result = parse_txt(Id)
        save_file(Title + '.txt', result)
    elif Type == 'doc':
        result = parse_doc(resp)
        save_file(Title + '.doc', result)


if __name__ == '__main__':
    main()