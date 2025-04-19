from neomodel import StringProperty, DateTimeProperty, ArrayProperty
from enum import Enum
from .BaseModel import BaseModel


class AppointmentStatus(str, Enum):
    """Все доступные статусы приема"""
    PENDING = 'ожидает подтверждения'
    CONFIRMED = 'подтвержден'
    CANCELED = 'отменен'
    COMPLETED = 'проведен'


class Appointment(BaseModel):
    date = DateTimeProperty()
    _status = StringProperty(
        choices=[(status.value, status.name) for status in AppointmentStatus],
        default=AppointmentStatus.PENDING.value
    )
    reason = StringProperty(max_length=480)
    comment = StringProperty(max_length=960)
    diagnosis = StringProperty(max_length=300)
    recommend = StringProperty(max_length=480)
    file_urls = ArrayProperty(StringProperty(max_length=120))

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        """Сеттер для статуса, проверяет, что статус является одним из перечисленных в AppointmentStatus"""
        if value not in [status.value for status in AppointmentStatus]:
            raise ValueError(f"Invalid status: {value}")
        self._status = value
