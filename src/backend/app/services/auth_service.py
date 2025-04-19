from werkzeug.security import check_password_hash, generate_password_hash
from app.models.User import User
from app.services.user_service import get_user_by_email, get_user_by_login



def login_user(data):
    """Авторизация пользователя."""
    if 'login' not in data or 'password' not in data:
        raise ValueError("Login and password are required")

    print(generate_password_hash(data['password']))

    # Поиск пользователя по логину
    user = get_user_by_login(data['login'])
    if not user or not check_password_hash(user.password_hash, data['password']):
        raise ValueError("Invalid login or password")

    return user

def register_user(data):
    """Регистрирует нового пользователя."""
    required_fields = ['second_name', 'first_name', 'last_name', 'login', 'password', 'email', 'role']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Field '{field}' is required")

    if get_user_by_login(data['login']):
        raise ValueError("Login already exists")
    if get_user_by_email(data['email']):
        raise ValueError("Email already exists")

    if data['role'] not in ['user', 'admin', 'client']:
        raise ValueError("Invalid role")

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256', salt_length=16)

    user = User(
        second_name=data['second_name'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        login=data['login'],
        password_hash=hashed_password,
        email=data['email'],
        role=data['role']
    )
    user.save()
    return user


def get_user_data(user_id):
    """Получение данных текущего пользователя по его ID."""
    user = User.nodes.get(id=user_id)
    if not user:
        raise ValueError("User not found")

    return user
