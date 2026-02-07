import os
import mysql.connector
from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

try:
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        connection_timeout=5
    )
    cursor = db.cursor()
    print("✅ Connected to AWS RDS")
except Exception as e:
    print("❌ RDS connection failed:", e)
    sys.exit(1)

