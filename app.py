from data_fetcher import DataFetcher
from data_processor import DataProcessor
from drip_calculator import DRIPCalculator

# Flask
from flask import Flask, request, abort, jsonify
# For enabling cors
from flask_cors import CORS

# Create flask app
app = Flask(__name__)
CORS(app)

@app.route("/")
def handle_api_req():
    # Evaluate start balance
    start_balance = handle_start_balance(request.args.get("start_balance")) 

    # Access security symbol
    symbol = request.args.get("symbol")

    # If symbol is not provided
    if not symbol:
        abort(404, description="symbol must be provided")
    
    # Access number of years
    n_years = request.args.get("n_years")

    # If n_years not provided
    if not n_years:
        abort(404, description="n_years must be provided")
    else:
        try:
            n_years = int(n_years)

            # Number of years must be greater than 0
            if n_years <= 0:
                abort(404, description="n_years should be positive integer")
        except ValueError as ve:
            # Invalid value for number of years
            abort(404, description="invalid n_years value")

    # Access tax percentage value
    tax_percent = request.args.get("tax_percent")

    if not tax_percent:
        # Default value is 0
        tax_percent = 0
    else:
        try:
            tax_percent = float(tax_percent)
        except ValueError as ve:
            # Invalid value for tax percent
            abort(404, description="invaid tax_percent value")

    # Access reinvested boolean
    reinvested = request.args.get("reinvested")

    # If reinvested in not provided
    if not reinvested:
        # Default value is True
        reinvested = True
    else:
        # If reinvested is true
        if reinvested == "true":
            reinvested = True
        # If reinvested is false
        elif reinvested == "false":
            reinvested = False
        # If any other value is provided
        else:
            abort(404, "invalid reinvested value, should be either true or false")

    emp_contrib = request.args.get("emp_contrib")

    # If employee contribution is not given
    if not emp_contrib:
        # Use default value
        emp_contrib = 0
    else:
        # Try to convert the value to float
        try:
            emp_contrib = float(emp_contrib)
        except ValueError as ve:
            abort(404, "invalid emp_contrib value")

    # Perform the calculation
    df = DataFetcher(symbol)
    dp = DataProcessor(df.get_drip_data(), df.get_stock_data())
    dc = DRIPCalculator(dp)

    # Generate projections based on given data
    dc.generate_projection(start_balance, emp_contrib, reinvested, tax_percent, n_years)

    # Get projection data
    data = dc.get_projection_data()

    # Return data as json
    return jsonify(data)


def handle_start_balance(start_balance):
    if not start_balance:
        # Start balance not provided
        abort(404, description="start_balance must be provided")
    else:
        try:
            start_balance = float(start_balance)
        except ValueError as ve:
            # Invalid start balance value
            abort(404, description="invalid start_balance value")

    return start_balance

# Return errors as JSON
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

if __name__ == "__main__":
    app.run()