import sys,os
import configparser
def test_url(config_file_path):
    cf =configparser.ConfigParser()
    cf.read(config_file_path)
    url = cf.get('Baseconf','test_url')
    deviceid = cf.get('Baseconf','deviceId')
    mobilePhone = cf.get('Baseconf','mobilePhone')
    return url,deviceid,mobilePhone
    #print(cf.items('Baseconf'))
    #print(url)


if __name__ == "__main__":
    test_url('C:/Users/Administrator/PycharmProjects/xjp/test_file/config.ini')