import unittest
from datetime import datetime
from ...models.Appointment import Appointment, AppointmentStatus


class TestAppointment(unittest.TestCase):

    def setUp(self):
        """Предварительная настройка для каждого теста."""
        self.appointment = Appointment(
            date=datetime(2025, 5, 1, 10, 0),
            reason="Checkup",
            comment="Everything looks good",
            diagnosis="Healthy",
            recommend="No action needed",
            file_urls=["file1.jpg", "file2.jpg"]
        )

    def test_status_default_value(self):
        """Проверка, что статус по умолчанию равен 'ожидает подтверждения'."""
        self.assertEqual(self.appointment.status, AppointmentStatus.PENDING.value)

    def test_invalid_status(self):
        """Проверка установки недопустимого значения статуса."""
        with self.assertRaises(ValueError):
            self.appointment.status = "InvalidStatus"

    def test_valid_status(self):
        """Проверка установки недопустимого значения статуса."""
        self.appointment.status = AppointmentStatus.PENDING
        self.assertEqual(self.appointment.status, AppointmentStatus.COMPLETED)
