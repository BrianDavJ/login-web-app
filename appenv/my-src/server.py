from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  
import json
import os

app = Flask(__name__)
CORS(app)

usersPath="./static/backend/users.json"
def loadUsers():
    if os.path.exists(usersPath):
        with open(usersPath, "r") as f:
            return json.load(f)
    return []

def saveUsers(users):
    with open(usersPath,'w') as f:
        json.dump(users,f,indent=4)

allUsers=loadUsers()

@app.route('/login')
@app.route('/signup')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username=data.get('username')
    email = data.get('email')
    password = data.get('password')

    for user in allUsers:
        if (user["email"] == email or user["username"]) and user["password"] == password:
            return jsonify({"token": "placeholder-token-123"}), 200

    return jsonify({"error": "Invalid email or password"}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username=data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if email.count('@')!=1:
        return jsonify({"error": "Invalid email format, missing @"}), 401
    for user in allUsers:
        if user["email"] == email:
            return jsonify({"error": "An account with this email already exists"}), 409
        if user["username"] == username:
            return jsonify({"error": "Username is taken"}), 409
     
    new_user = {"username": username, "email": email, "password": password}
    allUsers.append(new_user)
    saveUsers(allUsers)
    return jsonify({"message": "User created successfully!"}), 201

if __name__ == '__main__':
    print("Available routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} -> {rule.endpoint}")
    app.run(debug=True)