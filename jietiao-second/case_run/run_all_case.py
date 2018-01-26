import unittest
#批量
#待执行用例的目录
def testsuite():
    case_dir = "C:\\Users\\Administrator\\PycharmProjects\\jietiao-spark\\testcase"    #测试bank下的test_bank_sms文件
    testcase = unittest.TestSuite()

    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*overdue_serach.py",top_level_dir=None)
    #直接将discover添加到testcase中
    testcase.addTest(discover)
    return testcase

if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    #testsuite()函数用于查找指定条件下所有的测试用例
    runner.run(testsuite())



'''
def testsuite():
    case_dir = "C:\\Users\\Administrator\\PycharmProjects\\gny"
    testcase = unittest.TestSuite()

    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*register.py",top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            #添加用例到testcase
            testcase.addTests(test_case)
    testcase.addTest(testcase)
    return testcase

if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    #testsuite()函数用于查找指定条件下所有的测试用例
    runner.run(testsuite())'''
