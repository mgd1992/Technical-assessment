from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


PRODUCTS = {
	"GR1": {"name": "Green Tea", "price": 3.11},
	"SR1": {"name": "Strawberries", "price": 5.00},
	"CF1": {"name": "Coffee", "price": 11.23}
}

cart = []

def calculate_total(cart):

	item_count = {}
	for item in cart:
			code = item["code"]
			item_count[code] = item_count.get(code, 0) + 1

	total = 0

	for code, quantity in item_count.items():
			price = PRODUCTS[code]["price"]


			if code == "GR1":
					total += (quantity // 2 + quantity % 2) * price
			elif code == "SR1" and quantity >= 3:
					total += quantity * 4.50
			elif code == "CF1" and quantity >= 3:
					total += quantity * (price * 2 / 3)
			else:
					total += quantity * price

	return round(total, 2)

@app.route("/")
def home():
	return jsonify({"message": "Backend funcionando correctamente!"})

@app.route("/products", methods=["GET"])
def get_products():
	return jsonify([{"code": code, **data} for code, data in PRODUCTS.items()])

@app.route("/cart", methods=["POST"])
def add_to_cart():
	data = request.json
	cart.append(data)
	total = calculate_total(cart)
	return jsonify({"message": "Producto agregado", "cart": cart, "total": total})

@app.route("/cart", methods=["GET"])
def get_cart():
	total = calculate_total(cart)
	return jsonify({"cart": cart, "total": total})

@app.route("/cart/clear", methods=["POST"])
def clear_cart():
	global cart
	cart = []
	return jsonify({"message": "Carrito vaciado", "cart": [], "total": 0.0})

if __name__ == "__main__":
	app.run(debug=True)
