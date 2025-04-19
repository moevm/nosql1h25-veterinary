from ..models.User import User
from ..utils.functools import is_entity_exists


@is_entity_exists
def get_user_by_email(email):
    return User.nodes.get(email=email)


@is_entity_exists
def get_user_by_login(login):
    return User.nodes.get(login=login)
