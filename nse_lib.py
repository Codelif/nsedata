import csv
from os import read
from pandas import read_csv, Series, read_html
import requests
import json


class Nse():
    

    def __init__(self):
        pass

    def all_codes(self, to_json=False):
        equity_csv = 'https://archives.nseindia.com/content/equities/EQUITY_L.csv'
        df = read_csv(equity_csv)
        if to_json:
            return json.dumps(Series(df["NAME OF COMPANY"].values,index=df.SYMBOL).to_dict())
        return (Series(df["NAME OF COMPANY"].values,index=df.SYMBOL).to_dict())
    def get_intraday(self, code="", to_json=False):
        url = "https://www.nseindia.com/get-quotes/equity?symbol={}".format(code.upper())
        # df = read_html(url)
        return (read_html('https://en.wikipedia.org/wiki/History_of_Python'))



nse = Nse()
print(nse.get_intraday("atgl"))