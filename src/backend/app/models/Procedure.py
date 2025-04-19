from neomodel import StringProperty, FloatProperty, BooleanProperty
from .BaseModel import BaseModel


class Procedure(BaseModel):
    name = StringProperty(max_length=60)
    cost = FloatProperty()
    description = StringProperty(max_length=480)
    available = BooleanProperty()
