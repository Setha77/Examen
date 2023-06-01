from fastapi import FastAPI, HTTPException
from db import *
from modelMusique import ModelMusique
"""
app = FastAPI()

@app.get("/musique")
def fetch_musique():
    db = database()
    musics = db["Musique"].find()
    res = []
    
    for music in musics:
        data = {
            "titre": music["titre"],
            "nom_artiste": music["nom_artiste"],
            "immatriculation": music["immatriculation"]
        }
        res.append(data)
    
    return res

@app.post("/musique/")
def create_music(music : ModelMusique):
    db = database()
    if db["Musique"].find_one({"immatriculation": music.immatriculation}) is not None:
        raise HTTPException(
            status_code=409, detail="Registration is already registred"
        )
    
    db["Musique"].insert_one(music.dict())
    return music.dict()


client = MongoClient(connexion)
Music = client[db]
chanson = Music[table]

@app.get("/musique")
def get_musique():
    res = []
    for music in chanson:
        res.append(ModelMusique(**music))
    return res

@app.post("/musique")
def create_music(music: ModelMusique):
    result = chanson.insert_one(dict(music))
    return {"_id": str(result.inserted_id)} | dict(music)
"""
