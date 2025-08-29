from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field(default="postgresql+psycopg2://qa_user:qa_pass@db:5432/qa_db")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
