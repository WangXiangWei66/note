#教育机构 ：马士兵教育
#讲    师：杨淑娟
'''
ModuleNotFoundError: No module named 'requests'
解决方案：是安装requests模块
    安装语法: pip install requests
    卸载语法:pip uninstall requests
    安装第三方库（模块的语法）  pip  install 模块名称
'''
import requests
resp=requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=44951854803&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')
print(resp.text)
