from pydantic import BaseModel, validator, root_validator

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
    
    @validator('immatriculation')
    def verifier_slash(cls, value):
        """Verifier que l'immatriculation possède ses 3 slashs au bonnes emplacements"""
        slash1 = value[2]
        slash2 = value[6]
        slash3 = value[10]

        if (slash1 != "/") and (slash2 != "/") and (slash3 != "/"):
            raise ValueError("L'immatriculation ne possède pas les slashs")
        return value
    
    @validator('immatriculation')
    def verifier_style(cls, value):
        """Verifier que l'immatriculation possède ses 3 styles de musiques listés"""
        list_styles = ["POP", "RAP", "RNB"]
        style = value[7:10]
        resultat = isinstance(style, str)
        if resultat != 1 and style not in list_styles:
            raise ValueError("L'immatriculation ne possède le style que vous avez mis ou erreur ce que vous aves mis n'est pas une chaîne de caractère")
        return value
    
    @validator('immatriculation')
    def verifier_six(cls, value):
        """Verifier que l'immatriculation ne possède pas de six dans les 4 derniers"""
        premier = value[11]
        deuxieme = value[12]
        troisieme = value[13]
        quatrieme = value[14]

        if premier == 6 or deuxieme == 6 or troisieme == 6 or quatrieme == 6:
            raise ValueError("L'immatriculation possède des 6")
        return value
    
    @root_validator
    def verifier_initial(cls, value):
        """Verifier que l'immatriculation possède l'initial de l'artiste"""
        initial_temp = value.get("immatriculation")
        initial = initial_temp[0:2]
        initial_temp2 = value.get("nom_artiste")
        initial_artiste = initial_temp2[0:2]

        if initial != initial_artiste:
            raise ValueError("L'initial n'est pas bon")
        return value
        
