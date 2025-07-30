from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection (localhost for now, will use service name in K8s)
mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client["userdb"]
collection = db["users"]

# Sample data insert (only if collection is empty)
if collection.count_documents({}) == 0:
    collection.insert_many([
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"}
    ])

@app.route('/api/data')
def home():
    return jsonify({"message": "Hello from Backend API with MongoDB!"})

@app.route('/api/users')
def users():
    user_list = list(collection.find({}, {"_id": 0}))  # Remove Mongo ObjectId
    return jsonify(user_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

