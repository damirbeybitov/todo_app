from pydantic import BaseSettings, AnyHttpUrl
from typing import List, Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "My FastAPI App"
    VERSION: str = "1.0.0"
    BACKEND_CORS_ORIGINS: Optional[List[AnyHttpUrl]] = []

    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
