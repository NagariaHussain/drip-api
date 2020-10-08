from data_fetcher import DataFetcher
from data_processor import DataProcessor
from drip_calculator import DRIPCalculator

# Flask
from flask import Flask, request, abort

# Create flask app
app = Flask(__name__)


df = DataFetcher("MMM")
dp = DataProcessor(df.get_drip_data(), df.get_stock_data())
dc = DRIPCalculator(dp)

# Generate report
dc.generate_projection(1500, 0, False, 0, 5)

# Print projected data
print(dc.get_projection_data())


@app.route("/api")
def handle_api_req():
    print("Start Balance: ", request.args.get("start_balance"))
    print("Tax Percent: ", request.args.get("tax_percent"))
    print("Symbol: ", request.args.get("symbol"))
    print("Reinvested: ", request.args.get("reinvested"))
    print("Years:", request.args.get("n_years"))
    print("Employee Contrib", request.args.get("emp_contrib"))

    return "Hello"

if __name__ == "__main__":
    app.run()