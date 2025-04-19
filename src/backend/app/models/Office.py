from neomodel import StringProperty
import BaseModel


class Office(BaseModel):
    name = StringProperty(max_length=60)
    address = StringProperty(max_length=120)
    email = StringProperty()
    phone_number = StringProperty()
    opening_hours = StringProperty(max_length=60)
    meta = StringProperty(max_length=300)
