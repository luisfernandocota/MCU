from flask import Flask
from flask_mongoengine import MongoEngine
from flask_session import Session

db = MongoEngine()

def init_app():

    appFlask = Flask(__name__)
    appFlask.config['SECRET_KEY'] = '7287796dd4634627b4244629fa7b5f46'
    appFlask.config["MONGODB_DB"] = 'mcu'  
    appFlask.config["PRIVATE_KEY"] = 'ea5a1e28d4a8538fdbb7a3075652ecb2751dff19'
    appFlask.config["PUBLIC_KEY"] = '3b1f9fbd703b97760646feb9edec50ec'
    appFlask.config['HASH'] = '45e26205f035f4fe7ab8d16f450733d8'
    appFlask.config['TS'] = 1

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

    from .views.layaway import layawayApp
    appFlask.register_blueprint(layawayApp)

    return appFlask