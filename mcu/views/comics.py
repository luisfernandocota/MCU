
from flask import Blueprint, request
import json

from mcu.models.comicsModel import Comics

comicsApp = Blueprint('comics', __name__)

@comicsApp.route('/api/v1/comics', methods=['GET'])
def get_comics():
    comics = Comics.get_comics(request)
    return comics
    
@comicsApp.route('/api/v1/characters', methods=['GET'])
@comicsApp.route('/api/v1/')
def get_characters():
    characters = Comics.get_characters(request)
    return characters
