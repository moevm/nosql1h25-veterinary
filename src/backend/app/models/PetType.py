from neomodel import StringProperty
import BaseModel


class PetType(BaseModel):
    type_name = StringProperty(max_length=60)