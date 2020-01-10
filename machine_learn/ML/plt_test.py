def plt_01():
    import pandas as pd
    import numpy as np
    ### http://c.biancheng.net/view/2716.html
    ### https://blog.csdn.net/weixin_40683253/article/details/87641416
    df = pd.read_csv('./store_info.csv')

    gp = df.groupby(by='channel').count()[['idstore']].sort_values(by='idstore', ascending=False).iloc[:10]

    print(gp)
    _x = gp.index
    _y = gp['idstore'].values

    import matplotlib.pyplot as plt
    import matplotlib.axis as ax

    plt.figure(figsize=(20,8), dpi=80)
    plt.bar(range(len(_x)),_y)
    plt.xticks(range(len(_x)),_x)

    for x, y in enumerate(_y):
        plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')

    plt.legend()
    plt.show()


def plt_02():
    ### 统计各平台的销售额

    def xx(create_time, to_time):
        import pandas as pd
        import numpy as np
        from django.db import connection
        sql_currency_rate = "select currency_orign,rate from currency_rate_new where currency_change='USD' limit 1000"
        cc = pd.read_sql(sql_currency_rate, connection)
        # the_info = cc.set_index('currency_orign').to_dict().get('rate')
        sql = 'select o.Total_paid,o.currency_type,s.channel from `order` o inner join store s on s.idstore=o.store_idstore_id where o.order_status!="Canceled" and o.create_time>=%s and o.create_time<=%s' % (
        str(repr(create_time)), str(repr(to_time)))
        df = pd.read_sql(sql, connection)
        df = df.dropna(axis=0)
        df = df.groupby(by=['channel', 'currency_type'])[["Total_paid"]].sum()
        df = df.reset_index('currency_type')
        df[df['currency_type'] == ''] = np.nan
        df = df.dropna(axis=0)
        df = df.reset_index('channel')
        new_df = pd.merge(df, cc, left_on='currency_type', right_on='currency_orign', how='inner')
        new_df = new_df.drop(labels=['currency_type', 'currency_orign'], axis=1)
        new_df['Total_paid'] = new_df['Total_paid'] * new_df['rate']
        new_df = new_df.drop(labels='rate', axis=1)
        return new_df

    def run():
        create_time = '2019-11-01T00:00:00'
        to_time = '2019-12-20T00:00:00'
        new_df = xx(create_time, to_time)
        df2 = new_df.groupby(by='channel').sum()[['Total_paid']]
        print(df2['Total_paid'].sum())
        return df2

    ### df2.to_dict() -> data
    data = {'Total_paid': {u'11ST': 13706.997125380816,
                           u'AkuLaku': 70200.372066261596,
                           u'Aliexpress': 3679870.7657655585,
                           u'Allegro': 6339.9153025509013,
                           u'Amazon': 12538309.673794299,
                           u'Auction': 1220.2963572799999,
                           u'Awok': 17.25795537858,
                           u'B2W': 4913563.3540897379,
                           u'Buka': 21413.836160399998,
                           u'Cdiscount': 1437023.2391782035,
                           u'Chinavasion': 200770.17742507125,
                           u'ClubFactory': 2043.3672474897578,
                           u'Daraz': 559863.98390520574,
                           u'Ezbuy': 25452.771935558034,
                           u'Facebook': 105928.24000000187,
                           u'Flipkart': 11929.57167302,
                           u'Gmarket': 10802.072148733645,
                           u'JD': 1823.0291999999999,
                           u'Jollychic': 165.85541338644003,
                           u'Joom': 178540.716174,
                           u'Lazada': 10893526.271765985,
                           u'Lightinthebox': 33659.718277290129,
                           u'Linio': 12083.63846238794,
                           u'Mercadolibre': 400690.42905444186,
                           u'Mymall': 61245.03999999784,
                           u'Naver': 7304.6589750399999,
                           u'Newegg': 5531.8314371263368,
                           u'Perfee': 6470.3653149098955,
                           u'Priceminister': 28925.122636273896,
                           u'Qoo10': 23338.655146330999,
                           u'Rakuten': 14713.622496082999,
                           u'RakutenDE': 2174.2929989743207,
                           u'Shopee': 1801738.3745518913,
                           u'Snapdeal': 19749.27716121,
                           u'TIKI': 30151.610294400001,
                           u'Walmart': 953292.28467123583,
                           u'WalmartSale': 35484.866580008762,
                           u'WeMore': 8377.0119867559988,
                           u'Wish': 1565942.0366406352,
                           u'Wowma': 22265.495794710489,
                           u'XingYa': 5788.2153991004998,
                           u'Yahoo': 12178.185056331,
                           u'Zoodmall': 54883.581314087402,
                           u'cloudmall': 12.203623988496002,
                           u'dhgate': 3200.0999999999981,
                           u'eBay': 1364786.4351435101,
                           u'meesho': 1717.4175338644563,
                           u'mucho': 214.38162909171007,
                           u'ozon': 636.80021434800005,
                           u'rumall': 1274.5699999999999,
                           u'shopify': 136.96594232115999,
                           u'umka': 18.07}}
    import pandas as pd
    df = pd.DataFrame(data).sort_values(by='Total_paid')
    _x = df.index
    _y = df['Total_paid'].astype(int)
    # print(df)
    import matplotlib.pyplot as plt
    plt.figure(figsize=(20, 8), dpi=80)
    plt.bar(range(len(_x)), _y)
    plt.xticks(range(len(_x)), _x, rotation=90)
    ### rotation 字体倾斜度
    for x, y in enumerate(_y):
        plt.text(x, y + 100, '%s' % y, ha='center', va='bottom', rotation=90)

    plt.legend()
    plt.show()


def plt_03():
    import matplotlib
    import random
    import matplotlib.pyplot as plt

    data = {'Total_paid': {u'11ST': 13706.997125380816,
                           u'AkuLaku': 70200.372066261596,
                           u'Aliexpress': 3679870.7657655585,
                           u'Allegro': 6339.9153025509013,
                           u'Amazon': 12538309.673794299,
                           u'Auction': 1220.2963572799999,
                           u'Awok': 17.25795537858,
                           u'B2W': 4913563.3540897379,
                           u'Buka': 21413.836160399998,
                           u'Cdiscount': 1437023.2391782035,
                           u'Chinavasion': 200770.17742507125,
                           u'ClubFactory': 2043.3672474897578,
                           u'Daraz': 559863.98390520574,
                           u'Ezbuy': 25452.771935558034,
                           u'Facebook': 105928.24000000187,
                           u'Flipkart': 11929.57167302,
                           u'Gmarket': 10802.072148733645,
                           u'JD': 1823.0291999999999,
                           u'Jollychic': 165.85541338644003,
                           u'Joom': 178540.716174,
                           u'Lazada': 10893526.271765985,
                           u'Lightinthebox': 33659.718277290129,
                           u'Linio': 12083.63846238794,
                           u'Mercadolibre': 400690.42905444186,
                           u'Mymall': 61245.03999999784,
                           u'Naver': 7304.6589750399999,
                           u'Newegg': 5531.8314371263368,
                           u'Perfee': 6470.3653149098955,
                           u'Priceminister': 28925.122636273896,
                           u'Qoo10': 23338.655146330999,
                           u'Rakuten': 14713.622496082999,
                           u'RakutenDE': 2174.2929989743207,
                           u'Shopee': 1801738.3745518913,
                           u'Snapdeal': 19749.27716121,
                           u'TIKI': 30151.610294400001,
                           u'Walmart': 953292.28467123583,
                           u'WalmartSale': 35484.866580008762,
                           u'WeMore': 8377.0119867559988,
                           u'Wish': 1565942.0366406352,
                           u'Wowma': 22265.495794710489,
                           u'XingYa': 5788.2153991004998,
                           u'Yahoo': 12178.185056331,
                           u'Zoodmall': 54883.581314087402,
                           u'cloudmall': 12.203623988496002,
                           u'dhgate': 3200.0999999999981,
                           u'eBay': 1364786.4351435101,
                           u'meesho': 1717.4175338644563,
                           u'mucho': 214.38162909171007,
                           u'ozon': 636.80021434800005,
                           u'rumall': 1274.5699999999999,
                           u'shopify': 136.96594232115999,
                           u'umka': 18.07}}
    import pandas as pd
    df = pd.DataFrame(data).sort_values(by='Total_paid')

    # 中文乱码和坐标轴负号处理。
    matplotlib.rc('font', family='SimHei', weight='bold')
    plt.rcParams['axes.unicode_minus'] = False

    # 城市数据。
    city_name = df.index

    # 数组反转。

    # 装载随机数据。
    data = df['Total_paid'].astype(int)

    # 绘图。
    fig, ax = plt.subplots(figsize=(20, 20), dpi=80)
    b = ax.barh(range(len(city_name)), data, color='#6699CC')

    # 为横向水平的柱图右侧添加数据标签。
    for rect in b:
        w = rect.get_width()
        ax.text(w, rect.get_y() + rect.get_height() / 2, '%d' %
                int(w), ha='left', va='center')

    # 设置Y轴纵坐标上的刻度线标签。
    ax.set_yticks(range(len(city_name)))
    ax.set_yticklabels(city_name)

    # 不要X横坐标上的label标签。
    plt.xticks(())

    plt.title('wwwww', loc='center', fontsize='10',
              fontweight='bold', color='red')

    plt.show()


def plt_04():
    import matplotlib
    import random
    import matplotlib.pyplot as plt

    # 中文乱码和坐标轴负号处理。
    matplotlib.rc('font', family='SimHei', weight='bold')
    plt.rcParams['axes.unicode_minus'] = False

    # 城市数据。
    city_name = ['北京', '上海', '广州', '深圳', '成都']

    # 数组反转。
    city_name.reverse()

    # 装载随机数据。
    data = []
    for i in range(len(city_name)):
        data.append(random.randint(100, 150))
    # 绘图。
    fig, ax = plt.subplots()
    b = ax.barh(range(len(city_name)), data, color='#6699CC')

    # 为横向水平的柱图右侧添加数据标签。
    for rect in b:
        w = rect.get_width()
        ax.text(w, rect.get_y() + rect.get_height() / 2, '%d' %
                int(w), ha='left', va='center')

    # 设置Y轴纵坐标上的刻度线标签。
    ax.set_yticks(range(len(city_name)))
    ax.set_yticklabels(city_name)

    # 不要X横坐标上的label标签。
    plt.xticks(())

    plt.title('水平横向的柱状图', loc='center', fontsize='25',
              fontweight='bold', color='red')

    plt.show()


def plt_05():
    import matplotlib.pyplot as plt
    import random
    import matplotlib

    matplotlib.rc('font', family='SimHei', weight='bold')

    city_name = ['北京', '上海', '广州', '深圳', '成都']
    city_name.reverse()

    data = []
    for i in range(len(city_name)):
        data.append(random.randint(100, 200))

    colors = ['red', 'yellow', 'blue', 'green', 'gray']
    colors.reverse()

    plt.barh(range(len(data)), data, tick_label=city_name, color=colors)

    # 不要X横坐标标签。
    # plt.xticks(())

    plt.show()


if __name__ == '__main__':
    pass