# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------

# 请求头列表
USER_AGENT_LIST = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Hot Lingo 2.0)',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3451.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2999.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.70 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.1.4322; MS-RTC LM 8; InfoPath.2; Tablet PC 2.0)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 TheWorld 7',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 OPR/55.0.2994.61',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; .NET4.0C; CIBA; Maxthon 2.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; Touch; MASMJS)',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Hot Lingo 2.0)',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3451.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2999.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.70 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.1.4322; MS-RTC LM 8; InfoPath.2; Tablet PC 2.0)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 TheWorld 7',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 OPR/55.0.2994.61',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; .NET4.0C; CIBA; Maxthon 2.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; Touch; MASMJS)',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4093.3 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Swurl) Chrome/77.0.3865.120 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Goanna/4.7 Firefox/68.0 PaleMoon/28.16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/91.0.146 Chrome/85.0.4183.146 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 VivoBrowser/8.4.72.0 Chrome/62.0.3202.84',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Mozilla/5.0 (X11; CrOS x86_64 13505.63.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.400',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
]

import hashlib
import json
import os
import random
import threading
import time
import tkinter as tk
from tkinter import *

from requests_html import HTMLSession


class KgyySpider(object):
    def __init__(self):
        """
            1、初始化部分
        """
        # row: 行;  column: 分开; pady: 高距离; padx: 宽距离;sticky: 水平;W: 上对齐;N: 下对齐; E: 左对齐; S: 右对齐
        # 1、定义可视化窗口，设置窗口和主题大小布局
        self.window = tk.Tk()
        # self.window.configure(bg='black')
        self.window.title('音乐小助手')
        # 2、禁止修改窗口大小
        self.window.resizable(False, False)
        # 3、设置窗口大小和居中
        x = int((self.window.winfo_screenwidth() / 2) - (800 / 2))
        y = int((self.window.winfo_screenheight() / 2) - (600 / 2))
        self.window.geometry('{}x{}+{}+{}'.format(720, 500, x, y))
        # 4、创建提示话语标语标签
        self.prompt_words_1 = tk.Label(self.window, text="请输入歌手名称", font=('华文行楷', 12), width=10, height=2)  # fg="white", bg="green"
        self.prompt_words_1.grid(row=0, column=1, pady=1, sticky=W + E + N + S, padx=20)
        self.prompt_words_2 = tk.Label(self.window, text='如: KeyKey, 傲七爷', font=('黑体', 12), width=10, height=2, )
        self.prompt_words_2.grid(row=1, column=1, pady=1, sticky=W + E + N + S, padx=20)  # padx=20
        # 5、创建用户输入标签
        self.user_input = tk.Entry(self.window, show=None, font=('黑体', 12), textvariable=self.prompt_words_2)
        self.user_input.grid(row=2, column=1, sticky=W + E + N + S, padx=20)
        # 6、设置点击开始运行点击按钮
        # A、开始按钮
        self.start_button = tk.Button(self.window, text='下载', font=('黑体', 12), width=10, height=1, command=self.main)
        self.start_button.grid(row=4, column=1, pady=10, sticky=W + E + N + S, padx=20)
        # B、清屏按钮
        self.clear_button = tk.Button(self.window, text='清屏', font=('黑体', 12), width=10, height=1,
                                      command=self.clear)
        self.clear_button.grid(row=19, column=1, pady=10, sticky=W + N + S, padx=10)
        # C、退出按钮
        self.quit_button = tk.Button(self.window, text='退出', font=('黑体', 12), width=10, height=1, command=self.quit)
        self.quit_button.grid(row=19, column=1, pady=10, sticky=E + N + S, padx=10)
        # 7、创建富文本框，用于打印提示性话语
        self.text_box = tk.Text(self.window, font=('黑体', 12), width=60, height=30)
        self.text_box.grid(row=0, column=2, rowspan=20, columnspan=20, sticky=W + E + N + S, padx=5, pady=5)
        # 8、创建滚轮条标签
        self.scroll = tk.Scrollbar(orient="vertical", command=self.text_box)
        self.scroll['command'] = self.text_box.yview()
        self.scroll.grid(row=0, column=29, rowspan=20, columnspan=2, sticky=S + W + E + N, padx=5, pady=5)
        # 9、富文本框提示语句
        self.text_box.insert("insert", '+-----------------+欢迎使用音乐小助手+-----------------+' + '\n')
        self.text_box.insert("insert", '                醉后不知天在水，满船清梦压星河' + '\n')
        self.text_box.insert("insert", '\n\n' + '\n')
        # 10、爬虫初始化变量
        self.session = HTMLSession()
        self.cookies_dfid = '34dZ1w4Y0yX40RzxhP3irRmF'
        self.cookies_mid = '0f0f5f52283297b26e8d1a84be3c5999'
        self.start_url = r'https://complexsearch.kugou.com/v2/search/song?'
        self.song_info_url = r'https://wwwapi.kugou.com/yy/index.php?'

    def user_input_data(self):
        """
            2、获取用户输入
        """
        keyword = self.user_input.get()
        if keyword == '':
            self.text_box.insert("insert", '--------------------请正确输入歌手名称-------------------' + '\n')
        else:
            self.keyword = keyword
            self.Reverse_JS()

    def Reverse_JS(self):
        """
            3、JS逆向部分, 获取signature
        """
        # 1、获取时间戳
        timestamps = int(time.time() * 1000)
        # 2、获取加密列表
        sign_list = ['NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt', 'bitrate=0', 'callback=callback123',
                     f'clienttime={timestamps}', 'clientver=2000', 'dfid=-', 'inputtype=0', 'iscorrection=1',
                     'isfuzzy=0', f'keyword={self.keyword}', f'mid={timestamps}', 'page=1', 'pagesize=30',
                     'platform=WebFilter', 'privilege_filter=0', 'srcappid=2919', 'tag=em', 'userid=0',
                     f'uuid={timestamps}', 'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt']
        # 3、MD5加密
        signature = hashlib.md5("".join(sign_list).encode()).hexdigest()
        signature = signature.upper()
        # print(signature)
        self.confrim_params_index(timestamps, signature)

    def confrim_params_index(self, timestamps, signature):
        """
            4、确认歌曲列表页请求参数
        """
        params = {
            "callback": "callback123",
            "keyword": "{}".format(self.keyword),
            "page": "1",
            "pagesize": "30",
            "bitrate": "0",
            "isfuzzy": "0",
            "tag": "em",
            "inputtype": "0",
            "platform": "WebFilter",
            "userid": "0",
            "clientver": "2000",
            "iscorrection": "1",
            "privilege_filter": "0",
            "srcappid": "2919",
            "clienttime": "{}".format(timestamps),
            "mid": "{}".format(timestamps),
            "uuid": "{}".format(timestamps),
            "dfid": "-",
            "signature": "{}".format(signature),
        }
        self.requests_start_url(params)

    def requests_start_url(self, params):
        """
            5、发送请求，获取响应数据
        """
        headers = {'user-agent': random.choice(USER_AGENT_LIST)}
        response_first = self.session.get(self.start_url, headers=headers, params=params).content.decode()
        response_first = json.loads(response_first[12:-2])
        # print(response_first)
        self.parse_response_first(response_first)

    def parse_response_first(self, response_first):
        """
            6、解析获取歌曲ID，
        """
        # =========================A、构造大列表===========================
        song_infos = response_first['data']['lists']
        for song_info in song_infos:
            # =========================B、获取歌曲ID========================
            song_id = song_info['AlbumID']
            # =========================B、获取歌曲HASH值====================
            song_hash = song_info['FileHash']
            # print(song_id, song_hash, sep=' | ')
            self.confrim_params_info(song_id, song_hash)

    def confrim_params_info(self, song_id, song_hash):
        """
            7、确认歌曲详情页请求参数
        """
        params = {
            "r": "play/getdata",
            # "callback": "jQuery191045156410697659455_1633537283159",
            "hash": "{}".format(song_hash),
            "dfid": "{}".format(self.cookies_dfid),
            "mid": "{}".format(self.cookies_mid),
            "appid": "1014",
            "platid": "4",
            "album_id": "{}".format(song_id),
            "_": "{}".format(int(time.time() * 1000)),
        }
        self.requests_song_info_url(params)

    def requests_song_info_url(self, params):
        """
            8、获取歌曲详情页数据
        """
        headers = {'user-agent': random.choice(USER_AGENT_LIST)}
        try:
            response_second = self.session.get(self.song_info_url, headers=headers, params=params).json()
            # print(response_second)
            self.parse_response_second(response_second)
        except Exception as e:
            pass

    def parse_response_second(self, response_second):
        """
            9、解析获取歌曲名字， 歌曲地址
        """
        # 1、song_name
        song_name = response_second['data']['song_name']
        # 2、song_url
        song_url = response_second['data']['play_url']
        # print(song_name, song_url, sep=' | ')
        self.requests_song_url(song_name, song_url)

    def requests_song_url(self, song_name, song_url):
        """
            10、请求获取歌曲二进制数据
        """
        try:
            headers = {'user-agent': random.choice(USER_AGENT_LIST)}
            song_content = self.session.get(song_url, headers=headers).content
            self.create_dir(song_name, song_content)
        except Exception as e:
            pass

    def create_dir(self, song_name, song_content):
        """
            11、创建文件夹
        """
        if not os.path.exists(r'./{}'.format(self.keyword)):
            os.mkdir(r'./{}'.format(self.keyword))
        self.save_data(song_name, song_content)

    def save_data(self, song_name, song_content):
        """
            12、保存数据
        """
        try:
            with open(r'./{}/{}.mp3'.format(self.keyword, song_name), 'wb') as f:
                f.write(song_content)
            self.text_box.insert("insert", '歌曲下载成功: {} - {}.mp3'.format(self.keyword, song_name) + "\n")
        except Exception as e:
            self.text_box.insert("insert", '歌曲下载失败: {} - {}.mp3'.format(self.keyword, song_name) + "\n")

    def clear(self):
        """
            13、清除富文本框数据
        """
        self.text_box.delete("1.0", "end")

    def quit(self):
        """
            14、退出程序
        """
        self.window.quit()

    def main(self):
        """
            逻辑控制部分, 添加守护线程，防止线程停止时卡顿
        """
        Running = threading.Thread(target=self.user_input_data)
        Running.daemon = True
        Running.start()


if __name__ == '__main__':
    kgyy = KgyySpider()
    kgyy.window.mainloop()
