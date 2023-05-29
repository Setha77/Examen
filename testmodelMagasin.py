from mock import Mock
from modelMagasin import ModelMagasin
from modelMusique import ModelMusique

# Test si ajouter musique dans Vinyle fonctionne
def test_add_musiqueVinyle():
    musique = Mock()
    modelMag = ModelMagasin()
    modelMag.ajouter_Vinyle(musique)

    assert modelMag.liste_Vinyle == [musique]

# Test si ajouter musique dans DVD fonctionne
def test_add_musiqueDVD():
    musique = Mock()
    modelMag = ModelMagasin()
    modelMag.ajouter_DVD(musique)

    assert modelMag.liste_DVD == [musique]

# Test si retirer une musique dans Vinyle fonctionne
def test_remove_musiqueVinyle():
    musique = Mock()
    modelMag = ModelMagasin()
    modelMag.liste_Vinyle = [musique]
    modelMag.retirer_Vinyle(musique)

    assert modelMag.liste_Vinyle == []

# Test si retirer une musique dans DVD fonctionne
def test_remove_musiqueDVD():
    musique = Mock()
    modelMag = ModelMagasin()
    modelMag.liste_DVD = [musique]
    modelMag.retirer_DVD(musique)

    assert modelMag.liste_DVD == []

