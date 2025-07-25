from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/product', methods=['POST'])
def create_product():
    data = request.get_json()
    required_fields = ['name', 'description', 'price', 'stock_quantity']

    for field in required_fields:
    
     if field not in data:
        return jsonify({'error': f'Missing field: {field}'}), 400

     product = {
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
        "stock_quantity": data[" stock_quantity"]
    }

    return jsonify({"message ": "Product created", "product": product}), 201

if __name__ == '__main__':
    app.run(debug=True)
