from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection setup
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

# Route: Get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(products), 200

    except mysql.connector.Error as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500

# Route: Get product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()
        cursor.close()
        conn.close()

        if product:
            return jsonify(product), 200
        else:
            return jsonify({"message": "Product not found"}), 404

    except mysql.connector.Error as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500

    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
