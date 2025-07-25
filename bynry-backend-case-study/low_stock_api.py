from flask import Flask, jsonify,request

app = Flask(__name__)

inventory = [
    {"name": "Product A", "stock_quantity": 5},
    {"name": "Product B",  "stock_quantity": 2},
    {"name": "Product C", "stock_quantity": 10},
]

@app.route('/low_stock', methods=['GET'])

def low_stock():
    threshold = int(request.args.get("threshold", 5))
    low_stock_items = [item for item in inventory if item["stock_quantity"] < threshold]
    return jsonify(low_stock_items), 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)
