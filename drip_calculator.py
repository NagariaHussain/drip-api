from data_processor import DataProcessor

class DRIPCalculator:
    '''Calculates and returns DRIP projection data'''
    def __init__(self, data_processor):
        self.dp: DataProcessor = data_processor
        self.projected_data = None

    def generate_projection(self, start_balance, employee_contrib, \
        is_reinvested, tax_percent, n_years):
        '''Generates forward projection based on data'''
        # To store projected data rows
        self.projected_data = []

        share_price = self.dp.get_EV()
        stock_increase = self.dp.get_CAGR(n_years)
        print(stock_increase)
        shares = round(start_balance / share_price, 3)
        D_initial = self.dp.get_avg_dividend_data() * 4 * shares
        div_growth = self.dp.get_dgr_percent()
        D_final = D_initial

        for i in range(n_years):
            shares = round(start_balance / share_price, 3)
            growth = round((stock_increase / 100) * start_balance, 2)
            end_balance = round(start_balance + employee_contrib * 12 + growth, 2)

            if is_reinvested:
                reinvested =  D_final - (tax_percent / 100) * D_final 
                end_balance += reinvested
            else:
                reinvested = 0

            # Collect current projected year data            
            self.projected_data.append({
                "year": i + 1,
                "start_balance": round(start_balance, 2),
                "share_price": round(share_price, 2),
                "number_of_shares": round(shares, 3),
                "growth": round(growth, 2),
                "dividend": round(D_final, 2),
                "reinvested": round(reinvested, 2),
                "end_balance": round(end_balance, 2)
            })

            start_balance = end_balance
            share_price = round(share_price + (stock_increase / 100) * share_price, 2)
            D_initial = D_final
            D_final = (1 + (div_growth / 100)) * D_initial

    def get_projection_data(self):
        '''Returns nicely arranged data for JSON output'''
        return self.projected_data