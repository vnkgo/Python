# f=open("1960-2019全球GDP数据.csv","r",encoding="GB2312")
# GDP_lines=f.readlines()
# f.close()
#
# #删除第一行数据
# GDP_lines=GDP_lines[1:]
#
# data_dict={}
# data=0
# for line in GDP_lines:
#     year=int(line.split(",")[0])
#     country=line.split(",")[1]
#     GDP= float(line.split(",")[2])
#     data_dict[year].append([country,GDP])
# print(data_dict)
#     # try:
#     #     data_dict[year].append([country,GDP])
#     #
#     # except KeyError:
#     #     data+=1
#     #     data_dict[year]=[]
#     #     data_dict[year].append([country,GDP])
#
