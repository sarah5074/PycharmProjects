from util.operate_loanapply_excel import OperateExcel
from  data import data_config
from util.operate_json import  OperationJson
class GetData():
    def __init__(self):
        self.opera_excel = OperateExcel()

    #获取行数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    #获取是否运行
    def get_is_run(self,y):
        col = int(data_config.is_run()) #行是通过获取data配置表获取的
        run_model= self.opera_excel.get_cell_value(y,col)
        flag = None
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag
    #获取有没有头部信息
    def get_is_header(self,y):
        row = int(data_config.header_is())
        header = self.opera_excel.get_cell_value(y,row)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    #获取测试方法
    def get_request_method(self,y):
        row = int(data_config.request_method())
        request_mesd = self.opera_excel.get_cell_value(y,row)
        return request_mesd

    #获取测试的url
    def get_request_url(self,y):
        row = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(y,row)
        return url

    #获取请求的body数据,数据可以直接获取。不是字典的方式
    def get_request_data(self,y):
        row = int(data_config.data_body())
        body_data = self.opera_excel.get_cell_value(y,row)
        if body_data == '':
            return None
        return body_data

    #获取excel表中的parms的值
    def parms(self,y):
        row = int(data_config.header_params())
        header_data = self.opera_excel.get_cell_value(y,row)
        if header_data == 'no':
            return None
        return header_data

    #获取headers中的键值对，为json文件
    def get_parms_for_json(self,y):
        oprea_json = OperationJson()
        if self.parms(y) != None:
            request_json_data = oprea_json.get_data(self.parms(y))
            return request_json_data

    #如果y是关键字，获取y值，读取json文件中为y的value

    def get_data_for_json(self,y):
        oprea_json = OperationJson()
        request_json_data = oprea_json.get_data(self.get_request_data(y))
        return request_json_data


    def get_expect_data(self,y):
        row = int(data_config.expect_data())
        data_expect = self.opera_excel.get_cell_value(y,row)
        return data_expect