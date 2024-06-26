from datetime import date

from fastapi import APIRouter, Depends

from app.booking.DAO import BookingDAO
from app.booking.schemas import SBooking
from app.exceptions import RoomCannotBeBooked
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookins(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post("")
async def add_booking(
        room_id: int, date_from: date, date_to: date,
        user: Users = Depends(get_current_user)):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)

    if not booking:
        raise RoomCannotBeBooked
    # TypeAdapter и model_dump - это новинки новой версии Pydantic 2.0
    # booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()
    # Celery - отдельная библиотека
    # send_booking_confirmation_email.delay(booking, user.email)
    # Background Tasks - встроено в FastAPI
    # background_tasks.add_task(send_booking_confirmation_email, booking, user.email)
    # return booking
