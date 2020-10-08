import requests



# Test both the bussiness logic and API

# TEST CASES:
# 1. Reinvested and Taxable
# 2. Reinvested and Non-taxable
# 3. Not reinvested

# API Testing ------------------
URL = "http://127.0.0.1:5000/api?start_balance=5000&tax_percent=9.8&reinvested=true&symbol=MMM&n_years=10"
res = requests.get(URL)

URL = "http://127.0.0.1:5000/api?symbol=IBM&start_balance=1500&reinvested=false&tax_percent=10&n_years=5"
res = requests.get(URL)