import requests
import os

class DataFetcher:
    '''Fetches data from VintageAlpha API'''
    def __init__(self, symbol):
        # Create url strings 
        self.data_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={os.environ['API_KEY']}"

        # Fetch the data
        self.fetch_data()

    # Fetch Drip time series data
    def fetch_data(self):
        drip_response = requests.get(self.data_url)
        self.stock_data = drip_response.json()

    def get_drip_data(self):
        return self.stock_data['Monthly Adjusted Time Series']

    def get_stock_data(self):
        return self.stock_data