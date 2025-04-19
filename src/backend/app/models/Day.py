from neomodel import DateTimeProperty
from .BaseModel import BaseModel


class Day(BaseModel):
    date = DateTimeProperty()
