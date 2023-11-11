from flask import Flask, request, jsonify

app = Flask(__name__)

# Renting database
rentals = {}

# Rent a book
@app.route("/rentals", methods=["POST"])
def rent_book():
    rental_data = request.get_json()
    rental_id = rental_data["rental_id"]
    user_id = rental_data["user_id"]
    book_id = rental_data["book_id"]
    due_date = rental_data["due_date"]

    # TODO: Validate the rental data

    rentals[rental_id] = {
        "user_id": user_id,
        "book_id": book_id,
        "due_date": due_date,
        "status": "rented"
    }

    return jsonify({
        "success": True,
        "message": "Book rented successfully."
    })

# Get all rentals for a user
@app.route("/rentals/user/<user_id>", methods=["GET"])
def get_user_rentals(user_id):
    user_rentals = []
    for rental_id, rental_data in rentals.items():
        if rental_data["user_id"] == user_id:
            user_rentals.append(rental_data)

    return jsonify({
        "success": True,
        "rentals": user_rentals
    })

# Get the status of a rental
@app.route("/rentals/<rental_id>/status", methods=["GET"])
