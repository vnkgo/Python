# 演示地图可视化的基本使用
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()
# 准备数据
data = [
    ("广东省", 14),
    ("云南", 919),
    ("河南", 9978),
    ("武汉", 92229),
    ("上海市", 99),
    ("北京", 9943),
    ("肇庆", 9)
]
# 添加数据
map.add("地图", data)

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "100-499", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "499-999", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#CC3333"},
            {"min": 10000, "label": "10000以上", "color": "#990033"},

        ]
    )
)
# 绘图
map.render("map.html")
