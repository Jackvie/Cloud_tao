import pandas as pd
import numpy as np

def fn1():
    base = '2020 12 12'
    print(type(pd.Timestamp(base)))
    print(type(pd.to_datetime(base)))
    print(pd.to_datetime([base, base]))
    print(pd.DatetimeIndex([base, base]))
    # ignore return ndarray
    print(pd.to_datetime([base, 'xxxx'], errors='ignore'))
    # coerce return DatetimeIndex
    print(pd.to_datetime([base, 'xxxx'], errors='coerce'))


def fn2():
    # 时间序列与频率
    ts = pd.date_range(end='1/1/2020 15:30', periods=10, name='xxxx', normalize=True)
    print(ts)
    ts = pd.date_range(start='1/1/2020 14:00', end='1/10/2020 15:30',  name='xxxx', freq='D')
    print(ts)
    ts = pd.bdate_range(start='1/1/2020 14:00', end='1/10/2020 15:30',  name='xxxx')
    print(ts)
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
    # D/日历日 B/工作日
    # T/分 S/秒 L/毫秒 U/微秒
    # W-MON   WOM-2MON
    # ts = pd.date_range(start='1/1/2020 14:00', end='3/20/2020 15:30',  freq='WOM-2MON')
    # print(ts)
    # M MouthEnd  MS MouthStart
    # ts = pd.date_range(start='1/1/2020 14:00', end='3/20/2020 15:30',  freq='M')
    # print(ts)
    # Q QuarterEnd (12) QS QuarterStart (1)
    ts = pd.date_range(start='1/1/2020 14:00', end='3/20/2021 15:30',  freq='Q')
    # print(ts)
    # ts = pd.date_range(start='2017', end='2020', freq='Q-OCT')
    # print(ts)
    # ts = pd.date_range(start='2017', end='2020', freq='QS-JAN')
    # print(ts)
    # A,Y 年末 A-DEC  AS,YS 年初 YS-JAN
    ts = pd.date_range(start='2017', end='2020', freq='A')
    print(ts)
    # 总结 B/D 控制工作日 日历日
    # 总结 M月 A,Y年 Q季度  带S为初 即一月一日 不带S为末 即12月31
    # 总结 显示的 可以 通过-JAN/-DEC 来指定月份 通过有无S来指定1日或31日
    # 复合频率
    ts = pd.date_range(start='1/1/2020 14:00', end='3/20/2021 15:30',  freq='2H30T')
    print(ts)
    ts = pd.date_range(start='1/1/2020 14:00', end='6/20/2020 15:30',  freq='2MS')
    print(ts)


def fn3():
    # 频率转换
    ts = pd.Series(np.random.rand(4), index=pd.date_range('20170101', '20170104'))
    print(ts)
    ## ffill forward 用之前填充 bfill 用之后填充 back
    ts = ts.asfreq(freq='12H', method='ffill')
    print(ts)
    # 频率位移
    ts = pd.Series(np.random.rand(4), index=pd.date_range('20170101', '20170104'))
    ## 对数值 正数 后移 负数 前移
    print(ts.shift(periods=2))
    # 对时间戳位移
    print(ts.shift(periods=1, freq='2D'))
    print(ts.shift(periods=2, freq='D'))


if __name__ == '__main__':
    fn3()
