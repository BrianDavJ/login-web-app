from flask import Blueprint, render_template, request, jsonify
import json
import os



auth= Blueprint('auth', __name__)

usersPath="./appSrc/static/backend/users.json"
def loadUsers():
    if os.path.exists(usersPath):
        with open(usersPath, "r") as f:
            return json.load(f)
    return []

def saveUsers(users):
    with open(usersPath,'w') as f:
        json.dump(users,f,indent=4)

allUsers=loadUsers()

@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        print('no encontró')
        email = data.get('email')
        password = data.get('password')

        for user in allUsers:
            if (user["email"] == email or user["username"]==email) and user["password"] == password:
                return jsonify({"token": "placeholder-token-123"}), 200
        

        return jsonify({"error": "Invalid email or password"}), 401
    return render_template("index.html")


@auth.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        username=data.get('username')
        email = data.get('email')
        password = data.get('password')
        password2 = data.get('password2')
        if not password or len(password)==0:
            return jsonify({"error": "Password too short"}), 411
        if password != password2:
            return jsonify({"error":"Passwords don't match"}),401

        if email.count('@')!=1:
            return jsonify({"error": "Invalid email format"}), 401 
        for user in allUsers:
            if user["email"] == email:
                return jsonify({"error": "An account with this email already exists"}), 409
            if user["username"] == username:
                return jsonify({"error": "Username is taken"}), 409
        
        new_user = {"username": username, "email": email, "password": password}
        allUsers.append(new_user)
        saveUsers(allUsers)
        return jsonify({"message": "User created successfully!"}), 201

    return render_template("signUp.html")