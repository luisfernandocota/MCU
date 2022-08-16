from flask import jsonify, request, current_app, session

from datetime import datetime, timedelta
import jwt

from mcu import db


class Users(db.Document):
    username = db.StringField()
    email = db.EmailField()
    password = db.StringField()
    age = db.IntField()

    def to_json(self):
            return jsonify({
                '_id': str(self.pk),
                'username': self.username,
                'email': self.email,
                'age': self.age
            })
    
    @staticmethod
    def auth_user(username, password):
        from werkzeug.security import check_password_hash
        try:
            user = Users.objects.get(username=username)
            if check_password_hash(user.password, password):
                token = jwt.encode({
                    'user': request.json['username'],
                    'expiration': str(datetime.utcnow() + timedelta(seconds=120))
                }, current_app.config['SECRET_KEY'])
                session['username'] = user.username
                return jsonify({'token': token.decode('utf-8'), 'user':user.username})
            else:
                return jsonify({'message': 'Invalid username or password'})
        except Users.DoestNotExit:
            return jsonify({'message':'User does not exits'})