import threading

import requests
import parsel
lock = threading.Lock()
def get_text(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    response = requests.get(url=url, headers=headers).text
    return response

def parse_data(response):
    data_list=[]
    selector = parsel.Selector(response)
    comment_list = selector.css('.comment-item')
    for comment in comment_list:
        name = comment.css('.comment-info a::text').get().strip()
        time = comment.css('.comment-time::text').get().strip()
        content = comment.css('.short::text').get().strip()
        vote_count = comment.css('.votes.vote-count::text').get().strip()
        data_list.append([name, time, content, vote_count])
    return data_list

def save_data(data_list):
    lock.acquire()
    with open('长津湖.txt', mode='a', encoding='utf-8', newline='') as f:
        f.write(data_list)
    lock.release()


def main():
    urls = ['https://movie.douban.com/subject/35613853/comments?start={}&limit=20&status=P&sort=time'.format(page * 20)for page in range(10)]
    for url in urls:
        html_data=get_text(url)
        data_list=parse_data(html_data)
        txt=save_data(data_list)
        print(txt)


if __name__ == '__main__':
    t1 = threading.Thread(target=main).start()
    t2 = threading.Thread(target=main).start()
