from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Shopping Bill Calculator - V1"

@app.route("/calculate", methods=["POST"])
def calculate_bill():
    data = request.get_json()
    price = data.get("price", 0)
    quantity = data.get("quantity", 0)
    
    total = price * quantity
    
    return jsonify({
        "price": price,
        "quantity": quantity,
        "total_bill": total
    }), 200

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)