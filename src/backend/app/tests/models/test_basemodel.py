import unittest
from ...models.BaseModel import BaseModel
from ...models.Appointment import AppointmentStatus


class TestBaseModel(unittest.TestCase):
    def test_to_dict(self):
        """Проверка работы to_dict"""
        base_model = BaseModel()
        base_model.__all_properties__ = ['name', 'age', 'species', 'status']
        base_model.name = "Rex"
        base_model.age = 5
        base_model.species = "Dog"
        base_model.status = AppointmentStatus.PENDING
        base_model_dict = base_model.to_dict()
        base_model_dict.pop('id')

        data = {
            'name': 'Rex',
            'age': 5,
            'species': 'Dog',
            'status': 'ожидает подтверждения'
        }
        self.assertDictEqual(base_model_dict, data, "dicts are not equals")
