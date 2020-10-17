# -*- coding: utf-8 -*-
import tushare as ts
ts.set_token('df1add767608a3a3481997959084b942014f8ebb218878d631e5fc8b')



pro = ts.pro_api()

#查询当前所有正常上市交易的股票列表

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
some = {}
for each_line in zip(data['ts_code'], data['symbol']):
    some[each_line[1]]=each_line[0]

print(some)