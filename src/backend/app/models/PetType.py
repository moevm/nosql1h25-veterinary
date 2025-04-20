# PetType.py

from neomodel import StringProperty, RelationshipFrom, RelationshipTo
from .BaseModel import BaseModel


class PetType(BaseModel):
    type_name = StringProperty(max_length=60)

    # Связи
    pets = RelationshipFrom('app.models.Pet', 'BELONGS_TO')  # Тип имеет питомцев
    procedures = RelationshipTo('app.models.Procedure', 'PROVIDED_TO')  # Типу доступны процедуры