import datetime
from pandas import read_csv, Series
import requests
import json
import math


def conv_ctime(date=(2020, 1, 1)):
    return str(math.floor(datetime.datetime(date[0], date[1], date[2], 5, 30).timestamp()))

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
        url = "https://in.finance.yahoo.com/quote/{}.NS".format(code.upper())
        r = requests.get(url)
        
        return (r.content)
    

    def histoical_data(self, code="", date_from=(2020, 1, 1), date_to=(2021, 1, 1), to_json=False):
        url = 'https://query1.finance.yahoo.com/v7/finance/download/{}.NS?period1={}&period2={}&interval=1d&events=history&includeAdjustedClose=true'.format(code.upper(), conv_ctime(date_from), conv_ctime(date_to))

        return (url)


nse = Nse()

# print(nse.get_intraday("atgl"))

df = read_csv(nse.histoical_data("reliance", (2010, 1, 1), (2020, 1, 1)))
print(df)


