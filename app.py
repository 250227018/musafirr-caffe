from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

MENU = {
    "Hot Drinks": [
        {"id": 1, "name": "Karak Chai", "price": 40, "emoji": "☕"},
        {"id": 2, "name": "Cappuccino", "price": 180, "emoji": "☕"},
        {"id": 3, "name": "Kashmiri Chai", "price": 90, "emoji": "🍵"},
    ],
    "Cold Drinks": [
        {"id": 4, "name": "Cold Coffee", "price": 160, "emoji": "🧋"},
        {"id": 5, "name": "Mango Lassi", "price": 120, "emoji": "🥭"},
    ],
    "Food": [
        {"id": 6, "name": "Samosa", "price": 40, "emoji": "🔺"},
        {"id": 7, "name": "Burger", "price": 280, "emoji": "🍔"},
        {"id": 8, "name": "Masala Fries", "price": 130, "emoji": "🍟"},
    ],
}

@app.route("/")
def index():
    return render_template("index.html", menu=MENU)

@app.route("/order", methods=["POST"])
def order():
    data = request.get_json()
    total = sum(i["price"] * i["qty"] for i in data["items"])
    return jsonify({"success": True, "total": total})

if __name__ == "__main__":
    app.run(debug=True)