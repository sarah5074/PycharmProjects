class CommonUtil():
    def is_contain(self,str_one,str_two):
        #判断一个字符串是否在另外一个字符串中
        #str_one查找的字符串
        #str_two被查找的字符串
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag