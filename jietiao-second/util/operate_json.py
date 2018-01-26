import json

data = 'C:/Users/Administrator/PycharmProjects/jietiao-spark/test_file/useVo.json'

class OperationJson():
    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        with open('C:/Users/Administrator/PycharmProjects/jietiao-spark/test_file/useVo.json',encoding='UTF-8') as fp:
            data = json.load(fp)
            return data

    def get_data(self,id):
        return self.data[id]

if __name__ =='__main__':
    opjson = OperationJson()
    print(opjson.get_data('useVo'))
