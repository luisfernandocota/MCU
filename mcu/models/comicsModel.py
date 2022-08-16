from flask import current_app, jsonify
import json
import requests


from mcu import db


class Comics(db.Document):
    user_id = db.ReferenceField('Users')
    username = db.StringField()
    comic_id = db.StringField()
    comic_name = db.StringField()

    def to_json(self):
            return jsonify({
                '_id': str(self.pk),
                'user_id': self.user_id,
                'username': self.username,
                'comic_id': self.comic_id,
                'comic_name': self.comic_name
            })

    @staticmethod
    def get_comics(request):
        comics = []
        
        if request.args.get('titleStartsWith'):
            parameter = '&titleStartsWith='+request.args.get('titleStartsWith')
        else:
            parameter = ''
        url = f'https://gateway.marvel.com:443/v1/public/comics?ts={current_app.config["TS"]}&apikey={current_app.config["PUBLIC_KEY"]}&hash={current_app.config["HASH"]}' + parameter
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

    @staticmethod
    def get_comic_id(id):
        comics = []
        
        url = f'https://gateway.marvel.com:443/v1/public/comics/{id}?ts={current_app.config["TS"]}&apikey={current_app.config["PUBLIC_KEY"]}&hash={current_app.config["HASH"]}'
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

    @staticmethod
    def get_characters(request):
        characters = []
        if request.args.get('nameStartsWith'):
            parameter = '&nameStartsWith='+request.args.get('nameStartsWith')
        else:
            parameter = ''
        url = f'https://gateway.marvel.com:443/v1/public/characters?ts={current_app.config["TS"]}&apikey={current_app.config["PUBLIC_KEY"]}&hash={current_app.config["HASH"]}' + parameter
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