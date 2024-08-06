import asyncio
from app.tasks.celery import celery

from app.tasks.reminders.bookings import remind_of_booking


@celery.task(name="email.booking_reminder_1day")
def remind_booking_1day():
    asyncio.run(remind_of_booking(1))


@celery.task(name="email.booking_reminder_3days")
def remind_booking_3days():
    asyncio.run(remind_of_booking(3))
