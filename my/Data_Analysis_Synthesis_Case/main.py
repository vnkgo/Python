from pyecharts.options import TitleOpts, LabelOpts, InitOpts

from file_definite import FileReader,TextFileReader,JsonFileReader
from data_analysis import Record
from pyecharts.charts import Bar
from pyecharts.charts import *
from pyecharts.globals import ThemeType

text_file_reader=TextFileReader("2011年1月销售数据.txt")
json_file_reader=JsonFileReader("2011年2月销售数据JSON.txt")

jan_data=text_file_reader.read_data()
feb_data=json_file_reader.read_json()

all_data=jan_data+feb_data

data_dict={}
for record in all_data:
    if record.Date in data_dict.keys():
        data_dict[record.Date] += record.Sales

    else:
        data_dict[record.Date] = record.Sales

bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))

bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额"),

)

bar.render("每日销售额.html")