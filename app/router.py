from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_admin, get_current_user
from app.auth.router import router as router_auth
from app.category.router import router as router_category
from app.user.router import router as router_user
from app.client_frequently_asked_questions.router import router as router_frequently_asked
from app.client_user.router import router as router_client_user
from app.client_services.router import router as router_client_services

api_router = APIRouter()

# router without authenticated
api_router.include_router(router_auth, prefix="/auth", tags=["Auth"],
    responses={404: {"description": "Not found"}})

api_router.include_router(router_category, prefix="/category", tags=["Category"],
    responses={404: {"description": "Not found"}})

# router with authenticated (user)
api_router.include_router(router_user, prefix="/user", tags=["User"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)])

api_router.include_router(router_client_user, prefix="/client-user", tags=["ClientUser"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)])

api_router.include_router(router_client_services, prefix="/client-service", tags=["ClientService"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)])

api_router.include_router(router_frequently_asked, prefix="/client-frequently-asked", tags=["ClientFrequentlyAsked"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)])

# router with authenticated (admin)
