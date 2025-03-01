from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_admin
from app.database import get_session
from app.client_user.schema import ClientUserUpdate, ClientUserWithRelations
from app.client_user.controller import client_user as client_user_controller
from app.user.schema import User

router = APIRouter()

@router.put('/update/{client_user_id}', status_code=status.HTTP_200_OK)
async def update_client_user(data: ClientUserUpdate, client_user_id: str, session: Session = Depends(get_session)):
    await client_user_controller.put_update_client_user(db=session, obj_in=data, client_user_id=client_user_id)

@router.get('/determinated/{client_user_id}', status_code=status.HTTP_200_OK, response_model=ClientUserWithRelations)
async def get_client_user(client_user_id: str, session: Session = Depends(get_session)):
    client_user_current = await client_user_controller.get_client_user(db=session, client_user_id=client_user_id)
    return client_user_current

@router.delete('/{client_user_id}', status_code=status.HTTP_200_OK)
async def delete_client_user(client_user_id: str, session: Session = Depends(get_session), user: User = Depends(get_current_admin)):
    await client_user_controller.delete_remove_client_user(db=session, client_user_id=client_user_id)