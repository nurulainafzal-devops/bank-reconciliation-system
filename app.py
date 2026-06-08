

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    if not file:
        return "No file uploaded"

    df = pd.read_csv(file)

    return render_template(
        "report.html",
        tables=[df.to_html(classes="table", index=False)]
    )

if __name__ == "__main__":
    app.run(debug=True)




from utils.reconciliation_engine import reconcile

bank = [
    {"Date": "2025-01-01", "Description": "Salary", "Amount": 5000},
    {"Date": "2025-01-02", "Description": "ATM withdrawal", "Amount": -200}
]

internal = [
    {"Date": "2025-01-01", "Description": "Monthly Salary", "Amount": 5000},
]

result = reconcile(bank, internal)

print(result)
