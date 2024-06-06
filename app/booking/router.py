from fastapi import APIRouter

from app.booking.DAO import BookingDAO
from app.booking.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookins() -> list[SBooking]:
    result = await BookingDAO.find_all()
    return result
