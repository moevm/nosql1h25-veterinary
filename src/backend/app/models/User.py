from neomodel import StringProperty, DateProperty
from .BaseModel import BaseModel


class User(BaseModel):
    second_name = StringProperty(max_length=120)
    first_name = StringProperty(max_length=60)
    last_name = StringProperty(max_length=60)
    login = StringProperty(max_length=60)
    password_hash = StringProperty(max_length=120)
    birth_date = DateProperty()
    email = StringProperty()
    gender = StringProperty()
    phone_number = StringProperty()
    role = StringProperty(choices=[('doctor', 'Doctor'), ('admin', 'Admin'), ('client', 'Client'), ('user', 'User')], default='client')

