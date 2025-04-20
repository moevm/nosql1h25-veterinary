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
    doctors = RelationshipFrom('app.models.Doctor', 'WORKS_IN')            # В офисе работают врачи
    appointments = RelationshipFrom('app.models.Appointment', 'PROVIDES')  # В офисе проходят приёмы
    procedures = RelationshipFrom('app.models.Procedure', 'PROVIDES')      # В офисе предоставляются процедуры
