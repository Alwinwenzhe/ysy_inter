#Author:
#Data:
#Status
#Comment:读取excel

import xlrd
from xlutils.copy import copy

class OperateExcel(object):

    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = r'..\dataconfig\case.xlsx'
            self.sheet_id = 0
        self.data = self.get_sheet()


    def get_sheet(self):
        '''
        获取sheet
        :return: 一个内存地址
        '''
        workbook = xlrd.open_workbook(self.file_name)
        tables = workbook.sheets()[self.sheet_id]       #仅加载指定sheet id
        return tables

    def get_lines(self):
        '''
        获取行数
        :return: str
        '''
        tables = self.data
        return tables.nrows

    def get_cell(self,row,col):
        '''
        通过行、列获取单元格值
        :param row:
        :param col:
        :return:
        '''
        return self.data.cell_value(int(row),int(col))

    def write_data(self,row,col,value):
        '''
        通过copy，写入excel新数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        # read_data = xlrd.open_workbook(self.file_name)
        # write_data = copy(read_data)
        # sheet_data = write_data.get_sheet(0)
        # sheet_data.write_data(row,col,value)
        # write_data.save(self.file_name)
        book1 = xlrd.open_workbook(self.file_name)
        book2 = copy(book1)
        # print(dir(book2))
        sheet = book2.get_sheet(0)  # 获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
        sheet.write(row,col,value)
        book2.save(self.file_name)

if __name__ == '__main__':
    #直接读取行数
    # data = xlrd.open_workbook(r'..\dataconfig\case.xlsx')
    # tables = data.sheets()[0]
    # print(tables.nrows,tables.cell_value(2,3))
    re = OperateExcel()
    print('行数为：',re.get_lines())
    print('单元格值为：',re.get_cell(2,8))
