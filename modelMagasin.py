from pydantic import BaseModel, validator
from typing import List
from modelMusique import ModelMusique

class ModelMagasin(BaseModel):
    typeMusique: str
    liste_Vinyle: list[ModelMusique] = []
    liste_DVD: list[ModelMusique] = []

    @validator("liste_Vinyle")
    def ajouter_Vinyle(cls, value):
        