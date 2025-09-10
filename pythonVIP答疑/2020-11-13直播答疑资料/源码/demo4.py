# 教育机构 ：马士兵教育
# 讲    师：杨淑娟  动态更换请求头
from  fake_useragent import  UserAgent  # 封装了各种浏览器的描述信息
ua=UserAgent()

#print(ua.ie) #输出关于IE浏览器描述数据
print(ua.chrome)


