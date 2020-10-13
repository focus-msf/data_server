# -*- coding: utf-8 -*-
"""
1. 遍历目录下的文件
2. 对文件内容进行处理
"""
import os
import glob
import pprint

def get_table(file_name):
    table_data = {}
    table_data_reverse = {}
    with open(file) as f:
        data = f.readlines()[1:-1]
        for each_line in data:
            temp = each_line.split('\t')
            symbol, name = temp[0],temp[1]
            table_data[name] = symbol
            table_data_reverse[symbol] = name
    return table_data, table_data_reverse

    pass
if __name__ == '__main__':
    # files = os.listdir('.')
    files = glob.glob('*.txt')
    data = {}
    data_reverse = {}
    for file in files:
        block_name = file[:-12]
        table, table_reverse = get_table(file)
        data[block_name] = table
        data_reverse[block_name] = table_reverse

    # print(data_reverse)
    pprint.pprint(data_reverse)
    # print(data_reverse.keys())
    # print(len(data_reverse.keys()))



    pass