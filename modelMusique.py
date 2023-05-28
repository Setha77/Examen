from pydantic import BaseModel, validator

class ModelMusique(BaseModel):
    titre: str
    nom_artiste: str
    immatriculation: str

    @validator('immatriculation')
    def verifier_taille(cls, value):
        """Verifier si la taille de l'immatriculation de 15"""
        if len(value) != 15:
            raise ValueError("La taille n'est pas égal à 15")
        return value
    
    @validator('immatriculation')
    def verifier_string(cls, value):
         """Verifier que l'immatriculation soit une chaîne de caractère"""
         resultat = isinstance(value, str)
         if resultat != 1:
             raise ValueError("L'immatriculation n'est pas une chaîne de caractère")
         return value
    
    

