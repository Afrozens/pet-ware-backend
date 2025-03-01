from typing import Optional
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database import get_session
from app.user.schema import User, UserUpdate, UserWithRelations
from app.user.controller import user as controller_user
from app.auth.dependencies import get_current_user, get_current_admin

router = APIRouter()

@router.get('/me', status_code=status.HTTP_200_OK, response_model=UserWithRelations)
async def me_user(session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    user_current = await controller_user.get_me(db=session, user_id=user.id)
    return user_current

@router.get('/determined/{id}', status_code=status.HTTP_200_OK, response_model=UserWithRelations)
async def determined_user(id: str, session: Session = Depends(get_session)):
    user_current = await controller_user.get_determinated_user(db=session, user_id=id) 
    return user_current

@router.put('/update/{id}', status_code=status.HTTP_200_OK)
async def update_user(id: str, data: Optional[UserUpdate], session: Session = Depends(get_session)):
    await controller_user.put_update_user(db=session, user_id=id, obj_in=data)
    return JSONResponse({'message': 'user-updated-success'})

@router.delete('/remove/{id}', status_code=status.HTTP_200_OK)
async def remove_user(id: str, session: Session = Depends(get_session), user_current: User = Depends(get_current_admin)):
    await controller_user.delete_remove_user(db=session, user_id=id)
    return JSONResponse({'message': 'user-removed-success'})