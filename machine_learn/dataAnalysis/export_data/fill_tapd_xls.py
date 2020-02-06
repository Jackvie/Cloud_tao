# https://www.cnblogs.com/Detector/p/8709362.html
# https://blog.csdn.net/brucewong0516/article/details/82707492
# https://www.cnblogs.com/jiangzhaowei/p/5856604.html
# https://www.cnblogs.com/hedeyong/p/7646125.html


def main():
    dt = pd.read_excel('meme.xlsx').to_dict()
    for key,col in head_dict.items():
        if dt.get(key):
            for row, value in dt.get(key).items():
                worksheet.write(row+1,col,value)
    workbook.save('new_test.xls')


if __name__ == '__main__':
    import pandas as pd
    import xlrd
    # df = pd.DataFrame()
    # df2 = pd.ExcelFile('aaa.xlsx')
    # b = df2.book
    book = xlrd.open_workbook('test.xls', formatting_info=True)
    # i = book.sheet_by_index(1)
    from xlutils.copy import copy
    # from xlutils import display,styles,filter
    from xlwt.Worksheet import Worksheet
    from xlwt.Workbook import Workbook
    from xlwt.Row import Row

    # df2.close()
    workbook = copy(book)  # type: Workbook
    worksheet = workbook.get_sheet(1)  # type: Worksheet
    # row = worksheet.row(0) # type: Row
    # worksheet.write(1,1,'chaxxx')
    # workbook.save('new_test.xls')
    head_dict = {key:index for index,key in enumerate(book.sheet_by_index(1).row_values(0))}
    main()
