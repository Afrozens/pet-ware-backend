from fastapi import APIRouter, Depends

from app.auth.router import router as router_auth

api_router = APIRouter()

# router without authenticated

api_router.include_router(router_auth, prefix="/auth", tags=["Auth"],
    responses={404: {"description": "Not found"}})

# router with authenticated
