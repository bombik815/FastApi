from datetime import date

from app.booking.DAO import BookingDAO
from app.exceptions import RoomCannotBeBooked
from app.users.models import Users


class BookingService:
    @classmethod
    async def add_booking(
        cls,
        room_id: int,
        date_from: date,
        date_to: date,
        user: Users,
    ):
        booking = await BookingDAO.add(
            user.id,
            room_id,
            date_from,
            date_to,
        )

        if not booking:
            raise RoomCannotBeBooked
        # TypeAdapter и model_dump - это новинки новой версии Pydantic 2.0
        # booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()
        # Celery - отдельная библиотека
        # send_booking_confirmation_email.delay(booking, user.email)
        # Background Tasks - встроено в FastAPI
        # background_tasks.add_task(send_booking_confirmation_email, booking, user.email)
        return booking
