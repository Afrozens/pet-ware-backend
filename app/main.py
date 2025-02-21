from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.settings import get_settings
from app.router import api_router

settings = get_settings()

def create_application():
    application = FastAPI(title=settings.APP_NAME, version="1.0.0",
    )

    application.include_router(api_router)
    return application

app = create_application()
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

origins = [
    str(settings.FRONTEND_HOST)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Working..."}
