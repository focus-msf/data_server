# -*- coding: utf-8 -*-
"""
此模块用于封装数据的取用，用于同一接口
"""
from mootdx.quotes import Quotes
from mootdx.consts import MARKET_SH,MARKET_SZ
import pandas as pd
import pendulum
import tushare as ts

from util import time_format_1,symbol_format
from CONSTANT import ts_code_table

ts.set_token('df1add767608a3a3481997959084b942014f8ebb218878d631e5fc8b')



class DataCollector:

    def __init__(self, begin):
        begin = time_format_1(begin)
        now = time_format_1(pendulum.today())
        pro = ts.pro_api()
        self.trade_date = pro.query('trade_cal', start_date=begin, end_date=now)
        pass

    def open_days(self,begin, end):

        begin = time_format_1(begin)
        end = time_format_1(end)

        # get begin  and stop index
        begin = self.trade_date[self.trade_date['cal_date'] == begin].index.tolist()[0]
        end = self.trade_date[self.trade_date['cal_date'] == end].index.tolist()[0]

        df = self.trade_date[begin:end]
        open_day = len(df[df['is_open'] > 0])
        return open_day


    def good_day(self,begin, end):
        """
        传入开始日期和结束日期
        返回start 和 offset
        :param begin: 
        :param end: 
        :return: 
        """
        # init
        now = pendulum.today()
        begin= pendulum.parse(begin)
        end = pendulum.parse(end)

        # 计算start  从零开始所以减一
        start = self.open_days(end,now) - 1


        # 计算offset
        offset = self.open_days(begin,end) +1

        return start,offset


    def get_index_k_data(self,symbol, begin, end):
        """
        
        :param symbol: 
        :param begin: 
        :param end: 
        :return: 
        
        
        start = 0 为最新一天数据， offset 为若干条
        
        
        """
        # 确定市场
        if symbol.startswith('399'):
            market = MARKET_SZ
        else:
            market = MARKET_SH

        start, offset = self.good_day(begin,end)
        client = Quotes.factory(market='std')

        pulls, remainder = divmod(offset,800)

        my_data = []
        for each in range(pulls):
            data = client.index(frequency=9, market=market, symbol=symbol, start=start, offset=800)
            my_data.append(data)
            start += 800

        data = client.index(frequency=9, market=market, symbol=symbol, start=start, offset=remainder)
        my_data.append(data)
        my_data.reverse()
        my_data= pd.concat(my_data)

        return my_data


    def get_stock_k_data(self,symbol="000001,000002", begin="20150703", end="20170710"):

        # change
        symbol = ts_code_table[symbol]

        pro = ts.pro_api()
        df = pro.daily(ts_code=symbol, start_date=begin, end_date=end)
        return df

    def format_data(self,data):
        """
        open 0 close 1 high 2 low 3 datetime 11
        :param data: 
        :return: 
        """
        my_data = []
        for row in data.iterrows(): # iterrows 返回的tuple (0,row) 所以去row[1]
            my_data.append([row[1][11],row[1][0],row[1][1],row[1][3],row[1][2]])
        return my_data

def get_stock_k_data(symbol, begin, end):

    # change
    symbol = ts_code_table.get(symbol)
    if symbol is None:
        return None

    pro = ts.pro_api()
    df = pro.daily(ts_code=symbol, start_date=begin, end_date=end)
    return df




if __name__ == "__main__":
    # begin = pendulum.parse('2017-09-25')
    # datac = DataCollector(begin)
    # datac.open_days()

    # data = get_index_k_data()
    # symbol_str = "000166,000686,000712,000728,000750,000776,000783,002500,002670,002673,002736,002797,002926,002939,002945,300059,601990,601901,601881,601878,601788,601696,601688,601555,601456,601377,601375,601236,601211,601198,601162,601108,601099,601066,600999,600958,600918,600909,600864,600837,600621,600369,600155,600109,600095,600061,600030"
    # ["2020-06-02", "2020-09-04"]
    # ["2017-09-01", "2020-09-30"]
    symbol_str = "603706"
    # start = '20200901'
    start = '20200602'
    # stop = '20200930'
    stop = '20200904'
    data = get_stock_k_data(symbol_str,start,stop)
    data_per_stock = (data[data['ts_code'] == '002469.SZ']).loc[:,
                     ['trade_date', 'open', 'close', 'low', 'high']]
    data = []
    for index, row in data_per_stock.iterrows():
        data.append(list(row))

    # print(data_per_stock)
    # data  = format_data(data)
    # print(data)