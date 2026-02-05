from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_API: str
    HYPIXEL_API: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
