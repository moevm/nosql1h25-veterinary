from neomodel import StructuredNode
from enum import Enum


class BaseModel(StructuredNode):
    """Базовый класс модели, от него наследуются все модели"""

    def to_dict(self):
        """Возвращает dict с данными об объекте"""
        data = {}

        # Получаем свойства (то, что описано через StringProperty и т.п.)
        for key in self.__all_properties__:
            value = getattr(self, key)

            if isinstance(value, Enum):
                value = value.value
            data[key] = value

        # Добавим ID (UUID в Neo4j)
        data['id'] = str(self.get_id_safety())

        return data

    def get_id_safety(self):
        try:
            return self.id
        except AttributeError:
            return None
