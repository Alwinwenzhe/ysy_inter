# Author:
# Data:
# Status
# Comment:读取excel

import xlrd
from xlutils.copy import copy


class OperateExcel(object):

    def __init__(self, sheet_id=None):
        self.file_name = r'dataconfig\case.xlsx'
        if sheet_id:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = 0
        self.data = self.get_sheet()

    def get_sheet(self):
        """
        获取sheet
        :return: 一个内存地址
        """
        workbook = xlrd.open_workbook(self.file_name)
        # return workbook.sheets()[self.sheet_id]  # 仅加载指定sheet id
        return workbook.sheets()

    def get_sheets(self):
        '''
        获取sheets之和
        :return:list
        '''
        workbooks = xlrd.open_workbook(self.file_name)
        sheets = workbooks.sheets()
        return sheets

    def get_lines(self):
        '''
        获取行数
        :return: str
        '''
        sheets = self.get_sheets()
        tables = self.data[self.sheet_id]
        return tables.nrows

    def get_id(self, row):
        '''
        获取id值
        :return:
        '''
        return self.data[self.sheet_id].cell_value(int(row), int())

    def get_cell(self, row, col):
        '''
        通过行、列获取单元格值
        :param row:
        :param col:
        :return:
        '''
        return self.data[self.sheet_id].cell_value(int(row), int(col))

    def write_data(self, row, col, value):
        '''
        通过copy，写入excel新数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        book1 = xlrd.open_workbook(self.file_name)
        book2 = copy(book1)
        sheet = book2.get_sheet(self.sheet_id)  # 获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
        sheet.write(row, col, value)       # 这里的value只是一个相应状态，具体接口内容在其下的text中
        book2.save(self.file_name)

if __name__ == '__main__':
    # 直接读取行数
    # data = xlrd.open_workbook(r'..\dataconfig\case.xlsx')
    # tables = data.sheets()[0]
    # print(tables.nrows,tables.cell_value(2,3))
    re = OperateExcel()
    print('行数为：', re.get_lines())
    print('单元格值为：', re.get_cell(2, 8))
    print('excel行数为：',re.get_sheets())
