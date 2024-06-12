import json
from pyecharts.charts import Map
from pyecharts.options import *
f = open("疫情.txt", "r", encoding="utf-8")
henan_data = f.read()
f.close()

# json格式转换python
henan_data_dict = json.loads(henan_data)

henan_data_dict_list = henan_data_dict["areaTree"][0]["children"][3]["children"]

data_list = []

for city_data in henan_data_dict_list:
    city_name = city_data["name"] + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append([city_name, city_confirm])
map=Map()

map.add("各个市确诊",data_list,"河南")


map.set_global_opts(
    title_opts=TitleOpts(title="河南疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 10, "label": "1-10", "color": "#CCFFFF"},
            {"min": 10, "max": 19, "label": "10-19", "color": "#FFFF99"},
            {"min": 20, "max": 39, "label": "20-39", "color": "#FF9966"},
            {"min": 40, "max": 69, "label": "40-69", "color": "#FF6666"},
            {"min": 70, "max": 100, "label": "70-1009", "color": "#CC3333"},
            {"min": 100, "label": "100+", "color": "#990033"},
        ]
    )
)

map.render("henanyiqing.html")


