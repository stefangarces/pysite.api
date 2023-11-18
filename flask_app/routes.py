from flask_app import app
from flask import jsonify, request

# Initialize Users dictionary
users = {}

@app.route("/api/users", methods=["GET", "POST"])
def handle_users():
    if request.method == "GET":
        return jsonify({"users": users})

    elif request.method == "POST":
        # Received new request to add a user
        try:
            data = request.get_json()
            print("printing the data received from frontend", data)

            # Generate a new unique ID based on the length of users dictionary
            new_id = str(len(users))
            users[new_id] = data

            return jsonify({"message": "Users updated successfully"})
        except Exception as e:
            print("Error occurred: ", e)
            return jsonify({"message": "could not update users"}), 500


@app.route("/api/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def handle_user(user_id):
    if user_id in users:
        if request.method == "GET":
            return jsonify(users[user_id])
        elif request.method == "PUT":
            # Get the data sent with the request
            data = request.get_json()
            if data and "name" in data:
                # Update the user's name
                users[user_id]['name'] = data["name"]
                return jsonify(users[user_id])
            else:
                return jsonify({"message": "Invalid data"}), 400
        elif request.method == "DELETE":
            # Delete the user
            del users[user_id]
            return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"message": "User not found"}), 404
