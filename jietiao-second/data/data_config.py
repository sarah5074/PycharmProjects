class global_var():
    ID = '0'
    model_name = '1'
    condition_before = '2'
    url = '3'
    header_is = '4'
    data_connect = '5'

    header_params = '6'#头部参数

    data = '7' #body参数
    request_method = '8'
    is_run = '9'
    expect_data = '10'
    actual_data = '11'

#case id
def get_id():
        return global_var.ID

#获取模块名称
def model_name():
       return global_var.model_name

#前置条件
def condition_before():
        return global_var.condition_before

#url
def get_url():
    return global_var.url
#有无头部信息
def header_is():
    return global_var.header_is

#数据依赖
def data_connect():
    return global_var.data_connect

#请求头部的参数值
def header_params():
    return global_var.header_params

#body里的数值
def data_body():
    return global_var.data

#是否运行
def is_run():
    return global_var.is_run

def request_method():
    return global_var.request_method
#期望数值
def expect_data():
    return global_var.expect_data


#实际结果
def actual_data():
    return global_var.actual_data

def get_header_value():
    headers = {
    "content-type": "application/json",
    "accept": "*/*"
     }
    return headers