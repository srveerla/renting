from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/rentings_db'
mongo = PyMongo(app)

@app.route('/rentings', methods=['GET'])
def get_rentings():
    rentings = list(mongo.db.rentings.find())
    return jsonify({"rentings": rentings})

@app.route('/rentings', methods=['POST'])
def create_renting():
    data = request.get_json()

    # Assuming the data structure, adjust as needed
    renting_record = {
        "userId": data.get("userId"),
        "bookId": data.get("bookId"),
        "startDate": data.get("startDate"),
        "endDate": data.get("endDate"),
    }

    mongo.db.rentings.insert_one(renting_record)

    return jsonify({"renting": renting_record}), 201

if __name__ == '__main__':
    app.run(port=5002)
