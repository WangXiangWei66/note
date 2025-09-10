# coding:utf-8
# author:杨淑娟
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker


lst=[['广东', 126], ['北京', 132], ['上海', 52], ['江西', 94], ['湖南', 115], ['浙江', 147], ['江苏', 82],['吉林',100]]
c = (
    Map()
   .add("商家A", lst, "china")
   # .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    .render("map_base.html")
)