from neomodel import db
from datetime import datetime
from app.models.Appointment import Appointment, AppointmentStatus


class Neo4jRepository:
    """
    Универсальный репозиторий для работы с сущностями neomodel.
    """

    def __init__(self, model_cls):
        self.model_cls = model_cls  # Например, Pet, Client, Doctor и т.д.

    def create(self, **kwargs):
        """
        Создать новую сущность.
        Пример: repo.create(name="Барсик", breed="Сибирский")
        """
        for key, value in kwargs.items():
            if key == "birthdate" or key == "birth_date":
                try:
                    kwargs[key] = datetime.strptime(value, "%Y-%m-%d").date()
                except ValueError:
                    # Обработка ошибки, если формат даты неверный
                    print(f"Invalid date format for '{key}': {value}.  Expected format: YYYY-MM-DD")
                    # Можно выбросить исключение или присвоить значение по умолчанию
                    # raise ValueError(f"Invalid date format for '{key}': {value}")
                    kwargs[key] = None  # Или какое-то значение по умолчанию
            # elif key == 'date':
            #     try:
            #         # Преобразуем ISO-строку вида "2025-05-20T14:30" в datetime
            #         kwargs[key] = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M")
            #     except ValueError:
            #         # Если парсинг не удался — можно логировать или выбросить исключение
            #         raise ValueError(f"Invalid datetime format for field '{key}': {kwargs[key]}")

            # if isinstance(self.model_cls, Appointment) and 'status' in kwargs:
            #     status_value = kwargs['status']
            #     valid_statuses = {s.value: s for s in AppointmentStatus}
            #     if status_value in valid_statuses:
            #         kwargs['status'] = valid_statuses[status_value]
            #     else:
            #         raise ValueError(f"Invalid status value for Appointment: {status_value}")

        instance = self.model_cls(**kwargs)
        instance.save()
        return instance

    def get_by_id(self, node_id):
        """
        Получить сущность по id (uid).
        """
        try:
            return self.model_cls.nodes.get(uid=node_id)
        except self.model_cls.DoesNotExist:
            return None

    def update(self, node_id, **kwargs):
        """
        Обновить сущность по id.
        """
        instance = self.get_by_id(node_id)
        if not instance:
            return None
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, node_id):
        """
        Удалить сущность по id.
        """
        instance = self.get_by_id(node_id)
        if instance:
            instance.delete()
            return True
        return False

    def all(self):
        """
        Получить список всех сущностей данной модели.
        """
        return list(self.model_cls.nodes)

    def filter(self, **kwargs):
        """
        Фильтрация по полям модели с поддержкой регистронезависимого поиска по кириллице.
        Пример: repo.filter(name__icontains="барс", gender="male")
        """
        # Сначала обрабатываем обычные фильтры и icontains отдельно
        cypher_where = []
        params = {}

        for key, value in kwargs.items():
            print(f"key: {key}, value: {value}")
            # if key.startswith('date'):
            #     cypher_where.append(f"n.date = datetime(${value})")
            #     params[key] = value  # строка в ISO формате, например: "2025-05-20T14:30:00"
            if key.endswith('__start'):
                field = key[:-7]
                cypher_where.append(f"n.{field} >= ${key}")
                params[key] = value
            elif key.endswith('__end'):
                field = key[:-5]
                cypher_where.append(f"n.{field} <= ${key}")
                params[key] = value
            elif key.endswith('__icontains'):
                field = key[:-11]
                # (?iu) — флаги: i (ignore case), u (unicode)
                pattern = f"(?iu).*{value}.*"
                cypher_where.append(f"n.{field} =~ ${field}_pattern")
                params[f"{field}_pattern"] = pattern
            else:
                cypher_where.append(f"n.{key} = ${key}")
                params[key] = value

        label = self.model_cls.__label__
        where_clause = " AND ".join(cypher_where) if cypher_where else "1=1"
        query = f"MATCH (n:{label}) WHERE {where_clause} RETURN n"

        results, meta = db.cypher_query(query, params)
        return [self.model_cls.inflate(row[0]) for row in results]
