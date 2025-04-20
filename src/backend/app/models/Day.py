# Day.py

from neomodel import DateTimeProperty, RelationshipFrom
from .BaseModel import BaseModel

class Day(BaseModel):
    date = DateTimeProperty()

    # Связи
    appointments = RelationshipFrom('Appointment', 'IS_SCHEDULED_ON')  # На этот день назначены приёмы
    doctors = RelationshipFrom('Doctor', 'AVAILABLE_AT')               # В этот день доступны врачи
