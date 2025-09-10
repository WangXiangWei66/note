# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

class LianJiaSpider:

    def send_request(self,url): # 形参
        print(url)
    def start(self):
        full_url = 'http://www.baidu.com'
        self.send_request(full_url)  # 实参

if __name__ == '__main__': # 以主函数形式运行， 【模块那个章节学习】
    lianjia=LianJiaSpider() # 创建对象， 在内存中开空间，
    lianjia.start() #　这句代码执行完后，对象不会被马上销毁

    # 或者
    LianJiaSpider().start()# 这句代码运行完之后，这个对象的销毁会早一些

    # 这两种代码占用的内存空间不同

a = 10