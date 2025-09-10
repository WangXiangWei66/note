# coding:utf-8
import sys
import os
from  selenium import webdriver
from bs4 import BeautifulSoup as bs
import xlrd
import csv
#os.chdir(r'C:\Users\YWQ\Desktop')
#sys.setrecursionlimit(9000)  # 设置最大递归深度为9000

# 自动获取电影的评论数
# para:电影名
def getRemark(movie_name):  # 函数定义，传了一个电影的名称
    #option = webdriver.ChromeOptions()
    #option.add_argument('head')#“有头”模式，即可以看到浏览器界面，若要隐藏浏览器，可设置为 "headless"
    dr = webdriver.Chrome()#创建谷歌浏览器对象(chrome_options = option)#得到操作对象
    dr.get('https://movie.douban.com/')#打开豆瓣电影
     # 找到id名称为inp-query的输入框，输入电影名称
    dr.find_element_by_id('inp-query').send_keys(movie_name)#找到输入框并填写电影名

    dr.find_element_by_class_name('inp-btn').click()#找到搜索按钮并点击
    try:
        dr.find_element_by_partial_link_text(movie_name).click()#找到包含电影名的最近链接并点击，打开电影具体信息页面
        soup = bs(dr.page_source, 'lxml')#page_source得到当前网页的源代码
        dr.quit()#关闭浏览器
        return soup.select_one('.rating_sum').text  # select结果为列表，select_one是列表中的第一个
    except:
        return 'null'

# 将信息写入csv文件
def write(name):
    count = getRemark(name)  # 调用函数
    print(name, count) # 输出电影名称和评价次数
    with open('mark.csv', 'a+', newline = '\n')as f:
        w = csv.writer(f) # 写入CSV文件
        w.writerow([name, count])

# 以主函数方式运行
if __name__ == '__main__':
    names = ['小妇人', '我不是药神']#电影名列表
    print('开始自动化测试')
    for n in names:  # 遍历列表
        write(n)     # 一个电影一个电影 去写入
    print('测试完成')