from neomodel import StringProperty, DateProperty
from .BaseModel import BaseModel


class Pet(BaseModel):
    name = StringProperty(max_length=60)
    breed = StringProperty(max_length=60)
    birthdate = DateProperty()
    gender = StringProperty()
    photo_url = StringProperty(max_length=120)