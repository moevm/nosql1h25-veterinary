from .User import User
from neomodel import RelationshipTo


class Client(User):
    # Связи
    pets = RelationshipTo('Pet', 'OWN')  # Клиент владеет питомцами
    appointments = RelationshipTo('Appointment', 'REGISTERED_ON')  # Записан на приём