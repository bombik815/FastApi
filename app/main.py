from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class SHotel(BaseModel):
    address: str
    name: str
    stars: int
@app.get("/hotels", response_model=list[SHotel])
async def get_hotels(location: str,
                    date_from: date,
                    date_to: date,
                    has_spa: bool | None = None,
                    stars: int | None = Query(None, ge=1, le=5),
                    ):
    hotels =[{
                "address": "street",
                "name": "hotel",
                "stars": 5,
            },]
    return hotels

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/booking")
async def book_booking(booking: SBooking):
    return {"message": "booking successful"}


# Код для случая, если вы хотите запускать uvicorn через python main.py
if __name__ == "__main__":
    import uvicorn

    import os.path
    import sys
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    uvicorn.run(app="app.main:app",  reload=True,)
