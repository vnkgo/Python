from pyecharts.charts import Line

line=Line()

line.add_xaxis(["美国","中国","英国"])

line.add_yaxis("gdp",[30,20,10])

line.render("k.html")