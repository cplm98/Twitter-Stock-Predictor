import requests
import json
from collections import OrderedDict
import matplotlib.pyplot as plt


class StockData:

    def __init__(self, symbol, time_interval, op_size='compact'):
        self.stock_symbol = symbol
        self.time_interval = time_interval
        self.op_size = op_size
        self.open_price_list = []
        self.close_price_list = []
        self.time_stamps = [] # could probably create a dictionary instead but lists are fine for now
        self.data_list = []  # list of tuples that combines the above three lists

    def get_stock_data(self):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + self.stock_symbol + "&interval=" + self.time_interval + "&outputsize=" + self.op_size + "&apikey=9AD6SV02MT4Z7G8W"
        r = requests.get(url)
        response = r.text
        response = json.loads(response, object_pairs_hook=OrderedDict)  # gets stock data just fine
        print(response)
        return response

    def clean_stock_data(self, data):
        data = data['Time Series (' + self.time_interval + ')']
        for i in data:
            time_stamp = str(i)
            open_price = int(100*float(data[time_stamp]['1. open']))  # store prices in cents
            close_price = int(100*float(data[time_stamp]['4. close']))  # store prices in cents
            self.open_price_list.append(open_price) #matplotlib was plotting it wrong cause it saw the prices as strings
            self.close_price_list.append(close_price)
            self.time_stamps.append(time_stamp)  # save as string, when you take it back out of the db convert it to datetime
            self.data_list.append((time_stamp, open_price, close_price))

    # This is just for prototyping and checking data
    def plot_data(self):
        #plt.scatter(self.time_stamps, self.open_price_list)
        plt.plot(self.time_stamps, self.open_price_list)
        plt.show()  # its plotting but there is no way it's right, it's almost plotting in order, which isn't right
        # plot looks right in excel, probably going to have to find a better plot tool


# stock = StockData("TSLA", "15min", "full")
# stock.clean_stock_data(stock.get_stock_data())
# print(stock.data_list)
# print(stock.time_stamps)
# print(stock.open_price_list)
# stock.plot_data()

