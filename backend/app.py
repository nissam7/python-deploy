import os
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

# create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    message VARCHAR(255)
)
""")
db.commit()

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get("name")
    message = data.get("message")

    cursor.execute(
        "INSERT INTO messages (name, message) VALUES (%s, %s)",
        (name, message)
    )
    db.commit()

    return jsonify({"status": "Saved to AWS RDS successfully!"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

