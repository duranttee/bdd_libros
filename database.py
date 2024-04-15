from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb://localhost:27017/'

def dbConnection():
    try:
        client = MongoClient(MONGO_URI)
        db = client["dbb_libros_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
