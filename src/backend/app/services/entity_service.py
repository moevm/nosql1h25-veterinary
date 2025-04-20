from app.db.neo4j_controller import Neo4jRepository
from app.models import Pet, Client, Doctor, Appointment, Procedure, Day, Admin, Office, PetType, User  # импорт всех моделей


ENTITY_CLASS_MAP = {
    "admin": Admin,
    "appointment": Appointment,
    "client": Client,
    "day": Day,
    "doctor": Doctor,
    "office": Office,
    "pet": Pet,
    "pet_type": PetType,
    "procedure": Procedure,
    "user": User
}


def filter_entities(entity_name: str, filters: dict):
    entity_name = entity_name.lower()
    print(entity_name)
    print(filters)
    if entity_name not in ENTITY_CLASS_MAP:
        raise ValueError(f"Unknown entity: {entity_name}")

    model_cls = ENTITY_CLASS_MAP[entity_name]
    repo = Neo4jRepository(model_cls)
    return repo.filter(**filters)
