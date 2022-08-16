from flask import Blueprint, jsonify, request, current_app
import json
import jwt
from functools import wraps

utilsApp = Blueprint('utilsApp', __name__)


@utilsApp.errorhandler(404)
def not_found(error=None):
    response = jsonify({
            'message' : 'Resource not found: ' + request.url,
            'status' : 404
        }
    )
    response.status_code = 404

    return response

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'})
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Invalid token'})
    return decorated
