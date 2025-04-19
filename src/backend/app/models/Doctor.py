from neomodel import StringProperty
from .User import User


class Doctor(User):
    experience = StringProperty(max_length=300)
    specialization = StringProperty(max_length=60)
