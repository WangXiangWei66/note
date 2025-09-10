# coding:utf-8
# author:杨淑娟
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

lst=[['China', 147], ['Canada', 111], ['Brazil', 136], ['Russia', 148], ['United States', 20], ['Africa', 134], ['Germany', 149]]
c = (
    Map()
    .add("商家A", lst, "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
    .render("map_world.html")
)