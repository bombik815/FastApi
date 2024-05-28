from sqlalchemy import Column, String
from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    # bookings = relationship("Bookings", back_populates="user")

    def __str__(self):
        return f"Пользователь {self.email}"