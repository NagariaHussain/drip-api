import requests
import os

# For throwing HTTP exceptions
from flask import abort

class DataFetcher:
    '''Fetches data from VintageAlpha API'''
    def __init__(self, symbol):
        # Create url strings 
        self.data_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={os.environ['API_KEY']}"

        # Fetch the data
        self.fetch_data()

    # Fetch Time series data
    def fetch_data(self):
        response = requests.get(self.data_url)
        # Convert it from JSON
        self.stock_data = response.json()

    # Returns full time series
    def get_drip_data(self):
        try: 
            return self.stock_data['Monthly Adjusted Time Series']
        except Exception as ke:
            # The symbol does not exist
            abort(404, "Make sure the symbol exists")

    # Returns full time series with meta data
    def get_stock_data(self):
        return self.stock_data