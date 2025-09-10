# _*_coding:utf-8_*_
# @Time: 2022/3/17  20:24
import re
import time
import csv
import os
import requests
import html

# 设置请求头  （防止反爬）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def comment_crawl(page, writer):
    '''爬取评论'''
    print('当前正在下载第%d页评论' % (page + 1))
    # 构建 请求的网页
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100000499657&score=0&sortType=5&page=%d&pageSize=10&isShadowSku=0&fold=1' % page
    # 请求链接获取数据
    text = requests.get(url, headers=headers).text
    # 正则表达式匹配数据  （提取数据）
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

        # 写入数据（写到csv文件【逗号分隔值】）
        writer.writerow((comment_time, score, reply_count, vote_count, image_count, content))


if __name__ == '__main__':
    '''主函数'''
    start = time.time()  # 获取当前的系统 时间
    if os.path.exists('DATA.csv'):  #判断 DATA.csv在当前目录下 是否存在
        os.remove('DATA.csv')    # 如果存在，就删除

    with open('DATA.csv', 'a+', newline='', encoding='gb18030') as f:  # 上下文管理器，不需要手动close()

        writer = csv.writer(f) # 创建csv的writer对象

        # 将标题 行写入文件
        writer.writerow(('留言时间', '评分', '回复数', '点赞数', '图片数', '评论内容'))

        # 爬取评论的页面数
        for page in range(3): # 这个页码数可以更改

            comment_crawl(page, writer)   # 调用爬取 ，并写入的方法


    run_time = time.time() - start  # 获取程序结时间

    print('运行时间为%d分钟%d秒。' % (run_time // 60, run_time % 60))  # 计算程序运行的时间
    print('运行时间为' ,run_time)  # 计算程序运行的时间