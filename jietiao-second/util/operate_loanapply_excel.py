import xlrd


class OperateExcel():
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = 'C:/Users/Administrator/PycharmProjects/jietiao-spark/test_file/loan_apply.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()
    #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]

        return tables

    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取单元格的内容 y表示行，先表示列
    def get_cell_value(self,y,x):
        tables = self.data
        return tables.cell_value(y,x)


if __name__ =='__main__':
    opers = OperateExcel('C:/Users/Administrator/PycharmProjects/jietiao-spark/test_file/loan_apply.xlsx',0)
    opers.get_cell_value(1,1)