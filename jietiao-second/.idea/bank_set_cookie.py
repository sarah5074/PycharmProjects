import requests
def bank_set_cookie():
    url = "http://172.16.8.122:8081/lianlianBindCard/credit-card/firstUserBank"
    querystring = {"clientType":"android",
                   "appVersion":"2.0.0",
                   "deviceId":"864313033083959",
                   "mobilePhone":"15001746051",
                   }
    #payload = {"password":keyn,"username":phonenumber}
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept': "gzip",

}
    response = requests.request("GET", url, headers=headers,params = querystring).text
    print(response)



bank_set_cookie()

