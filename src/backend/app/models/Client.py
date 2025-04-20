from .User import User
from neomodel import RelationshipTo

class Client(User):
    # Связи
    pets = RelationshipTo('app.models.Pet', 'OWN')  # Клиент владеет питомцами
    appointments = RelationshipTo('app.models.Appointment', 'REGISTERED_ON')  # Записан на приём
