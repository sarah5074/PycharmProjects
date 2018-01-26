import requests
import json
class RunMethod():
    def post_main(self,url,data,querystring=None,header=None):

        if header != None and querystring != None:
            res = requests.post(url=url,json=data,headers=header,params=querystring)
        elif header != None and querystring == None:
            res = requests.post(url=url,json=data,headers=header)
            print(res.status_code)
        elif header == None and querystring == None:
            res = requests.post(url=url,json=data)
        elif header == None and querystring != None:
            res = requests.post(url=url,json=data,params=querystring)
        return res.json()#json格式


    def get_method(self,url,querystring=None,header=None):

        if header != None and querystring != None:
            res = requests.get(url=url,headers=header,params=querystring).json()
        elif header != None and querystring == None:
            res = requests.get(url=url,headers=header)
        elif header == None and querystring == None:
            res = requests.get(url=url)
        elif header == None and querystring != None:
            res = requests.get(url=url,params=querystring)
        return res.json()

    def run_choose_method(self,method,url,querystring=None,header=None,data=None):
        if method == 'post':
            res = self.post_main(url,data,querystring,header)
        else:
            res = self.get_method(querystring,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=None,indent=2)#更改返回的格式以json格式解析返回，然后有空格







