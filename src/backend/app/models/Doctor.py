# Doctor.py

from neomodel import StringProperty, RelationshipFrom, RelationshipTo
from .User import User

class Doctor(User):
    experience = StringProperty(max_length=300)
    specialization = StringProperty(max_length=60)

    # Связи
    appointments = RelationshipTo('app.models.Appointment', 'CONDUCTS')  # Врач проводит приёмы
    offices = RelationshipTo('app.models.Office', 'WORKS_IN')              # Врач работает в офисе
    available_days = RelationshipTo('app.models.Day', 'AVAILABLE_AT')      # Врач доступен в определённые дни/слоты