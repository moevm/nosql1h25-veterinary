from neomodel import config


import uuid
from datetime import datetime

from app.db.neo4j_controller import Neo4jRepository
from app.models.Pet import Pet
from app.models.Client import Client
from app.models.PetType import PetType
from app.models.Procedure import Procedure
from app.models.Appointment import Appointment
from app.models.Doctor import Doctor
from app.models.Office import Office
from app.models.Day import Day

def test_pet_crud():
    pet_repo = Neo4jRepository(Pet)
    # Создание
    pet = pet_repo.create(
        name="ТестПитомец",
        breed="ТестоваяПорода",
        birthdate=datetime(2020, 1, 1),
        gender="male",
        photo_url="http://example.com/photo.jpg"
    )
    assert pet is not None
    print("Создан питомец:", pet.to_dict())

    # Получение по id
    found = pet_repo.get_by_id(pet.uid)
    assert found is not None
    print("Найден питомец:", found.to_dict())

    # Обновление
    res = pet_repo.update(pet.uid, breed="ИзменённаяПорода")
    updated = pet_repo.get_by_id(pet.uid)
    assert updated.breed == "ИзменённаяПорода"
    print("Обновлён питомец:", updated.to_dict())

    # Фильтрация
    pets = pet_repo.filter(breed__icontains="змен")
    assert any(p.uid == pet.uid for p in pets)
    print("Фильтрация питомцев:", [p.to_dict() for p in pets])

    # Удаление
    assert pet_repo.delete(pet.uid)
    assert pet_repo.get_by_id(pet.uid) is None
    print("Питомец успешно удалён.")

def test_client_pet_relation():
    client_repo = Neo4jRepository(Client)
    pet_repo = Neo4jRepository(Pet)

    # Создаём клиента и питомца
    client = client_repo.create(
        first_name="Иван",
        second_name="Иванович",
        last_name="Иванов",
        login="test_login_" + str(uuid.uuid4()),
        password_hash="hash",
        birth_date=datetime(1990, 1, 1),
        email=f"test_{uuid.uuid4()}@mail.com",
        gender="male",
        phone_number="1234567890"
    )
    pet = pet_repo.create(
        name="Рекс",
        breed="Овчарка",
        birthdate=datetime(2021, 5, 5),
        gender="male",
        photo_url=""
    )

    # Связываем клиента и питомца
    client.pets.connect(pet)
    assert pet in client.pets.all()
    print("Связь клиент-питомец успешно создана.")

    # Чистим за собой
    pet.delete()
    client.delete()

def test_full_appointment_flow():
    client_repo = Neo4jRepository(Client)
    pet_repo = Neo4jRepository(Pet)
    pet_type_repo = Neo4jRepository(PetType)
    procedure_repo = Neo4jRepository(Procedure)
    doctor_repo = Neo4jRepository(Doctor)
    office_repo = Neo4jRepository(Office)
    day_repo = Neo4jRepository(Day)
    appointment_repo = Neo4jRepository(Appointment)

    # Создаём все необходимые сущности
    client = client_repo.create(
        first_name="Мария",
        second_name="Петровна",
        last_name="Петрова",
        login="test_login_" + str(uuid.uuid4()),
        password_hash="hash",
        birth_date=datetime(1985, 2, 2),
        email=f"test_{uuid.uuid4()}@mail.com",
        gender="female",
        phone_number="0987654321"
    )
    pet_type = pet_type_repo.create(type_name="Кошка")
    pet = pet_repo.create(
        name="Мурка",
        breed="Дворовая",
        birthdate=datetime(2018, 3, 3),
        gender="female",
        photo_url=""
    )
    pet.pet_type.connect(pet_type)
    client.pets.connect(pet)

    procedure = procedure_repo.create(
        name="Вакцинация",
        cost=1000.0,
        description="Общая вакцинация",
        available=True
    )
    procedure.pet_types.connect(pet_type)

    doctor = doctor_repo.create(
        first_name="Олег",
        second_name="Сергеевич",
        last_name="Сидоров",
        login="test_login_" + str(uuid.uuid4()),
        password_hash="hash",
        birth_date=datetime(1975, 4, 4),
        email=f"test_{uuid.uuid4()}@mail.com",
        gender="male",
        phone_number="5555555555",
        experience="10 лет",
        specialization="Терапия"
    )

    office = office_repo.create(
        name="Главный офис",
        address="ул. Центральная, 1",
        email="office@example.com",
        phone_number="111222333",
        opening_hours="9:00-18:00",
        meta="Тестовый офис"
    )
    day = day_repo.create(date=datetime(2025, 4, 21))

    # Создаём приём и связываем все сущности
    appointment = appointment_repo.create(
        date=datetime(2025, 4, 21, 10, 0),
        reason="Плановая вакцинация",
        comment="Без особенностей",
        diagnosis="Здорова",
        recommend="Повторить через год",
        file_urls=[]
    )
    appointment.pet.connect(pet)
    appointment.client.connect(client)
    appointment.doctor.connect(doctor)
    appointment.procedure.connect(procedure)
    appointment.day.connect(day)

    # Проверяем связи
    assert pet in client.pets.all()
    assert pet_type in pet.pet_type.all()
    assert procedure in pet_type.procedures.all()
    assert doctor in appointment.doctor.all()
    assert day in appointment.day.all()

    print("Все связи для приёма успешно созданы.")

    # Чистим за собой
    appointment.delete()
    day.delete()
    office.delete()
    doctor.delete()
    procedure.delete()
    pet.delete()
    pet_type.delete()
    client.delete()

if __name__ == "__main__":
    test_pet_crud()
    test_client_pet_relation()
    test_full_appointment_flow()
    print("Все тесты успешно завершены.")
