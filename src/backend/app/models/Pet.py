# Pet.py

from neomodel import StringProperty, DateProperty, RelationshipFrom, RelationshipTo
from .BaseModel import BaseModel

class Pet(BaseModel):
    name = StringProperty(max_length=60)
    breed = StringProperty(max_length=60)
    birthdate = DateProperty()
    gender = StringProperty(max_length=10)
    photo_url = StringProperty(max_length=120)

    # Связи
    owner = RelationshipFrom('Client', 'OWN')  # Питомец принадлежит клиенту
    pet_type = RelationshipTo('PetType', 'BELONGS_TO')  # Принадлежит типу
    appointments = RelationshipTo('Appointment', 'REGISTERED_ON')  # Записан на приём
