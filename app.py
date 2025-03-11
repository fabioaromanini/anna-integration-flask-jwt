from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'xablau'  # Change this!
jwt = JWTManager(app)

# Example user data (replace with database)
users = {
    'poc': {'password': 'password123'}
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username') #get from request
    password = request.form.get('password') #get from request
    user = users.get(username)

    if user and user['password'] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

@app.route('/chat', methods=['POST'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200