from app.db.neo4j_controller import Neo4jRepository
from app.models.Pet import Pet
from app.models.Client import Client
from app.models.Doctor import Doctor
from app.models.Appointment import Appointment
from app.models.Procedure import Procedure
from app.models.Day import Day
from app.models.Admin import Admin
from app.models.Office import Office
from app.models.PetType import PetType
from app.models.User import User


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
    if entity_name not in ENTITY_CLASS_MAP:
        raise ValueError(f"Unknown entity: {entity_name}")

    model_cls = ENTITY_CLASS_MAP[entity_name]
    repo = Neo4jRepository(model_cls)
    return repo.filter(**filters)

def create_entity(entity_name: str, data: dict):
    entity_name = entity_name.lower()
    print(entity_name)
    print(data)
    if entity_name not in ENTITY_CLASS_MAP:
        raise ValueError(f"Unknown entity: {entity_name}")

    model_cls = ENTITY_CLASS_MAP[entity_name]
    repo = Neo4jRepository(model_cls)
    return repo.create(**data)
