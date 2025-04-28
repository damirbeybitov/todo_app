from fastapi import FastAPI
# from app.api.v1.endpoints import users, auth  # пример
# from app.core.config import settings

# def create_app() -> FastAPI:
#     app = FastAPI(
#         title=settings.PROJECT_NAME,
#         version=settings.VERSION,
#     )

#     app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
#     app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
    
#     return app

app = FastAPI()
