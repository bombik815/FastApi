from pydantic import BaseModel, EmailStr


# схема для валидации регистрации пользователя
class SUserAuth(BaseModel):
    email: EmailStr
    password: str
