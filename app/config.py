import os
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    DB_HOST: str = Field(os.getenv("DB_HOST"))
    DB_PORT: int = Field(os.getenv("DB_PORT"))
    DB_URL: str = Field(os.getenv("DB_URL"))


settings = Settings()