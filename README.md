# DRIP API Specification

## Input Spec

### Required Parameters

1. `start_balance`: The starting investment amount.

2. `symbol`: Symbol of the security

3. `n_years`: The number of years for which the projection (plan) is to be determined.

### Optional Parameters

1. `reinvested`: Must be either `true` or `false`. The default value if `true`.

2. `tax_percent`: A value for tax percentage to be cut from the dividend amount for each year.

3. `emp_contrib`: Amount of monthly contribution by the employee.

## Output Spec

The data is returned in JSON format. The JSON contains a list of objects containing the following fields for each year:

* `year`: A positive integer representing the year number. Starts at 1.

* `start_balance`: Starting balance for this `year`.

* `share_price`: Starting share price of this year.

* `number_of_shares`: Number of shares bought this year.

* `dividend`: Dividend amount generated this year.

* `reinvested`: Amount reinvested after cutting tax, if any, from the dividend amount.

* `growth`: Growth in investment based on compound annual growth rate.

* `end_balance`: Ending balance for this year. Will be the starting balance for next year


## Examples

1. For getting the 5 year DRIP of the **MMM** stock with 15000$ as starting amount:

**root_url/api?start_balance=15000&n_years=5&symbol=MMM**

2. For getting the above data with 9.8% tax applied

**root_url/api?start_balance=15000&n_years=5&symbol=MMM&tax_percent=9.8**

3. For getting 10 year plan for **IBM** with 5000$ as starting investment amount. This time we want to see the balance without reinvestment.

**root_url/api?start_balance=5000&n_years=10&symbol=IBM&reinvested=false**


## Contact

Mohammad Hussain Nagaria


Email: hussainbhaitech@gmail.com


Github: NagariaHussain

