import os
from controllers.auth.login import pwd_context


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def registry_cases(phone, name, password, region):
    if get_user_login_service(phone):
        return {"message": "номер уже зарегестрирован !"}
    password = hash_password(password)


    return {"message": "success"}

