from pymongo import MongoClient

"""
def database():
    client = MongoClient("mongodb+srv://sethahong77:9ONsYp6oH05vpR7m@cluster0.0lcafi0.mongodb.net/")
    db = client.Musique
    return db
"""

client = MongoClient("mongodb+srv://sethahong77:caca@cluster0.0lcafi0.mongodb.net/")
database = "Musique"
music = "music"
shop = "MagasinMusique"
