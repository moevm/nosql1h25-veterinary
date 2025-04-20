# Office.py

from neomodel import StringProperty, RelationshipFrom, RelationshipTo
from .BaseModel import BaseModel

class Office(BaseModel):
    name = StringProperty(max_length=60)
    address = StringProperty(max_length=120)
    email = StringProperty()
    phone_number = StringProperty()
    opening_hours = StringProperty(max_length=60)
    meta = StringProperty(max_length=300)

    # Связи
    doctors = RelationshipFrom('Doctor', 'WORKS_IN')            # В офисе работают врачи
    appointments = RelationshipFrom('Appointment', 'PROVIDES')  # В офисе проходят приёмы
    procedures = RelationshipFrom('Procedure', 'PROVIDES')      # В офисе предоставляются процедуры
