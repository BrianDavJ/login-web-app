from flask import Flask, request, jsonify, send_from_directory
import json

app = Flask(__name__)


# Load or initialize the user data from a JSON file
with open("./static/backend/users.json", "r") as f:
    users = json.load(f)

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

# Endpoint for login
@app.route('/', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Check if user exists and password matches
    for user in users:
        if user["email"] == email and user["password"] == password:
            return jsonify({"token": "placeholder-token-123"}), 200

    # If no match found, return an error response
    return jsonify({"error": "Invalid email or password"}), 401

# Endpoint for signup
@app.route('/', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Check if the user already exists
    for user in users:
        if user["email"] == email:
            return jsonify({"error": "User already exists"}), 409

    # If new user, add to users and save
    new_user = {"email": email, "password": password}
    users.append(new_user)
    with open("users.json", "w") as f:
        json.dump(users, f)

    return jsonify({"message": "User created successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
