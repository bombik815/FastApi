from fastapi import APIRouter, Depends, Response, HTTPException, status

from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.users.dao import UsersDAO
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserAuth

router_auth = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

router_users = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router_auth.post("/register")  # ручка для регистрации юзера
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    # хешируем пароль пользователя
    hashed_password = get_password_hash(user_data.password)
    # сохраняем пользователя в БД
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router_auth.post("/login")  # ручка для входа юзера в систему
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return {"access_token": access_token, "token_type": "bearer"}


@router_auth.post("/logout")  # ручка для выхода юзера из систему
async def logout_user(response: Response):
    response.delete_cookie("access_token")


@router_users.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user
