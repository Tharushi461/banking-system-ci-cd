from flask import Flask, request, jsonify
from bank_operations import BankAccount

app = Flask(__name__)

# In-memory account for simplicity
account = BankAccount(account_number="123456", holder_name="John Doe", balance=1000.0)

@app.route("/")
def welcome():
    return "Welcome to the Banking System API!"

@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.get_json()
    amount = data.get("amount", 0)
    result = account.deposit(amount)
    return jsonify({"message": result, "balance": account.balance})

@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.get_json()
    amount = data.get("amount", 0)
    result = account.withdraw(amount)
    return jsonify({"message": result, "balance": account.balance})

@app.route("/balance", methods=["GET"])
def balance():
    result = account.check_balance()
    return jsonify({"message": result, "balance": account.balance})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
