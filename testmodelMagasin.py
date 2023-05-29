from mock import Mock
from modelMagasin import ModelMagasin, ModelMagasinException

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

# Test si retirer une musique inexistante dans Vinyle 
def test_remove_musiqueVinyleFailure():
    musique = Mock()
    other_musique = Mock()
    modelMag = ModelMagasin()
    modelMag.liste_Vinyle = [musique]

    try:
        modelMag.retirer_Vinyle(other_musique)
    except ModelMagasinException:
        pass
    else:
        raise Exception("expected Exception was not raised")
    
# Test si retirer une musique inexistante dans DVD
def test_remove_musiqueDVDFailure():
    musique = Mock()
    other_musique = Mock()
    modelMag = ModelMagasin()
    modelMag.liste_Vinyle = [musique]

    try:
        modelMag.retirer_DVD(other_musique)
    except ModelMagasinException:
        pass
    else:
        raise Exception("expected Exception was not raised")