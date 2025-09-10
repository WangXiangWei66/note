from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar, Grid, Line


Line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
    .add_xaxis(['day1', 'day2'])
    .add_yaxis("交易人数", ['28','36'])
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=True),
        TextStyleOpts=opts.TextStyleOpts(font_size=18),
        AreaStyleOpts=opts.AreaStyleOpts(opacity=0.5,color='rgb(255,23,140)'),
        SplitAreaOpts=opts.SplitAreaOpts(is_show=True),
    )
)

list1 = [{"value": 4},{"value": 6}]
list2 = [{"value": 7},{"value": 7}]
list3 = [{"value": 17},{"value": 23}]
list4 = [{"value": -5},{"value": -5}]



Bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
    .add_xaxis(['day1', 'day2'])
    .add_yaxis("正常交易用户数", list3, stack="stack1", category_gap="90%",itemstyle_opts=opts.ItemStyleOpts(color='gray'),)
    .add_yaxis("新增交易用户数", list2, stack="stack1", category_gap="90%",itemstyle_opts=opts.ItemStyleOpts(color='blue'),)
    .add_yaxis("激活交易用户数", list1, stack="stack1", category_gap="90%",itemstyle_opts=opts.ItemStyleOpts(color='green'),)
    .add_yaxis("流失合约用户数", list4, stack="stack1", category_gap="90%",itemstyle_opts=opts.ItemStyleOpts(color='brown'),)
    #,"blue","green","brown"]
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return Number(x.data.value).toFixed();}"
            )
        )
    )
)

Line.overlap(Bar)
grid = Grid()
grid.add(Line,opts.GridOpts(pos_left="10%", pos_right="20%"),is_control_axis_index=True)
grid.render("test1.html")