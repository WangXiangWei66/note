# coding:utf-8
# author:杨淑娟
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
#print( [list(z) for z in zip(Faker.choose(), Faker.values())])
lst=[['猫', 135], ['狗', 136], ['兔', 97], ['猪', 130]]
c = (
    Pie()
    .add(
        "",
        #[list(z) for z in zip(Faker.choose(), Faker.values())],
        lst,
        radius=["40%", "75%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-Radius"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_radius.html")
)