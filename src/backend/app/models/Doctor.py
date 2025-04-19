from neomodel import StringProperty, DateProperty
import BaseModel


class Doctor(BaseModel):
    second_name = StringProperty(max_length=120)
    first_name = StringProperty(max_length=60)
    last_name = StringProperty(max_length=60)
    login = StringProperty(max_length=60)
    password_hash = StringProperty(max_length=120)
    birthday = DateProperty()
    email = StringProperty()
    gender = StringProperty()
    phone_number = StringProperty()
    experience = StringProperty(max_length=300)
    specialization = StringProperty(max_length=60)