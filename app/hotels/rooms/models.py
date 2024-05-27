from sqlalchemy import Integer, Column, String, JSON, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primery_key=True)
    hotel_id = Column(ForeignKey("hotels.id"), )
    name = Column(String, )
    description = Column(String, nullable=True)
    price = Column(Integer, )
    services = Column(JSON, nullable=True)
    quantity = Column(Integer, )
    image_id = Column(Integer)

    hotel = relationship("Hotels", back_populates="rooms")
    booking = relationship("Bookings", back_populates="room")

    def __str__(self):
        return f"Номер {self.name}"