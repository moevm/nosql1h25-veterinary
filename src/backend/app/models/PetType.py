from neomodel import StringProperty
from .BaseModel import BaseModel


class PetType(BaseModel):
    type_name = StringProperty(max_length=60)