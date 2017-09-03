#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
import pandas as pd

ticker_symbols = ["1736:JP", "6758:JP", "8159:JP", "8923:JP", "6960:JP", "1736:JP",
                  "1758:JP", "1799:JP", "8066:JP", "4202:JP", "6954:JP"]

def fetch_stock_data(symbol):
    sleep(0.5)
    resp = requests.get("https://www.bloomberg.com/quote/" + symbol)

    if resp.ok:
      html = BeautifulSoup(resp.text, "html.parser")
    else:
      print "error: {}".format(resp.status_code)

    data_table = html.body.find('div', attrs={'class':'data-table_detailed'})
    entries = data_table.find_all('div')

    pe_ratio = entries[23].text     # price per earnings ratio
    e_per_share = entries[26].text  # earnings per share
    price = entries[2].text         # price
    market_cap = entries[29].text   # market capitalization

    return {"symbol": symbol, "price": price, "pe": pe_ratio, "es": e_per_share, 
            "cap": market_cap}


stock_data = []
for symbol in ticker_symbols:
  stock_data.append(fetch_stock_data(symbol))

df = pd.DataFrame(stock_data)
print df.describe()
