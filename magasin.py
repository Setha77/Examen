class Magasin:
    def __init__(self, typeMusique):
        self.typeMusique = typeMusique
        self.listeVinyle = []
        self.listeDVD = []
    # Méthode pour connaître les informations
    def get_typeMusique(self):
        return self.typeMusique
    
    # Méthode pour ajouter une musique dans la liste des vinyles
    def ajouter_musique_vinyle(self, musique):
        self.listeVinyle.append(musique)

    # Méthode pour ajouter une musique dans la liste des DVD
    def ajouter_musique_dvd(self, musique):
        self.listeDVD.append(musique)

    # Méthode pour retirer une musique dans la liste des vinyles
    def retirer_vinyles(self, musique):
        if(musique in self.listeVinyle):
            self.listeVinyle.remove(musique)
            return True
        else:
            return False
    # Méthode pour retirer une musique dans la liste des DVD   
    def retirer_dvd(self, musique):
        if(musique in self.listeDVD):
            self.listeDVD.remove(musique)
            return True
        else:
            return False

