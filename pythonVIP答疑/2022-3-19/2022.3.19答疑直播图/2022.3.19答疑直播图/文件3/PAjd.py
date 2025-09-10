# _*_coding:utf-8_*_
# @Time: 2022/3/17  20:24
import re
import time
import csv
import os
import requests
import html

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def comment_crawl(page, writer):
    '''爬取评论'''
    print('当前正在下载第%d页评论' % (page + 1))
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100000499657&score=0&sortType=5&page=%d&pageSize=10&isShadowSku=0&fold=1' % page
    # 请求链接获取数据
    text = requests.get(url, headers=headers).text
    # 正则表达式匹配数据
    comment_list = re.findall(
        r'guid":".*?"content":"(.*?)".*?"creationTime":"(.*?)",".*?"replyCount":(\d+),"score":(\d+).*?usefulVoteCount":(\d+).*?imageCount":(\d+).*?images":',
        text)
    for result in comment_list:
        # 根据正则表达式结果匹配数据
        content = html.unescape(result[0]).replace('\n', ' ')
        comment_time = result[1]
        reply_count = result[2]
        score = result[3]
        vote_count = result[4]
        image_count = result[5]
        # 写入数据
        writer.writerow((comment_time, score, reply_count, vote_count, image_count, content))


if __name__ == '__main__':
    '''主函数'''
    start = time.time()
    if os.path.exists('DATA.csv'):
        os.remove('DATA.csv')
    with open('DATA.csv', 'a+', newline='', encoding='gb18030') as f:
        writer = csv.writer(f)
        writer.writerow(('留言时间', '评分', '回复数', '点赞数', '图片数', '评论内容'))
        for page in range(100):
            comment_crawl(page, writer)
    run_time = time.time() - start
    print('运行时间为%d分钟%d秒。' % (run_time // 60, run_time % 60))
