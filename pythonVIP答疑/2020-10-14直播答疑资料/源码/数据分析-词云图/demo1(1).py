#encoding=utf-8
#教育机构 ：马士兵教育
#讲    师：杨淑娟

import sys
from os import path
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot
import jieba
import jieba.analyse
from wordcloud import WordCloud

matplotlib.use('TkAgg')
d=path.dirname(__file__)

# stopwords_path = 'stopwords\stopwords1893.txt' # 停用词词表

# 添加的自定义中文语句的代码在这里
jieba.add_word('路明非')

# 读取整个文本-要分析的文本
text=open(path.join(d,'lisao.txt')).read()

def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)  #精确模式
    liststr="/ ".join(seg_list)
    f_stop = open(path.join(d,'lisao.txt'))
    try:
        f_stop_text = f_stop.read( )
        f_stop_text= f_stop_text.encode("gbk")
    finally:
        f_stop.close( )
    f_stop_seg_list=str(f_stop_text,encoding="gbk").split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

text1 = jiebaclearText(text)

file_path = os.path.abspath('.')
alice_mask=np.array(Image.open(path.join(d,"picture.png")))
font =file_path+ '/simhei.ttf'   #一定要设置中文字体否则显示乱码 先下载

wc=WordCloud(background_color="black",font_path=font,max_words=2000,mask=alice_mask,stopwords=open(path.join(d,file_path + "/lisao.txt")).read())
# 生成一个词云图像
wordcloud=wc.generate(text1)
image=wordcloud.to_image()
# 展示生成的词云图像
image.show()