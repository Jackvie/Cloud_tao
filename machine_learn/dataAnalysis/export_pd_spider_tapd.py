import requests
### https://blog.csdn.net/CSU_GUO_LIANG/article/details/102772294
def fn(page=1):
    url = 'https://www.tapd.cn/50594052/prong/stories/stories_list'

    params = {
    'data[Filter][owner]': '魏云涛;',
    'data[Filter][status][0]': 'resolved',
    'data[Filter][status][1]': 'status_2',
    'data[Filter][status][2]': 'status_3',
    'data[Filter][modified][begin]': '2020-02-01',
    'data[Filter][modified][end]': '2020-01-01',
    'qksearch': 'true',
    #'conf_id': '1150594052001010508',
    'perpage': 20,
    'page': page,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Cookie': '69918265_50594052_/prong/stories/stories_list_remember_view=1150594052001010508; 50594052_category_tree_for_view=10; is_filter_close=false; tui_filter_fields=%5B%22name%22%2C%22owner%22%2C%22status%22%2C%22modified%22%5D; story_index_order1150594052001010508sort=owner%7Edesc; selected_category_id=-1; current_user_nick=%E9%AD%8F%E4%BA%91%E6%B6%9B; current_user_id=69918265; bugtrace_reports_myview_50594052_filter_fields=%5B%22version_report%22%2C%22module%22%5D; locale=zh_cn; pgv_pvi=9364111360; __root_domain_v=.tapd.cn; _qddaz=QD.oh4gvq.qg2vnx.k2y0w6rq; new_worktable=todo%7C%7C%7Cexpiration_date; iteration_view_type_cookie=card_view; current_view_tab=list; editor_type=markdown; tapdsession=15807147120121356358a54500dcf6a8bf77228a9b28d9d91789971c26db5175dd69db16b1; t_u=de553fd231b7b98edd40e5a63e4d9d547829c7b21d460065f061878312c51a31f060925246ee316728eb60e0f695a12a578e7ad744453acf28039e74828144beef1510f356cfdb05%7C1; t_cloud_login=yuntao%40starmerx.com; _t_uid=69918265; _t_crop=53554184; tapd_div=101_2463; iteration_card_current_iteration_50594052=1150594052001000380; _wt=eyJ1aWQiOiI2OTkxODI2NSIsImNvbXBhbnlfaWQiOiI1MzU1NDE4NCIsImV4cCI6MTU4MDk1ODU2OH0%3D.bbe70a48ba4123b0868fa664ed1c9fba38c2056ca15c86292a26549fabb4374d; dsc-token=Ypu84hQt9rLCV5fA'
    }
    #response = requests.get(url, params=params, headers=headers)
    response = requests.get(url+'?data[Filter][owner]=%E9%AD%8F%E4%BA%91%E6%B6%9B%3B&data[Filter][status][]=resolved&data[Filter][status][]=status_2&data[Filter][status][]=status_3&data[Filter][modified][begin]=2020-01-01&data[Filter][modified][end]=2020-02-01&qksearch=true&qksearch=true', headers=headers)

    from bs4 import BeautifulSoup
    import re
    soup = BeautifulSoup(response.content, 'lxml')
    data = soup.find_all(name='a', attrs={'class':'namecol editable-value', 'id': re.compile(r'story_')})
    # data = [data.text for i in data]
    return {i.attrs['title'] for i in data}

def outputfile(writer, df):
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Add a header format.
    header_format = workbook.add_format({
        'bold': True,  # 字体加粗
        'text_wrap': True,  # 是否自动换行
        'valign': 'top',  # 垂直对齐方式
        'align': 'left',  # 水平对齐方式
        'fg_color': '#D7E4BC',  # 单元格背景颜色
        'border': 2})  # 单元格边框宽度

    yellow = workbook.add_format({'fg_color': '#FFEE99'})
    red = workbook.add_format({'fg_color': '#2dB054'})

    # Write the column headers with the defined format.
    # for col_num, value in enumerate(df.columns.values):
    #     if col_num % 2 == 0:
    #         worksheet.write(0, col_num, value, header_format)
    #     else:
    #         worksheet.write(0, col_num, value, yellow)
    #
    # # Write the row with the defined format.
    # for index, value in df.iterrows():
    #     print(index, " -- > ", value.values)
    #     if index % 2 == 0:
    #         worksheet.write(index + 1, 0, value[0], header_format)
    #     else:
    #         worksheet.write(index + 1, 0, value[0], yellow)

    worksheet.set_column("A:C", 16)
    format2 = workbook.add_format({'bold': True, 'align': 'vcenter', 'valign': 'top', 'text_wrap': True, 'fg_color':'#FCFCFC'})
    worksheet.set_row(0, cell_format=format2)

    return writer

def run():
    s = set()
    for page in [1,2]:
        s = s | fn(page)
    df = pd.Series(list(s)).to_frame('星任务') # type: pd.DataFrame
    df['类型'] = '任务'
    df['提报人'] = '刘亚波'
    df['解决人'] = '魏云涛'
    df['描述'] = df['星任务']
    ### 交换列
    # df.loc[:, ['a', 'b']] = np.array(df[['b', 'a']]).tolist()
    df = df.loc[:, ['类型','星任务', '描述','提报人','解决人']]

    return df

if __name__ == '__main__':
    import pandas as pd
    df = run()  # type: pd.DataFrame
    writer = pd.ExcelWriter('xxx.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer = outputfile(writer, df)
    writer.save()

