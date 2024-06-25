from fastapi import APIRouter, Depends

from app.booking.DAO import BookingDAO
from app.booking.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookins(user: Users = Depends(get_current_user)):  # -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)
