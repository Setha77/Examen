from pymongo import MongoClient

class Seed:
    def __init__(self):
        host = "mongodb+srv://sethahong77:9ONsYp6oH05vpR7m@cluster0.0lcafi0.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(host=f"{host}")
        self.__db = client.Musique

    