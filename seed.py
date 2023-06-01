from fastapi import FastAPI
from pymongo import MongoClient
from modelMusique import ModelMusique
from modelMagasin import ModelMagasin, ModelMagasinException
from bson.objectid import ObjectId
from db import *

app = FastAPI()
connexion = MongoClient("mongodb+srv://sethahong77:caca@cluster0.0lcafi0.mongodb.net/")
BaseDonnee = client[database]
Music = BaseDonnee[music]
Magasin = BaseDonnee[shop]

musiques = [
  {"titre": "My Heart Will Go On", "nom_artiste": "DION Celine", "immatriculation":"DI/250/POP/1234"},
  {"titre": "Shape of You", "nom_artiste": "SHEERAN Ed", "immatriculation":"SH/250/POP/1235"}
]

magasins = [
    {"typeMusique":"POP","liste_Vinyle":[],"liste_DVD":[]},
    {"typeMusique":"RAP","liste_Vinyle":[],"liste_DVD":[]}
]
# Ajoute de la musique dans base de données music
Music.insert_many(musiques)
Magasin.insert_many(magasins)
