import os
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        connection_timeout=5
    )

@app.route('/submit', methods=['POST'])
def submit():
    try:
        db = get_db()
        cursor = db.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            message VARCHAR(255)
        )
        """)

        cursor.execute(
            "INSERT INTO messages (name, message) VALUES (%s, %s)",
            (request.json['name'], request.json['message'])
        )
        db.commit()

        return jsonify({"status": "Saved to AWS RDS successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🔴 THIS LINE IS CRITICAL — WITHOUT THIS, CONTAINER EXITS
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

