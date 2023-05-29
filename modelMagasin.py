from pydantic import BaseModel, validator
from typing import List
from modelMusique import ModelMusique

class ModelMagasin(BaseModel):
    typeMusique: str
    liste_Vinyle: List[ModelMusique] = []
    liste_DVD: List[ModelMusique] = []