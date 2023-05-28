from pydantic import BaseModel

class ModelMusique(BaseModel):
    titre: str
    nom_artiste: str
    immatriculation: str

