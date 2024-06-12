from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar1=Bar()

bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("gdp",[30,39,12],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar1.render("Product/bar-chart.html")
