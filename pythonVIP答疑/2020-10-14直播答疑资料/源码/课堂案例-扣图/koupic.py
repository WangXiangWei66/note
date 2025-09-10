#教育机构 ：马士兵教育
#讲    师：杨淑娟
'''pip install removebg -i http://pypi.douban.com/simple --trusted-host pypi.douban.com'''
from removebg import  RemoveBg  #第三方库(需要安装才能使用 pip install removebg)，可以提供扣图的功能
import os   #Python自带的模块
#获取要操作的图片的（名称）根据位置

img_lst=os.listdir('picture')  #获取到了picture目录下所有图片的名称，结果是一个列表
rmbg=RemoveBg('Mx2UkLVwuucWxDdsszTFLQm6','error.log') #第一个参数叫API key  ,第二个参数是一个日志文件
for pic  in img_lst:  #每次从img_lst中获取一张图片的名称，赋值给变量pic
    print('pic是什么,',pic)
    rmbg.remove_background_from_img_file('picture/'+pic)   #小括号中提供图片的路径






