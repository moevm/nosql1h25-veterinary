from neomodel import DateTimeProperty
import BaseModel


class Day(BaseModel):
    date = DateTimeProperty()
