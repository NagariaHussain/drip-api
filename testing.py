# For making API calls
import requests

# TEST CASES:
# 1. Reinvested and Taxable
# 2. Reinvested and Non-taxable
# 3. Not reinvested

# API Testing ------------------
# URL = "http://127.0.0.1:5000/api?start_balance=5000&tax_percent=9.8&reinvested=true&symbol=MMM&n_years=10"
# res = requests.get(URL)
# assert res.status_code == 200
# print(res.json())

# URL = "http://127.0.0.1:5000/api?symbol=IBM&start_balance=1500&reinvested=false&tax_percent=10&n_years=5"
# res = requests.get(URL)
# print(res.json())
# assert res.status_code == 200


# # Start balance not provided
# URL = "http://127.0.0.1:5000/api?symbol=IBM&reinvested=false&tax_percent=10&n_years=5"
# res = requests.get(URL)

# assert res.status_code == 404
# assert res.json()['error'] == '404 Not Found: start_balance must be provided'
# # -----------------------------

# # Invalid start balance
# URL = "http://127.0.0.1:5000/api?start_balance=hello&symbol=IBM&reinvested=false&tax_percent=10&n_years=5"
# res = requests.get(URL)

# assert res.status_code == 404
# assert res.json()['error'] == '404 Not Found: invalid start_balance value'
# # -----------------------------

# # Symbol not provided
# URL = "http://127.0.0.1:5000/api?start_balance=15000&reinvested=false&tax_percent=10&n_years=5"
# res = requests.get(URL)

# assert res.status_code == 404
# assert res.json()['error'] == '404 Not Found: symbol must be provided'

# # -----------------------------


# # Number of years not provided
# URL = "http://127.0.0.1:5000/api?start_balance=15000&symbol=MMM&reinvested=false&tax_percent=10"
# res = requests.get(URL)

# assert res.status_code == 404
# assert res.json()['error'] == '404 Not Found: n_years must be provided'

# # -----------------------------

# # Invalid number of years provided
# URL = "http://127.0.0.1:5000/api?start_balance=15000&reinvested=false&symbol=IBM&tax_percent=10&n_years=hello"
# res = requests.get(URL)

# assert res.status_code == 404
# assert res.json()['error'] == '404 Not Found: invalid n_years value'

# # -----------------------------

# # Negative Number of years

# URL = "http://127.0.0.1:5000/api?n_years=-1&start_balance=15000&symbol=MMM&reinvested=false&tax_percent=10"
# res = requests.get(URL)

# assert res.status_code == 404
# assert res.json()['error'] == '404 Not Found: n_years should be positive integer'

# # -----------------------------

# # Invalid tax percent value

# URL = "http://127.0.0.1:5000/api?n_years=5&start_balance=15000&symbol=MMM&reinvested=false&tax_percent=hello"
# res = requests.get(URL)

# assert res.status_code == 404
# assert res.json()['error'] == '404 Not Found: invaid tax_percent value'

# # -----------------------------

# # Invalid reinvested value
# URL = "http://127.0.0.1:5000/api?n_years=5&start_balance=15000&symbol=MMM&reinvested=hello"
# res = requests.get(URL)

# assert res.status_code == 404
# assert res.json()['error'] == '404 Not Found: invalid reinvested value, should be either true or false'

# # -----------------------------

# # Invalid emp contrib value
# URL = "http://127.0.0.1:5000/api?n_years=5&start_balance=15000&symbol=MMM&reinvested=true&emp_contrib=hello"
# res = requests.get(URL)

# assert res.status_code == 404
# assert res.json()['error'] == '404 Not Found: invalid emp_contrib value'

# -----------------------------

URL = "http://127.0.0.1:5000?n_years=10&start_balance=5000&symbol=AMD"
res = requests.get(URL)
from pprint import pprint

pprint(res.json())
print("ALL tests passed!")

# Generating API spec

import markdown

with open('README.md', 'r') as f:
    # Generate HTML from markdown
    md = markdown.markdown(f.read())
    # Write the generated HTML to file
    with open('SPEC.html', 'w') as html_f:
        # Write heading
        html_f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DRIP API Specification</title>
    <link href="https://unpkg.com/@primer/css/dist/primer.css" rel="stylesheet" />
</head>
<body>
<div class="markdown-body">
''')
        # Write markdown body
        html_f.write(md)

        # Write tail
        html_f.write('''
</div>
</body>
</html>''')