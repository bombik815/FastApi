from datetime import date

from fastapi import APIRouter, Depends

from app.booking.DAO import BookingDAO
from app.booking.schemas import SBooking
from app.booking.service import BookingService
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
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user),
):
    new_booking = await BookingService.add_booking(
        room_id,
        date_from,
        date_to,
        user,
    )
    return new_booking


@router.delete("/{booking_id}")
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    await BookingDAO.delete(
        id=booking_id,
        user_id=current_user.id,
    )
