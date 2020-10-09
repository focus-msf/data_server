# -*- coding: utf-8 -*-
from mootdx.quotes import Quotes
from mootdx.consts import MARKET_SH,MARKET_SZ


# data = client.k(symbol="000001", begin="2017-07-03", end="2017-07-10")
client = Quotes.factory(market='std')
data = client.index(frequency=9, market=MARKET_SH, symbol='000001', start=0, offset=1)
print(data)
pass


# from mootdx.quotes import Quotes
#
# client = Quotes.factory(market='std')
