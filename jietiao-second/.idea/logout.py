import requests
def logout(deviceId,mobilePhone):
    #repay()
    print("=================退出登录================")

    url = "http://172.16.8.122:8081/credit-user/logout"
    querystring = {"deviceId":deviceId,"mobilePhone":mobilePhone}
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept': "gzip",
    'Cookie':'JSESSIONID=79EFEE9ED91D210DC3911E16709A502A'
}
    response = requests.request("GET", url, headers=headers,params =querystring).json()
    print(response)

logout(6228480038472512979,15001746051)
