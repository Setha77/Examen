class Magasin:
    def __init__(self, typeMusique):
        self.typeMusique = typeMusique
        self.listeVinyle = []
        self.listeDVD = []

    # Méthode pour ajouter une musique dans la liste des vinyles
    def ajouter_musique_vinyle(self, musique):
        self.listeVinyle.append(musique)

    # Méthode pour ajouter une musique dans la liste des vinyles
    def ajouter_musique_dvd(self, musique):
        self.listeDVD.append(musique)
