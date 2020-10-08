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
        self.drip_data = drip_response.json()

    # Fetch stock price time series data
    def fetch_stock_price_data(self):
        pass

    def get_drip_data(self):
        return self.drip_data['Monthly Adjusted Time Series']

    def get_stock_data(self):
        return self.drip_data