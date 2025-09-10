# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

#pyecharts安装0.1.9.4 版
# pip install pyecharts==0.1.9.4

from pyecharts import Map

#数据
province_distribution = {'河南': 45.23, '北京': 37.56, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16, '湖南': 9,  '浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7, '内蒙古': 3, '重庆': 3,  '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1, '天津': 1, '其他': 1}

# 把字典转成两个列表
list1=list(province_distribution.keys()) #省份
lst2=list(province_distribution.values()) # 省份对应的数值

#开始绘图 Map是一个类，18行代码的操作，创建类的对象，
map=Map('中国地图','chinamap',width=1200,height=600)

#向地图中添加数据
map.add('',list1,lst2,visual_range=[0,50],is_visualmap=True,visual_text_color='#000')

# 绘制
map.render(path='中国地图.html')# 生成文件是HTML文件

