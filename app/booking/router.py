from datetime import date

from fastapi import APIRouter, Depends, BackgroundTasks
from pydantic import TypeAdapter

from app.booking.DAO import BookingDAO
from app.booking.schemas import SBooking, SNewBooking
from app.booking.service import BookingService
from app.exceptions import RoomCannotBeBooked
from app.tasks.tasks import send_booking_confirmation_email
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
    booking: SNewBooking,
    background_tasks: BackgroundTasks,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(
        user.id,
        booking.room_id,
        booking.date_from,
        booking.date_to,
    )
    if not booking:
        raise RoomCannotBeBooked
    # TypeAdapter и model_dump - это новинки новой версии Pydantic 2.0
    booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()
    # Celery - отдельная библиотека
    # send_booking_confirmation_email.delay(booking, user.email)

    # Background Tasks - встроено в FastAPI
    background_tasks.add_task(send_booking_confirmation_email, booking, user.email)
    return booking


@router.delete("/{booking_id}")
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    await BookingDAO.delete(
        id=booking_id,
        user_id=current_user.id,
    )
