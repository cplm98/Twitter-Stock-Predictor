import requests
import json
from collections import OrderedDict
import matplotlib.pyplot as plt


class StockData:

    def __init__(self, symbol, ti):
        self.stock_symbol = symbol
        self.time_interval = ti
        self.open_price_list = []
        self.close_price = []
        self.time_stamps = [] # could probably create a dictionary instead but lists are fine for now

    def get_stock_data(self):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + self.stock_symbol + "&interval=" + self.time_interval + "&apikey=9AD6SV02MT4Z7G8W"
        r = requests.get(url)
        response = r.text
        response = json.loads(response, object_pairs_hook=OrderedDict) # gets stock data just fine
        print(response)
        return response

    def clean_stock_data(self, data):
        data = data['Time Series ('+ self.time_interval +')']
        for i in data:
            time_stamp = i
            open_price = data[time_stamp]['1. open']
            close_price = data[time_stamp]['4. close']
            self.open_price_list.append(open_price)
            self.time_stamps.append(time_stamp)
            #print(open_price)

    def plot(self):
        plt.scatter(self.time_stamps, self.open_price_list)
        plt.show()  # its plotting but there is no way it's right, it's almost plotting in order, which isn't right
        # plot looks right in excel, probably going to have to find a better plot tool


stock = StockData("TSLA", "15min")
stock.clean_stock_data(stock.get_stock_data())
stock.plot()

