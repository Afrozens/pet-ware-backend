from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_admin, get_current_user
from app.auth.router import router as router_auth
from app.user.router import router as router_user

api_router = APIRouter()

# router without authenticated

api_router.include_router(router_auth, prefix="/auth", tags=["Auth"],
    responses={404: {"description": "Not found"}})

# router with authenticated (user)
api_router.include_router(router_user, prefix="/user", tags=["Users"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)])

# router with authenticated (admin)
