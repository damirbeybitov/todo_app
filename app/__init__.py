from fastapi import FastAPI
from app.api.v1.endpoints import api_router  # пример
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
    )

    app.include_router(api_router, prefix="/api/v1")
    
    return app
