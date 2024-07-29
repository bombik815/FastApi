from datetime import date

from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.booking.router import router as router_bookings
from app.images.router import router_images
from app.users.router import router_users, router_auth
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms
from app.pages.router import router as router_pages

app = FastAPI()

"""
Этот код использует метод mount объекта приложения FastAPI (app)
 для монтирования директории статических файлов к маршруту "/static".
"""
app.mount("/static", StaticFiles(directory="app/static"), "static")

# Включение основных роутеров
app.include_router(router_auth)
app.include_router(router_users)

app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)

app.include_router(router_pages)

app.include_router(router_images)


# Подключение CORS, чтобы запросы к API могли приходить из браузера
origins = [
    # 3000 - порт, на котором работает фронтенд на React.js
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Включаем возможность передачи cookie
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3/swagger-ui.css",
    )


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels", response_model=list[SHotel])
async def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    has_spa: bool | None = None,
    stars: int | None = Query(None, ge=1, le=5),
):
    hotels = [
        {
            "address": "street",
            "name": "hotel",
            "stars": 5,
        },
    ]
    return hotels


# Код для случая, если вы хотите запускать uvicorn через python main.py
if __name__ == "__main__":
    import uvicorn

    import os.path
    import sys

    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    uvicorn.run(
        app="app.main:app",
        reload=True,
    )
