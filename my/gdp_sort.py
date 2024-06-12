from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts

f=open("1960-2019全球GDP数据.csv","r",encoding="GB2312")
GDP_lines=f.readlines()
f.close()

#删除第一行数据
GDP_lines=GDP_lines[1:]

data_dict={}

timeline=Timeline()

for line in GDP_lines:
    year=int(line.split(",")[0])
    country=line.split(",")[1]
    GDP= float(line.split(",")[2])
    try:
        data_dict[year].append([country,GDP])

    except KeyError:

        data_dict[year]=[]
        data_dict[year].append([country,GDP])

sorted_year_list=sorted(data_dict.keys())


for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1],reverse=True)
    year_data=data_dict[year][0:8]
    x_data=[]
    y_data=[]
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/1000000)
    bar=Bar()
    y_data.reverse()
    x_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    timeline.add(bar,str(year))


timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False

)
timeline.render("product/世界gdp.html")
