from flask_app import app
from flask import jsonify, request

# Initialize Users dictionary
users = {}

@app.route("/api/users", methods=["GET", "POST"])
def handle_users():
    if request.method == "GET":
        return jsonify({"users": users})

    elif request.method == "POST":
        try:
            data = request.get_json()
            print("printing the data received from frontend", data)

            new_id = str(len(users))
            users[new_id] = data

            return jsonify({"message": "Users updated successfully"})
        except Exception as e:
            print("Error occurred: ", e)
            return jsonify({"message": "could not update users"}), 500


@app.route("/api/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def handle_user(user_id):
    """
    This function takes an ID as a dynamic URL parameter, for example '0'.
    Note:
    - GET method is only available for debugging purposes, to test for a specific user
    open the browser with for example http://localhost:5000/api/users/0 to see the data

    - The assignment is to implement the PUT and DELETE methods for the specific ID, see assignment for specific instructions
    """
    if user_id in users:
        if request.method == "GET":
            return jsonify(users[user_id])
    else:
        return jsonify({"message": "User not found"}), 404

