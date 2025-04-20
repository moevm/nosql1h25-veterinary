# Procedure.py

from neomodel import StringProperty, FloatProperty, BooleanProperty, RelationshipFrom, RelationshipTo
from .BaseModel import BaseModel

class Procedure(BaseModel):
    name = StringProperty(max_length=60)
    cost = FloatProperty()
    description = StringProperty(max_length=480)
    available = BooleanProperty()

    # Связи
    appointments = RelationshipFrom('Appointment', 'INCLUDES')  # Входит в приём
    pet_types = RelationshipFrom('PetType', 'PROVIDED_TO')  # Предоставляется типу питомца
    offices = RelationshipTo('Office', 'PROVIDES')  # Проводится в офисе
