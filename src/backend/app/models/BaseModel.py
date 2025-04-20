from neomodel import StructuredNode, UniqueIdProperty
from enum import Enum


class BaseModel(StructuredNode):
    """Базовый класс модели, от него наследуются все модели"""
    uid = UniqueIdProperty()

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
        for key in self.__all_properties__:
            if isinstance(key, str):
                value = getattr(self, key)

                if isinstance(value, Enum):
                    value = value.value
                data[key] = self.serialize_value(value)

        # Добавим ID (UUID в Neo4j)
        data['id'] = str(self.get_id_safety())

        return data

    def get_id_safety(self):
        try:
            return self.uid
        except AttributeError:
            return None
