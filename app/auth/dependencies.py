from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session, joinedload

from app.database import get_session
from app.auth.config import get_token_user
from app.user.model import User

message_not_authorised = 'not-authorised'
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(request: Request, optional_token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    token = request.cookies.get('access_token')
    if token:
        user = await get_token_user(token=token, db=db)
    elif optional_token:
        user = await get_token_user(token=optional_token, db=db)
    if user: 
        return user
    raise HTTPException(status_code=401, detail=message_not_authorised)

async def get_current_admin(request: Request, optional_token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    user = await get_current_user(request=request, optional_token=optional_token, db=db)

    user_with_role = (
            db.query(User)
            .options(joinedload(User.role))
            .filter(User.id == user.id)
            .first()
    )
    role_name = user_with_role.role.name

    if role_name != 'administrador': 
        raise HTTPException(status_code=401, detail=message_not_authorised)
    return user