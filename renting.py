from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/library"
mongo = PyMongo(app)

class Renting:
    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

@app.route('/rentings', methods=['GET'])
def get_rentings():
    rentings = list(mongo.db.rentings.find({}, {'_id': 0}))
    return jsonify(rentings)

@app.route('/rent', methods=['POST'])
def rent_book():
    data = request.get_json()
    user_id = data['user_id']
    book_id = data['book_id']

    # Check if the book is already rented
    existing_renting = mongo.db.rentings.find_one({'book_id': book_id})
    if existing_renting:
        return 'Book is already rented', 400

    # If not rented, proceed with renting
    renting = Renting(user_id, book_id)
    mongo.db.rentings.insert_one(renting.__dict__)
    return 'Book rented', 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
