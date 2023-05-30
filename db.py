import pymongo
from pymongo import MongoClient

def database():
  client = "mongodb+srv://sethahong77:9ONsYp6oH05vpR7m@cluster0.0lcafi0.mongodb.net/?retryWrites=true&w=majority"
  db = client.Musique
  collection = client.Musique.MagasinMusique
  return db
