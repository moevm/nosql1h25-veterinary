# Day.py

from neomodel import DateTimeProperty, RelationshipFrom
from .BaseModel import BaseModel

class Day(BaseModel):
    date = DateTimeProperty()

    # Связи
    appointments = RelationshipFrom('app.models.Appointment', 'IS_SCHEDULED_ON')  # На этот день назначены приёмы
    doctors = RelationshipFrom('app.models.Doctor', 'AVAILABLE_AT')               # В этот день доступны врачи