
from flask import Blueprint, jsonify, request, Response, session, url_for, redirect
from werkzeug.security import generate_password_hash

from mcu.core.utils import not_found
from mcu.models.usersModel import Users

usersApp = Blueprint('users', __name__)

@usersApp.route('/api/v1/users/register', methods=['POST'])
def register():
    #-- Receiving data
    try:
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        age = request.json['age']
        if username and email and age and password:
            try:
                user = Users.objects.get(username=username)
                return jsonify({'message': 'That username already exists!'})

            except Users.DoesNotExist:
                hash_password = generate_password_hash(password)

                user = Users(
                    username=username,
                    email= email,
                    age=age,
                    password=hash_password
                )
                user.save()
                session['username'] = username
                return redirect(url_for('users.login'))
        else:

            return not_found()
    except KeyError as e:
        return jsonify({'message': 'Faltan los campos: ' + str(e.args)})

@usersApp.route('/api/v1/users/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']

        if 'username' in session:
            return jsonify({'message': 'You are logged in as '+ session['username']})
        else:
            return  Users.auth_user(username, password)
    else:
        if 'username' in session:
            return jsonify({'message': 'You are logged in as '+ session['username']})
        else:
            return jsonify({'message': 'There is no sessions'})


@usersApp.route('/api/v1/users', methods=['GET'])
def get_users():
    users = Users.objects.all()
    response = users.to_json()

    return Response(response, mimetype='application/json')

@usersApp.route('/api/v1/users/session', methods=['GET'])
def get_user():
    if 'username' in session:
        user = Users.objects.filter(username=session['username'])
        if user:
            response = user.to_json()
            return Response(response, mimetype='application/json')
        else:
            response = jsonify({'message': 'There no was object with this id, should be deleted'})
            return response
    else:
        return jsonify({'message':'Theres no sessions'})

@usersApp.route('/api/v1/users/logout', methods=['GET'])
def logout():
    if session:
        session.pop('username', None)
    return redirect(url_for('users.login'))

@usersApp.route('/api/v1/users/<id>', methods=['PUT'])
def update_user(id):
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if username and email and password:
        hash_password = generate_password_hash(password)
        user = Users.objects(pk=id).update_one(set__username=username, set__email=email, set__password=hash_password)
        response = jsonify({'message': 'User %s was updated' %(username)})
    else:
        response = jsonify({'message': 'There no was object with this id'})

    return response


@usersApp.route('/api/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
    Users.objects(pk=id).delete()
    response = jsonify({'message': 'User %s was deleted' %(id) })
    return response

