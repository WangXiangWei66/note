# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import jieba
from wordcloud import WordCloud
import numpy
from PIL import Image
#（1）从京东上爬取“华为笔记本的”好评数据  【如果不会操作的去看下体验课】

#（2）从文本文件中将数据读取出来
with open('华为笔记本.txt','r',encoding='utf-8') as file:
    text=file.read()
#print(text)
#（3）分词使用一个第三方库jieba
text_cut=jieba.lcut(text)  #开始分词，结果为一个列表
#去除列表中单个字的词语
lst=[]  # 存储非单个字的词语
for item in text_cut:
    if len(item)!=1:
    #print(item)
        lst.append(item)

#（4）生成词云图 使用到一个第三方库wordcloud  第三方库的安装方式pip install 模块名
text_cut=' '.join(text_cut)

#将图片转成数组类型
alice_image=numpy.array(Image.open('picture2.png'))

# 创建WordCloud的对象
word_cloud=WordCloud(font_path='simhei.ttf',background_color='black',mask=alice_image) #mask是词云图的形状

#生成词云图
wc=word_cloud.generate(text_cut)
#转成图片
image=wc.to_image()
#显示
image.show()





