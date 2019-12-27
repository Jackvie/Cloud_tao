# -*- coding: utf-8 -*-
import StringIO
import xlsxwriter
from django.http import HttpResponse


def export_summary(request):
    key = ['q','w','e']
    value = {'q':'qwe','w':'asd','e':'zxc'}
    get_file_name = 'test'
    return make_excel(key,value,get_file_name)


def make_excel(key,value,get_file_name):
    sio = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(sio)
    worksheet = workbook.add_worksheet()
    # 单元格样式
    header_format= workbook.add_format({
        'text_wrap': True,
        'valign': 'vcenter',
        'align': 'center',
        'border': 1,
        'font_size': 10
    })
    col_len = len(key)
    row_len = len(value)+1
    for c in range(col_len):

        for r in range(row_len):
            if r == 0:
                worksheet.write(r,c,key[c],header_format)
            else:
                worksheet.write(r-1,c,value[key[c]],header_format)
    workbook.close()
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='APPLICATION/OCTET-STREAM')
    file_name = 'attachment; filename=%s.xlsx' % (get_file_name)
    response['Content-Disposition'] = file_name
    return response


### js
#$scope.export = function () {
#	var url = 'export_summary?' + 'report_id=' + $scope.report_id;
#	window.open(url)
#}
