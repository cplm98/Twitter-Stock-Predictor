import requests
import json


class StockData:

    def __init__(self, symbol, ti):
        self.stock_symbol = symbol
        self.time_interval = ti

    def get_stock_data(self):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + self.stock_symbol + "&interval=" + self.time_interval + "&apikey=9AD6SV02MT4Z7G8W"
        r = requests.get(url)
        response = r.text
        response = json.loads(response) # gets stock data just fine
        print(response)


stock = StockData("TSLA", "15min")
stock.get_stock_data()

