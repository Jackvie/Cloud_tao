### 统计各平台的销售额

def xx(create_time, to_time):
    import pandas as pd
    import numpy as np
    from django.db import connection
    sql_currency_rate = "select currency_orign,rate from currency_rate_new where currency_change='USD' limit 1000"
    cc = pd.read_sql(sql_currency_rate, connection)
    #the_info = cc.set_index('currency_orign').to_dict().get('rate')
    sql = 'select o.Total_paid,o.currency_type,s.channel from `order` o inner join store s on s.idstore=o.store_idstore_id where o.order_status!="Canceled" and o.create_time>=%s and o.create_time<=%s' % (str(repr(create_time)),str(repr(to_time)))
    df = pd.read_sql(sql, connection)
    df = df.dropna(axis=0)
    df = df.groupby(by=['channel','currency_type'])[["Total_paid"]].sum()
    df = df.reset_index('currency_type')
    df[df['currency_type']=='']=np.nan
    df = df.dropna(axis=0)
    df = df.reset_index('channel')
    new_df = pd.merge(df, cc, left_on='currency_type', right_on='currency_orign', how='inner')
    new_df = new_df.drop(labels=['currency_type','currency_orign'], axis=1)
    new_df['Total_paid'] = new_df['Total_paid']*new_df['rate']
    new_df = new_df.drop(labels='rate',axis=1)
    return new_df

def run():
    create_time = '2019-11-01T00:00:00'
    to_time = '2019-12-20T00:00:00'
    new_df = xx(create_time, to_time)
    print(new_df.to_dict())
    df2 = new_df.groupby(by='channel').sum()[['Total_paid']]
    print(df2['Total_paid'].sum())

### new_df.to_dict() -> data
data = {'Total_paid': {0: 13706.997125380816,
  1: 1220.2963572799999,
  2: 10802.072148733645,
  3: 7304.6589750399999,
  4: 70200.372066261596,
  5: 21413.836160399998,
  6: 1823.0291999999999,
  7: 2209089.8761044713,
  8: 334267.19734765345,
  9: 3679870.7657655585,
  10: 6011748.0703429831,
  11: 200770.17742507125,
  12: 105928.24000000187,
  13: 178540.716174,
  14: 400690.42905444186,
  15: 61245.03999999784,
  16: 4599.529999999997,
  17: 953292.28467123583,
  18: 35484.866580008762,
  19: 1203589.2790399985,
  20: 3200.0999999999981,
  21: 447263.99709779734,
  22: 1274.5699999999999,
  23: 46.990000000000002,
  24: 18.07,
  25: 6339.9153025509013,
  26: 109327.52408141698,
  27: 67383.424880355742,
  28: 42084.478779829617,
  29: 51326.480791101749,
  30: 4913563.3540897379,
  31: 6287.215558452709,
  32: 705458.36894486914,
  33: 932.30143712633992,
  34: 5615.0598488397554,
  35: 2846061.6406699694,
  36: 1437023.2391782035,
  37: 28925.122636273896,
  38: 2174.2929989743207,
  39: 54883.581314087402,
  40: 599659.89209429396,
  41: 89.975942321159991,
  42: 804750.12971115753,
  43: 270163.00732274941,
  44: 875399.99191675277,
  45: 12.218452602379999,
  46: 11929.57167302,
  47: 19749.27716121,
  48: 8377.0119867559988,
  49: 849.01710954399994,
  50: 687201.91049781244,
  51: 23338.655146330999,
  52: 14713.622496082999,
  53: 22265.495794710489,
  54: 12178.185056331,
  55: 373762.25004123128,
  56: 2778.0086951801381,
  57: 5889.8819166486592,
  58: 494150.67355326912,
  59: 73823.932026948169,
  60: 17.25795537858,
  61: 2043.3672474897578,
  62: 25440.553482955653,
  63: 165.85541338644003,
  64: 33659.718277290129,
  65: 362352.75760063663,
  66: 12.203623988496002,
  67: 868.40042432045652,
  68: 214.38162909171007,
  69: 234859.805710352,
  70: 6470.3653149098955,
  71: 158972.73982089778,
  72: 166031.43837395599,
  73: 1255175.0175831155,
  74: 288659.31066665915,
  75: 5788.2153991004998,
  76: 2803848.0446557375,
  77: 675160.26002223068,
  78: 3711930.8503061915,
  79: 212196.89151240897,
  80: 419331.80956319999,
  81: 183778.97358641576,
  82: 30151.610294400001,
  83: 18.913859567999999,
  84: 3477.5955698399998,
  85: 749.72717958600003,
  86: 5059.393158213803,
  87: 27564.593831122274,
  88: 636.80021434800005},
 'channel': {0: u'11ST',
  1: u'Auction',
  2: u'Gmarket',
  3: u'Naver',
  4: u'AkuLaku',
  5: u'Buka',
  6: u'JD',
  7: u'Lazada',
  8: u'Shopee',
  9: u'Aliexpress',
  10: u'Amazon',
  11: u'Chinavasion',
  12: u'Facebook',
  13: u'Joom',
  14: u'Mercadolibre',
  15: u'Mymall',
  16: u'Newegg',
  17: u'Walmart',
  18: u'WalmartSale',
  19: u'Wish',
  20: u'dhgate',
  21: u'eBay',
  22: u'rumall',
  23: u'shopify',
  24: u'umka',
  25: u'Allegro',
  26: u'Amazon',
  27: u'Amazon',
  28: u'eBay',
  29: u'Amazon',
  30: u'B2W',
  31: u'Shopee',
  32: u'Amazon',
  33: u'Newegg',
  34: u'eBay',
  35: u'Amazon',
  36: u'Cdiscount',
  37: u'Priceminister',
  38: u'RakutenDE',
  39: u'Zoodmall',
  40: u'eBay',
  41: u'shopify',
  42: u'Amazon',
  43: u'eBay',
  44: u'Amazon',
  45: u'Ezbuy',
  46: u'Flipkart',
  47: u'Snapdeal',
  48: u'WeMore',
  49: u'meesho',
  50: u'Amazon',
  51: u'Qoo10',
  52: u'Rakuten',
  53: u'Wowma',
  54: u'Yahoo',
  55: u'Amazon',
  56: u'Linio',
  57: u'Amazon',
  58: u'Lazada',
  59: u'Shopee',
  60: u'Awok',
  61: u'ClubFactory',
  62: u'Ezbuy',
  63: u'Jollychic',
  64: u'Lightinthebox',
  65: u'Wish',
  66: u'cloudmall',
  67: u'meesho',
  68: u'mucho',
  69: u'Daraz',
  70: u'Perfee',
  71: u'Daraz',
  72: u'Daraz',
  73: u'Lazada',
  74: u'Shopee',
  75: u'XingYa',
  76: u'Lazada',
  77: u'Shopee',
  78: u'Lazada',
  79: u'Shopee',
  80: u'Lazada',
  81: u'Shopee',
  82: u'TIKI',
  83: u'Linio',
  84: u'Linio',
  85: u'Linio',
  86: u'Linio',
  87: u'Shopee',
  88: u'ozon'}}
import pandas as pd
df = pd.DataFrame(data)
_x = df['channel']
_y = df['Total_paid'].astype(int)
# print(df)
import matplotlib.pyplot as plt
plt.figure(figsize=(20,8), dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)

for x, y in enumerate(_y):
    plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')

plt.legend()
plt.show()
