# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 汉腾同学：编程就是 获取数据 处理数据 输出数据的过程
#          专业说法为IPO  （输入，处理，输出）
import requests

url='http://www.baidu.com'
resp=requests.get(url)
resp.encoding='utf-8' # 响应结果的编码格式
#resp.encoding=resp.apparent_encoding

print(resp.text)
