from datetime import datetime

class DataProcessor:
    '''Processes raw fetched data.'''
    def __init__(self, drip_data, stock_data):
        self.drip_data = drip_data
        self.stock_data = stock_data

        # Calculate required dividend data
        self.calculate_dividends_by_year()
        self.calculate_avg_dividends_by_year()
    
    def calculate_dividends_by_year(self):
        # For storing dividend amounts
        self.dividends_by_year = {}

        # For keeping track of unique years
        self.unique_years = set()

        for date in self.drip_data:
            # Get the dividend amount as float
            dividend = float(self.drip_data[date]["7. dividend amount"])

            # Extract the year from date string
            year = datetime.strptime(date, '%Y-%m-%d').year

            # Add to unique years
            self.unique_years.add(year)

            # If there was a dividend that month
            if dividend > 0:
                # Record the dividend amount in dict
                if year in self.dividends_by_year:
                    self.dividends_by_year[year].append(dividend)
                else:
                    self.dividends_by_year[year] = [dividend]
        
    def calculate_avg_dividends_by_year(self):
        '''Returns dict containing tuple (avg, xdividents)'''
        self.avg_data = {}

        # Find average by years
        for year in self.dividends_by_year:
            # Access year's dividends list
            divs = self.dividends_by_year[year]
            self.avg_data[year] = (sum(divs) / len(divs)), len(divs)
        
        # Handling years with no dividends
        for year in self.unique_years:
            if not (year in self.avg_data):
                self.avg_data[year] = 0, 0

        # For testing only
        print("Unique years: ", self.unique_years)
        print("Average div data calc complete, Data: ", self.avg_data)

    def get_dgr_percent(self, n_years=5):
        # Return 0 if no dividend given in any year
        if (len(self.dividends_by_year) == 0):
            return 0

        growths = []
        n_years = min(n_years, len(self.dividends_by_year) - 2)
        current_year = datetime.now().year

        for y in range(current_year, current_year - 1 - n_years, -1):
            # This year
            D2 = (self.avg_data[y][0] / self.avg_data[y][1]) * 4
            # Prev year
            D1 = (self.avg_data[y - 1][0] / self.avg_data[y - 1][1]) * 4
            
            # Add growth to the growths list
            growths.append((D2 / D1) - 1)
        
        return (sum(growths) / len(growths)) * 100

    def get_avg_dividend_data(self):
        '''Returns avg of current year'''
        return self.avg_data[datetime.now().year][0]

    def get_EV(self):
        '''Returns end value of the stock'''

        # Get latest market date
        last_stock_update = self.stock_data["Meta Data"]["3. Last Refreshed"]

        # Get latest stock price
        EV = self.stock_data["Monthly Adjusted Time Series"][last_stock_update]["5. adjusted close"]

        # Save for future use
        self.EV = float(EV)

        # Return as float
        return float(EV)
    
    def get_BV(self, n_years=10):
        '''Returns begin value of the stock'''
        # Begin value date
        bv_date = None
        current_year = datetime.now().year

        # Calculate begin year
        bv_year = current_year - n_years

        # Begin month is same as end month
        bv_month = datetime.now().month

        for date in self.stock_data["Monthly Adjusted Time Series"]:
            date_match = "{}-{:0>2}".format(bv_year, bv_month)
            if date_match in date:
                bv_date = date
                break
        
        print("BV_DATE: ", bv_date)
        BV = self.stock_data["Monthly Adjusted Time Series"][bv_date]["4. close"]

        # Save for future use
        self.BV = float(BV)
        return float(BV)

    def get_CAGR(self, n_years=5):
        # Upper bound on number of years
        # Based on historical data avialability

        n_years = min(n_years, len(self.unique_years) - 1)

        # Get EV and BV
        BV = self.get_BV(n_years)
        EV = self.get_EV()
        
        print("Using {} years to calculate CAGR".format(n_years))
        print("EV: ", EV)
        print("BV: ", BV)

        CAGR = ((EV / BV) ** (1 / n_years)) - 1

        # Return CAGR as percentage
        return (CAGR * 100)