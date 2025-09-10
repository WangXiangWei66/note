# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from  twisted.enterprise import adbapi#创建异步，就得现需要道路让这个模块
class LieyunPipeline(object):
    def __init__(self,mysql_config):
        self.dbpool=adbapi.ConnectionPool(
            mysql_config['DRIVER'],
            host=mysql_config['HOST'],
            user=mysql_config['USER'],
            password=mysql_config['PASSWORD'],
            database=mysql_config['DATABASE'],
            auth_plugin=mysql_config['auth_plugin'],
            charset='utf8'
        )

    @classmethod#这是一个类方法。要先调用classmethod
    def from_crwaler(cls,crawler):#只要重写了该方法，那么以后创建对象的时候，都会调取该方法获取pipeline对象
        mysql_config=crawler.settings['MYSQL_DB']#这样就是去找到
        return cls(mysql_config)#这个cls指的就是，创建了上面这个类
    def process_item(self, item, spider):
        result=self.dbpool.runInteraction(self.insert_item,item)
        result.addErrback(self.insert_error)
#除错了就调用下面这个函数，把错误信息给打印下来
        return item
    #这个是执行sql语句的方法
    def insert_item(self,cursor,item):#这个就是利用cursor对象的插入操作去导入的mysql里面的
        sql='insert into article (id,title,time,author_name,main_text,article_url) values(null,%s,$s,%s,%s,%s)'#sql赋值语言
        args=(item['title'],item['time'],item['author_name'],item['main_text'],item['article_url'])
        cursor.execute(sql,args)

    def insert_error(self,failure):#这是一个自己编写的函数，如果出错的话，我们把错误给打印出来
        print("========================================")
        print(failure)
        print("========================================")
