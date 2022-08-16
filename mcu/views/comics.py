
from flask import Blueprint, request
import json
import requests


comicsApp = Blueprint('comics', __name__)

ts=1
private_key = 'ea5a1e28d4a8538fdbb7a3075652ecb2751dff19'
public_key = '3b1f9fbd703b97760646feb9edec50ec'
hash = '45e26205f035f4fe7ab8d16f450733d8'



@comicsApp.route('/api/v1/comics', methods=['GET'])
def get_comics():
    comics = []
    
    if request.args.get('titleStartsWith'):
        parameter = '&titleStartsWith='+request.args.get('titleStartsWith')
    else:
        parameter = ''
    url = f'https://gateway.marvel.com:443/v1/public/comics?ts={ts}&apikey={public_key}&hash={hash}' + parameter
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        for i in data['data']['results']:
            id = i['id']
            title = i['title']
            on_sale_date = i['dates']
            images = i['thumbnail']['path']
            dic = {'id':id, 'title': title, 'images':images, 'onSaleDate':on_sale_date}
            comics.append(dic)
    return comics

@comicsApp.route('/api/v1/characters', methods=['GET', 'POST'])
@comicsApp.route('/api/v1/')
def get_characters():
    characters = []
    if request.args.get('nameStartsWith'):
        parameter = '&nameStartsWith='+request.args.get('nameStartsWith')
    else:
        parameter = ''
    url = f'https://gateway.marvel.com:443/v1/public/characters?ts={ts}&apikey={public_key}&hash={hash}' + parameter
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)

        for i in data['data']['results']:
            id = i['id']
            name = i['name']
            appearances = i['comics']['available']
            images = i['thumbnail']['path']
            dic = {'id':id, 'name': name, 'images':images, 'appearances':appearances}
            characters.append(dic)
    return characters