import datetime
import matplotlib.pyplot  as plt
import yfinance as fin
import pandas_datareader.data as dtr


def plot_usd_to_rub():
    fin.pdr_override()
    df = dtr.DataReader('USDRUB=X', datetime.datetime.today() - datetime.timedelta(days=365))
    plt.plot(df.index, df['Close'])
    plt.show()


def plot_usd_to_btc():
    fin.pdr_override()
    df = dtr.DataReader('BTC-USD', datetime.datetime.today() - datetime.timedelta(days=365))
    plt.plot(df.index, df['Close'])
    plt.show()
