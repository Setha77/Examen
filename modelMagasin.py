from pydantic import BaseModel, validator
from typing import List
from modelMusique import ModelMusique

class ModelMagasin(BaseModel):
    typeMusique: str
    liste_Vinyle: List[ModelMusique]
    liste_DVD: List[ModelMusique]

    # Récupère les musiques dans la liste Vinyle
    def get_Vinyle(self):
        return self.liste_Vinyle
    
    # Récupère les musiques dans la liste DVD
    def get_DVD(self):
        return self.liste_DVD
    
    # Verifier le type de musique ajouté
    def verifier_typeMusique(self, musique: ModelMusique):
        styleMusique = musique.immatriculation[7:10]
        if styleMusique != self.typeMusique:
            return False
        else:
            return True
        
    # Ajouter des musiques dans la liste Vinyle
    def ajouter_Vinyle(self, musique: ModelMusique):
        compatible = self.verifier_typeMusique(musique)
        if compatible == 1:
            self.liste_Vinyle.append(musique)

    # Ajouter des musiques dans la liste DVD
    def ajouter_DVD(self, musique: ModelMusique):
        compatible = self.verifier_typeMusique(musique)
        if compatible == 1:
            self.liste_DVD.append(musique)
    
    # Enlever des musiques dans la liste Vinyle
    def retirer_Vinyle(self, musique: ModelMusique):
        if musique in self.liste_Vinyle:
            self.liste_Vinyle.remove(musique)

    # Enlever des musiques dans la liste Vinyle
    def retirer_DVD(self, musique: ModelMusique):
        if musique in self.liste_DVD:
            self.liste_DVD.remove(musique)

