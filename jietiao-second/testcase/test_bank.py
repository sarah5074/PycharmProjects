#测试绑定银行卡

import unittest
import  requests
from time import sleep
from bank.insertBanK import insertBanKCard
class interger(unittest.TestCase):
    def setUp(self):
        print("开始")



    def test001(self):

        print("============1.持卡人与银行卡号不一致===============")
        response = insertBanKCard("6228480038472512979",5,"15001746051","鲍","34250119921116262X","中国农业银行")

        self.assertEqual('成功',response)


    def test002(self):
        sleep(61)
        print("============2.银行卡号与预留手机号不一致===============")
        response = insertBanKCard("6228480038472512979",5,"17612115062","鲍娟","34250119921116262X","中国农业银行")
        self.assertEqual('成功',response)

    def test003(self):
        sleep(61)
        print("============3.持卡人与预留手机不一致===============")
        response = insertBanKCard("6228480038472512979",5,"15001746051","鲍甜","34250119921116262X","中国农业银行")
        self.assertEqual('成功',response)

    def test004(self):
        sleep(61)
        print("============4.信息不填写进行绑定===============")
        response = insertBanKCard()
        self.assertEqual('成功',response)

    '''def test009(self):
        #sleep(61)
        print("============9.信用卡===============")
        response = insertBanKCard("6228480038472512979",5,"15001746051","鲍娟","34250119921116262X","中国农业银行")
        #print(response)
        self.assertEqual('成功',response)'''

    def test007(self):
        #sleep(61)
        print("============9.成功===============")
        response = insertBanKCard("6228480038472512979",5,"15001746051","鲍娟","34250119921116262X","中国农业银行")
        #print(response)
        self.assertEqual('成功',response)

    def tearDown(self):
        print("结束")


if __name__ =='__main__':
    unittest.main()