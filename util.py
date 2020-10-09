# -*- coding: utf-8 -*-
import pendulum
def time_format_1(dt):
    return dt.format('YYYYMMDD')

def symbol_format(symbol):
    symbol_list = symbol.split(',')
    res = []

    for each in symbol_list:
        if each.startswith("601"):
            res.append(each+".SH")
        if each.startswith("600"):
            res.append(each+".SH")
        if each.startswith("300"):
            res.append(each+".SZ")
        if each.startswith("000"):
            res.append(each+".SZ")
        if each.startswith("003"):
            res.append(each+".SZ")
        if each.startswith("002"):
            res.append(each+".SZ")
    res = ','.join(res)
    return res

