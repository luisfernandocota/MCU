from flask import Flask
from flask_mongoengine import MongoEngine
from flask_session import Session

db = MongoEngine()

def init_app():

    appFlask = Flask(__name__)
    appFlask.config['SECRET_KEY'] = '7287796dd4634627b4244629fa7b5f46'
    appFlask.config["MONGODB_DB"] = 'mcu'        
    db.connect(
        'mcu',
        username='mcu-user',
        password='ingfer96',
        host='mongodb+srv://mcu-user:ingfer96@mongodb-mcu.bu3zhqj.mongodb.net/?retryWrites=true&w=majority',
        port=27017
    )

    appFlask.config["SESSION_PERMANENT"] = False
    appFlask.config["SESSION_TYPE"] = "filesystem"
    Session(appFlask)

    #-- Route
    from .views.users import usersApp
    appFlask.register_blueprint(usersApp)

    from .views.comics import comicsApp
    appFlask.register_blueprint(comicsApp)

    return appFlask