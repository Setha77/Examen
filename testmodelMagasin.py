import unittest
from mock import Mock
from modelMagasin import ModelMagasin, ModelMagasinException

class TestModelMagasin(unittest.TestCase):
    def setUp(self):
        musique = Mock()
        self.magasin = ModelMagasin(
            typeMusique = "POP",
            liste_Vinyle = [],
            liste_DVD = [], 
        )

    # Test si ajouter musique dans Vinyle fonctionne
    def test_add_musiqueVinyle(self):
        musique = Mock()
        #modelMag = ModelMagasin()
        self.magasin.ajouter_Vinyle(musique)
        self.assertEqual(self.magasin.liste_Vinyle, [musique])
        #assert self.magasin.liste_Vinyle == [musique]
    
    # Test si ajouter musique dans DVD fonctionne
    def test_add_musiqueDVD(self):
        musique = Mock()
        #modelMag = ModelMagasin()
        self.magasin.ajouter_DVD(musique)
        self.assertEqual(self.magasin.liste_DVD, [musique])
        #assert self.magasin.liste_DVD == [musique]
    
    # Test si retirer une musique dans Vinyle fonctionne
    def test_remove_musiqueVinyle(self):
        musique = Mock()
        #modelMag = ModelMagasin()
        self.magasin.liste_Vinyle = [musique]
        self.magasin.retirer_Vinyle(musique)

        assert self.magasin.liste_Vinyle == []
    
    # Test si retirer une musique dans DVD fonctionne
    def test_remove_musiqueDVD(self):
        musique = Mock()
        #modelMag = ModelMagasin()
        self.magasin.liste_DVD = [musique]
        self.magasin.retirer_DVD(musique)

        assert self.magasin.liste_DVD == []

    # Test si retirer une musique inexistante dans Vinyle 
    def test_remove_musiqueVinyleFailure(self):
        musique = Mock()
        other_musique = Mock()
        #modelMag = ModelMagasin()
        self.magasin.liste_Vinyle = [musique]

        try:
            self.magasin.retirer_Vinyle(other_musique)
        except ModelMagasinException:
            pass
        else:
            raise Exception("expected Exception was not raised")
        
    # Test si retirer une musique inexistante dans DVD
    def test_remove_musiqueDVDFailure(self):
        musique = Mock()
        other_musique = Mock()
        #modelMag = ModelMagasin()
        self.magasin.liste_Vinyle = [musique]

        try:
            self.magasin.retirer_DVD(other_musique)
        except ModelMagasinException:
            pass
        else:
            raise Exception("expected Exception was not raised")

if __name__ == '__main__':
    unittest.main()