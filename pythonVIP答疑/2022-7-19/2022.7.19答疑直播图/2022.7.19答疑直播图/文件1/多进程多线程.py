import os.path
import time
import requests
import concurrent.futures
import multiprocessing
import threading
baidu_urls = ['https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/']
def get_html(index, url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    html_data = response.text
    file_name = 'baidu_' + str(index) + '.html'
    return file_name, html_data

def save_html(file_name, html_data):
    if not os.path.exists('files'):
        os.mkdir('files')
    with open(f'files/{file_name}', mode='w', encoding='utf-8') as f:
        f.write(html_data)

def run(index, url):
    file_name, html_data = get_html(index, url)
    save_html(file_name, html_data)


if __name__ == '__main__':
    print('begin')
    start_time = time.time()
    for index, url in enumerate(baidu_urls, 1):
        multiprocessing.Process(target=run, args=(index, url)).start()
        # threading.Thread(target=run, args=(index, url)).start()

        # exe = concurrent.futures.ThreadPoolExecutor(max_workers=5)
        # exe = concurrent.futures.ProcessPoolExecutor(max_workers=5)
        # exe.submit(run, index, url)
    print('end')

    print(f'用时:\t {time.time() - start_time}')