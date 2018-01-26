from run_method.run_method import RunMethod
from data import get_data

class RunTest():
    def __init__(self):
        self.run_method = RunMethod()
        self.data = get_data.GetData()

    def go_on_run(self):
        rows_count = self.data.get_case_lines()
        #res = None
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            header = self.data.get_is_header(i)
            querystring = self.data.get_parms_for_json(i)
            if is_run:
                res = self.run_method.run_choose_method(method,url,querystring,header,data)
            return res


if __name__ == '__main__':
    run = RunTest()
    print(run.go_on_run())


