from fastapi import APIRouter
from sqlalchemy import select

from app.booking.models import Bookings
from app.database import async_session_maker

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookins():
    async with  async_session_maker() as session:
        query = select(Bookings)  # select * from bookings
        result = await session.execute(query)  # вернет ответ на запрос выше
        return (result.mappings().all())  # вернет список всех записей
