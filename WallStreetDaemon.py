import pandas as pd
import yfinance as yf
from yahoo_fin import stock_info as si

# requires panda, yfinance and yahoo-fin, sometimes listed as yahoo-fin
# all dates in format of 2020-01-05
# all company names in format of TSLA
# all arguments inputed as strings
#all prices in USD

# use getStockInfo to create data frame df
def getStockInfo(company,startDate, endDate):
    data = yf.download(company, start=startDate, end=endDate)
    return data # returns panda dataframe

def getMarketHiLo(df, date):
    high = df.loc[str(date),['High']][0]
    low = df.loc[str(date),['Low']][0]
    hiLo = (high, low)
    return hiLo # outputted as a tuple

def getCurrentPrice(company):
    si.get_live_price(company) # numerical output

