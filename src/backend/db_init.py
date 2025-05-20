import requests

# URL для регистрации пользователей
register_url = "http://localhost:5000/api/users/register"


# Данные для пользователя с ролью 'client'
client_data = {
    "second_name": f"Иванов",
    "first_name": f"Иван",
    "last_name": f"Иванович",
    "login": "client_user",
    "password": "user123",
    "email": f"user@example.com",
    "role": "client",
    "birth_date": "1970-01-02"
}

# Данные для пользователя с ролью 'admin'
admin_data = {
    "second_name": f"Петров",
    "first_name": f"Петр",
    "last_name": f"Петрович",
    "login": "admin_user",
    "password": "admin123",
    "email": f"admin@example.com",
    "role": "admin",
    "birth_date": "1989-12-11"
}

# Данные для пользователя с ролью 'doctor'
doctor_data = {
    "second_name": f"Карлов",
    "first_name": f"Карл",
    "last_name": f"Карлович",
    "login": "doctor_user",
    "password": "doctor123",
    "email": f"doctor@example.com",
    "role": "doctor",
    "birth_date": "2000-05-05"
}

# Регистрация пользователя с ролью 'client'
print("\nРегистрация пользователя с ролью 'client'...")
try:
    user_response = requests.post(register_url, json=client_data)
    print(f"Статус: {user_response.status_code}")
    print(f"Ответ: {user_response.text}")
except Exception as e:
    print(f"Ошибка при регистрации клиента: {e}")

# Регистрация пользователя с ролью 'admin'
print("\nРегистрация пользователя с ролью 'admin'...")
try:
    admin_response = requests.post(register_url, json=admin_data)
    print(f"Статус: {admin_response.status_code}")
    print(f"Ответ: {admin_response.text}")
except Exception as e:
    print(f"Ошибка при регистрации администратора: {e}")

# Регистрация пользователя с ролью 'doctor'
print("\nРегистрация пользователя с ролью 'doctor'...")
try:
    doctor_response = requests.post(register_url, json=doctor_data)
    print(f"Статус: {doctor_response.status_code}")
    print(f"Ответ: {doctor_response.text}")
except Exception as e:
    print(f"Ошибка при регистрации доктора: {e}")
