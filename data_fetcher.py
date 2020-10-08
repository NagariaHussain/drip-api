import requests
import os

class DataFetcher:
    '''Fetches data from VintageAlpha API'''
    def __init__(self, symbol):
        # Create url strings 
        self.drip_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={os.environ['API_KEY']}"
        self.stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey={os.environ['API_KEY']}"

        # Fetch the data
        self.fetch_drip_data()
        self.fetch_stock_price_data()

    # Fetch Drip time series data
    def fetch_drip_data(self):
        drip_response = requests.get(self.drip_url)
        drip_response_json = drip_response.json()
        self.drip_data = drip_response_json['Monthly Adjusted Time Series']

    # Fetch stock price time series data
    def fetch_stock_price_data(self):
        stock_response = requests.get(self.stock_url)
        stock_response_json = stock_response.json()
        self.stock_price_data = stock_response_json

    def get_drip_data(self):
        return self.drip_data

    def get_stock_data(self):
        return self.stock_price_data