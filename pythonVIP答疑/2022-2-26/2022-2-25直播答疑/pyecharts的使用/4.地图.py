# coding:utf-8
# author:杨淑娟

from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
#$print( [list(z) for z in zip(Faker.provinces, Faker.values())])
lst=[['天津', 118], ['湖南', 148], ['上海', 146], ['云南', 144], ['山西', 73],['台湾',120]]
c = (
    Map()
    .add("销售省份", lst, "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="我的销售地图"))
    .render("map_base.html")
)