# -*- coding: utf-8 -*-
import tushare as ts
ts.set_token('df1add767608a3a3481997959084b942014f8ebb218878d631e5fc8b')

def open_days(begin, end):
    pro = ts.pro_api()
    df = pro.query('trade_cal', start_date='20180101', end_date='20181231')
    open_day = len(df[df['is_open'] > 0])
    print(open_day)
    return open_day


if __name__ == "__main__":
    # open_days(1,2)
    pro = ts.pro_api()
    data = pro.daily(ts_code='003000.SZ', start_date='20200914', end_date='20200929')

    # 查询当前所有正常上市交易的股票列表

    # data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    print(data)