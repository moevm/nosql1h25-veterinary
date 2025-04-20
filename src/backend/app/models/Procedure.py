# Procedure.py

from neomodel import StringProperty, FloatProperty, BooleanProperty, RelationshipFrom, RelationshipTo
from .BaseModel import BaseModel

class Procedure(BaseModel):
    name = StringProperty(max_length=60)
    cost = FloatProperty()
    description = StringProperty(max_length=480)
    available = BooleanProperty()

    # Связи
    appointments = RelationshipFrom('app.models.Appointment', 'INCLUDES')  # Входит в приём
    pet_types = RelationshipFrom('app.models.PetType', 'PROVIDED_TO')  # Предоставляется типу питомца
    offices = RelationshipTo('app.models.Office', 'PROVIDES')  # Проводится в офисе