from neomodel import StructuredNode, UniqueIdProperty, db, RelationshipFrom, RelationshipTo
from enum import Enum
from datetime import date, datetime


class BaseModel(StructuredNode):
    """Базовый класс модели, от него наследуются все модели"""
    uid = UniqueIdProperty()

    @staticmethod
    def serialize_value(value):
        if isinstance(value, Enum):
            return value.value
        if isinstance(value, (datetime, date)):
            return value.isoformat()
        return value

    def to_dict(self):
        """Возвращает dict с данными об объекте"""
        data = {}

        # Получаем свойства (то, что описано через StringProperty и т.п.)
        for field, prop in self.__properties__.items():
            value = getattr(self, field)

            # Сериализация значений
            if isinstance(value, Enum):
                value = value.value
            data[field] = self.serialize_value(value)

        # Добавим ID (UUID в Neo4j)
        data['id'] = str(self.get_id_safety())
        return data

    def get_id_safety(self):
        try:
            return self.uid
        except AttributeError:
            return None

    def get_relationships(self):
        related_objects = {}
        for name, attr in self.__class__.__dict__.items():
            if isinstance(attr, (RelationshipFrom, RelationshipTo)):
                related = getattr(self, name).all()
                related_objects[name] = [obj.to_dict() for obj in related]
        return related_objects
