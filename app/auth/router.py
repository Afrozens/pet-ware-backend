from fastapi import APIRouter, status, Depends, Header, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.schema import Email, Login, RefreshTokenRequest, Reset, VerifyUser
from app.database import get_session
from app.auth.controller import auth as auth_controller
from app.user.schema import UserSaveConsumer

router = APIRouter()

@router.post('/login', status_code=status.HTTP_200_OK, response_model=Login)
async def user_login(data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    data = await auth_controller.post_login_token(db=session, obj_in=data)
    return data

@router.post('/refresh', status_code=status.HTTP_200_OK, response_model=Login)
async def refresh_token(
    request: RefreshTokenRequest, 
    session: Session = Depends(get_session)):
    refresh_token = request.refresh_token
    data = await auth_controller.post_refresh_token(db=session, token=refresh_token)
    return data

@router.post('/logout', status_code=status.HTTP_200_OK)
async def user_logout():
    response = JSONResponse(content={'message': 'logout-success'})
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response

@router.post('/verify', status_code=status.HTTP_200_OK)
async def verify_user_account(data: VerifyUser, session: Session = Depends(get_session)):
    await auth_controller.post_activate_user_account(data, session)
    return JSONResponse({"message": "account-activated-success"})

@router.post('/forgot-password', status_code=status.HTTP_200_OK)
async def forgot_password(data: Email, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    await auth_controller.post_email_forgot_password_link(obj_in=data.email, background_tasks=background_tasks, db=session)
    return JSONResponse(content={"message": "email-password-link"})

@router.put('/reset-password', status_code=status.HTTP_200_OK)
async def reset_password(data: Reset, session: Session = Depends(get_session)):
    await auth_controller.put_reset_user_password(obj_in=data, db=session)
    return JSONResponse(content={"message": "password-updated"})

@router.post('/register/user', status_code=status.HTTP_201_CREATED)
async def register_user(data: UserSaveConsumer, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    await auth_controller.post_register_consumer(db=session, background_tasks=background_tasks, obj_in=data)

@router.post('/register/client', status_code=status.HTTP_201_CREATED)
async def register_client(data: UserSaveConsumer, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    await auth_controller.post_register_client(db=session, background_tasks=background_tasks, obj_in=data)