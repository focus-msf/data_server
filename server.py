# -*- coding: utf-8 -*-
from waitress import serve
import falcon
import json
import pendulum
import pandas as pd
from api import DataCollector, get_stock_k_data
from CONSTANT import inustry_symbol_table_reverse,stock_table,stock_table_reverse
from util import time_format_1,symbol_format

# begin = "2018-05-09"
# end = "2020-09-30"

#      web framework
class IndexResource(object):
    """
    返回 上证 深证 创业板 以及 下属56个行业指数的日线数据，指定时间
    
     [
            ['2004-01-05', 10411.85, 10544.07, 10411.85, 10575.92, 221290000],
            ['2004-01-06', 10543.85, 10538.66, 10454.37, 10584.07, 191460000],
            ['2004-01-07', 10535.46, 10529.03, 10432, 10587.55, 225490000],
            ]
    example data
    
    """
    def on_get(self, req, resp):
        """Handles GET requests"""

        begin, end = self.get_time(req.params['q[]'])
        data = self.get_data(begin,end)
        data = json.dumps(data,ensure_ascii=False)

        # 允许跨域访问
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = data

    def get_data(self, begin, end):
        """
        获取数据
        1. 上证指数
        2. 深证指数
        3. 56个行业指数
        
        返回数据格式：
        data = {
        'shzs': [[date,open,close,loweset,highest],[...],[...]],
        'szzs'
        }
        :return: 
        """
        data = {}
        data_c = DataCollector(begin)
        for name, symbol in inustry_symbol_table_reverse.items():
            data[name] = IndexResource.format_data(data_c.get_index_k_data(symbol=symbol,begin=begin,end=end))

        return data

    @staticmethod
    def format_data(data):
        """
        open 0 close 1 high 2 low 3 datetime 11
        :param data: 
        :return: 
        """
        my_data = []
        for row in data.iterrows():  # iterrows 返回的tuple (0,row) 所以去row[1]
            my_data.append([row[1][11][:-6], row[1][0], row[1][1], row[1][3], row[1][2]])
        return my_data

    def get_time(self, time_array):
        begin = pendulum.parse(time_array[0], strict=False)
        end = pendulum.parse(time_array[1], strict=False)

        begin = begin.format('YYYY-MM-DD')
        end = end.format('YYYY-MM-DD')
        return begin, end


class BlockResource:
    """
    返回一个板块的数据，包括板块指数，以及该板块内部的股票
    """


    def on_get(self, req, resp):
        """Handles GET requests"""

        begin, end = self.get_time(req.params['q[]'])
        block = req.params['block']
        print("获取 参数 *{}*".format(block))

        data = self.get_data(begin, end, block)
        print('查询完毕，返回数据')
        data = json.dumps(data, ensure_ascii=False)

        # 允许跨域访问
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = data

    def get_time(self, time_array):
        begin = pendulum.parse(time_array[0], strict=False)
        end = pendulum.parse(time_array[1], strict=False)

        begin = begin.format('YYYY-MM-DD')
        end = end.format('YYYY-MM-DD')
        return begin, end

    def get_data(self, begin, end, block):
        """
        获取数据， 板块指数，该板块内股票
        
        返回数据格式：
        data = {
        'shzs': [[date,open,close,loweset,highest],[...],[...]],
        'szzs'
        }
        :param begin: 
        :param end: 
        :param block: 
        :return: 
        """
        # init and transfer

        print("查询数据中")
        # 获取板块指数数据
        data = {}
        data_c = DataCollector(begin)
        block_symbol = inustry_symbol_table_reverse[block]
        print('查询指数数据')
        data[block] = IndexResource.format_data(data_c.get_index_k_data(symbol=block_symbol,begin=begin,end=end))

        # 获取板块内股票数据
        # 构造时间
        start = pendulum.parse(begin).format('YYYYMMDD')
        stop = pendulum.parse(end).format('YYYYMMDD')

        symbol_list = []
        for name, symbol in stock_table[block].items():
            symbol_list.append(symbol)

        print('查询股票数据')
        stock_data = self.get_stock_data_with_symbol_list(symbol_list, start, stop)


        # 整合 并 组成一个数组
        for name, symbol in stock_table[block].items():
            ts_symbol=symbol_format(symbol)
            data_per_stock = (stock_data[stock_data['ts_code'] == ts_symbol]).loc[:,
                             ['trade_date', 'open', 'close', 'low', 'high']]
            # reverse data frame
            data_per_stock = data_per_stock[::-1]
            data[name]=[list(row) for index, row in data_per_stock.iterrows()]

        return data


    def get_stock_data_with_symbol_list(self,symbol_list, begin,stop):
        """
        
        :param symbol: symbol list
        :param begin: 
        :param stop: 
        :return: 
        """
        data = []
        for each_symbol in symbol_list:
            each_stock_data = get_stock_k_data(each_symbol,begin,stop)
            if each_stock_data is None:
                continue
            data.append(each_stock_data)
        all_stock_data = pd.concat(data)
        return all_stock_data



# ---------------------------------------------
#              api  functions

def make_apps():
    # falcon.API instances are callable WSGI apps
    app = falcon.API()

    # Resources are represented by long-lived class instances
    index = IndexResource()
    block = BlockResource()
    # things will handle all requests to the '/things' URL path
    app.add_route('/index', index)
    app.add_route('/block', block)

    return app

# ---------------------------------------------



if __name__ == "__main__":
    app = make_apps()
    serve(app, host='127.0.0.1', port=8081)