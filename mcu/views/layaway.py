
import json
from flask import Blueprint, jsonify, request, Response, session
from ..models.comicsModel import Comics

from mcu.models.usersModel import Users

layawayApp = Blueprint('layaway', __name__)

@layawayApp.route('/api/v1/addToLayaway', methods=['POST'])
def addToLayaway():
    if 'username' in session:
        try:
            comic_id = request.json['comic_id']
            username = request.json['username']
            comic = Comics.get_comic_id(comic_id)
            user = Users.objects.get(username=username)

            if comic:
                Comics.objects(user_id=user.pk, username=user.username, comic_id=str(comic[0]['id']), comic_name=comic[0]['title'])\
                                .update(user_id=user.pk, username=user.username, comic_id=str(comic[0]['id']), comic_name=comic[0]['title'], upsert=True)

                return jsonify({'message': 'Correctly bookmarked comic ' + comic[0]['title']})
            else:
                return jsonify({'message': 'The comic does not exits'})
        except Users.DoesNotExist:
            return jsonify({'message': 'The user does not exist'})
    else:
        return jsonify({'message': 'Only registered users can access'})

@layawayApp.route('/api/v1/getLayawayList', methods=['GET'])
def getLayawayList():
    if 'username' in session:
        user = Users.objects.get(username=session['username'])
        comics = Comics.objects.filter(user_id=user.pk)
        response = comics.to_json()

        return Response(response, mimetype='application/json')
    else:
        return jsonify({'message': 'Only registered users can access'})