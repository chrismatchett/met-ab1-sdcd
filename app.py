from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "changeme-secret-key"

APP_TITLE = "ChangeMe"

# Fake product data
products = [
    {"id": 1, "name": "Laptop Pro", "price": 999.99, "category": "Electronics"},
    {"id": 2, "name": "Wireless Mouse", "price": 29.99, "category": "Electronics"},
    {"id": 3, "name": "Python Book", "price": 39.99, "category": "Books"},
    {"id": 4, "name": "Coffee Mug", "price": 12.99, "category": "Home"},
    {"id": 5, "name": "Mechanical Keyboard", "price": 149.99, "category": "Electronics"},
]

# Fake users (username: password)
users = {
    "admin": "password123",
    "user1": "pass1",
}


@app.route("/")
def index():
    return render_template("index.html", products=products, title=APP_TITLE)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if users.get(username) == password:
            session["user"] = username
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid credentials.", "danger")
    return render_template("login.html", title=APP_TITLE)


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out.", "info")
    return redirect(url_for("index"))


@app.route("/search")
def search():
    query = request.args.get("q", "").lower()
    results = [p for p in products if query in p["name"].lower()] if query else []
    return render_template("search.html", results=results, query=query, title=APP_TITLE)


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        flash("Product not found.", "danger")
        return redirect(url_for("index"))
    # Fake AI recommendation
    recommendations = [p for p in products if p["id"] != product_id][:2]
    return render_template("product.html", product=product, recommendations=recommendations, title=APP_TITLE)


@app.route("/cart", methods=["GET", "POST"])
def cart():
    if "cart" not in session:
        session["cart"] = []
    if request.method == "POST":
        product_id = int(request.form.get("product_id"))
        session["cart"] = session.get("cart", []) + [product_id]
        session.modified = True
        flash("Item added to cart!", "success")
        return redirect(url_for("cart"))
    cart_items = [p for p in products if p["id"] in session["cart"]]
    total = sum(p["price"] for p in cart_items)
    return render_template("cart.html", cart_items=cart_items, total=total, title=APP_TITLE)


@app.route("/checkout", methods=["POST"])
def checkout():
    session["cart"] = []
    session.modified = True
    flash("Payment simulated successfully! Order placed.", "success")
    return redirect(url_for("index"))


@app.route("/dashboard")
def dashboard():
    if session.get("user") != "admin":
        flash("Admin only.", "danger")
        return redirect(url_for("login"))
    stats = {
        "total_products": len(products),
        "total_users": len(users),
        "simulated_orders": 42,
        "revenue": 15823.50,
    }
    return render_template("dashboard.html", stats=stats, title=APP_TITLE)


if __name__ == "__main__":
    app.run(debug=True)
