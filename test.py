import yfinance as yf
import json, requests
import pandas as pd
def test_function():

    msft = yf.Ticker("MSFT")
    aapl = yf.Ticker("AAPL")
    #print(msft.info)
    #x = msft.info
    #print(x['sector'])

    hist = msft.history(period = "1mo")
    print(hist)
    hist2 = aapl.history(period="1mo")
    print(hist2)
    print(hist.columns)
    print(hist[["Open"]])
    #print(hist.loc[Date[0],"Open"])



test_function()
