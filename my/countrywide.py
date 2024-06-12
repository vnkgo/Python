import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("疫情.txt", "r", encoding="utf-8")
data = f.read()
# 关闭文件
f.close()

# 取得各省数据
data_dict = json.loads(data)

# 从字典中取出省份的数据
province_data_list = data_dict["areaTree"][0]["children"]

# 绘图需要用到的数据
data_list = []
# 组装每个省份和确诊人数为元组，并各个省的数据都封装到列表内
for province_data in province_data_list:
    province_name = province_data["name"]
    if province_name=="上海北京天津重庆":
        province_name+="市"
    else:
        province_name = province_data["name"]+"省"  # 省份名称

    province_confirm = province_data["total"]["confirm"]  # 省份确诊
    data_list.append((province_name, province_confirm))

# 调用地图
map = Map()

map.add("各个省份确诊人数", data_list, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#CC3333"},
            {"min": 100000, "label": "1-99", "color": "#990033"},
        ]
    )
)

map.render("全国疫情地图.html")
