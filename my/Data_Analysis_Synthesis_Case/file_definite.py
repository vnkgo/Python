from data_analysis import Record
import json

class FileReader:
    def read_data(self) -> list[Record]:
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    # 复写父类方法
    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='utf-8')

        record_list = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_json(self)->list[Record]:
        f=open(self.path, 'r',encoding='utf-8')

        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"],int(data_dict["money"]), data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list

if __name__ == '__main__':
    jsontext=JsonFileReader('2011年2月销售数据JSON.txt')
    texfile=TextFileReader('2011年1月销售数据.txt')
    list1=jsontext.read_json()
    list2=texfile.read_data()

    for i in list1:
        print(i)
    for j in list2:
        print(j)