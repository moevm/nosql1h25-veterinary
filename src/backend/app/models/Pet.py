from neomodel import StringProperty, DateProperty
import BaseModel


class Pet(BaseModel):
    name = StringProperty(max_length=60)
    breed = StringProperty(max_length=60)
    birthdate = DateProperty()
    gender = StringProperty()
    photo_url = StringProperty(max_length=120)