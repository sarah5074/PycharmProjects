#接收key验证码登录，保存token
import requests
import csv
__author__ = 'Administrator'
#!/usr/bin/env python
#coding=utf-8
import datetime
import  requests
import json

def login(phonenumber,keyn):
    print('================进行登录===================')
    url1 = "http://172.16.8.122:8081/credit-user/login"

"
    querystring = {"deviceId":"864313033083959",
                   "osVersion":"6.0.1",
                   "appName":"gny",
                   }
    Data = {"password":keyn,"username":phonenumber}
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept': "gzip",

}
    session = requests.Session;
    response=session.post(requests,url=url1,data=json.dumps(Data),headers=headers,verify = False)
    print(response)
    loginCookies = response.cookies
    return loginCookies

def bank(deviceId,mobilePhone,bank_id,card_no):
    print('===发送获取验证码')
    #repay()
    #id = borrow_detail(200,7)

    url2 = "http://172.16.8.122:8081/lianlianBindCard/getLianLianToken

"


    Data = {"bank_id":bank_id,"card_no":card_no,'phone':mobilePhone,'id':''}
    querystring = {"deviceId":deviceId,"mobilePhone":mobilePhone}
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept': "gzip",

}
    lock =login(15001746051,123456)
    print(lock)
    response = requests.request("POST", url=url2, data=json.dumps(Data), headers=headers,params =querystring,cookies =lock).json()

    #print(response['msg'])
    print(response)

bank('864313033083959','15001746051','4','6228480038472512979')

#将token读取到csv文件中

