from typing import Optional
from fastapi import HTTPException, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime
import logging

from app.auth.schema import Reset, VerifyUser
from app.auth.config import get_hash_password, get_refresh_user, verify_password
from app.auth.utils import FORGOT_PASSWORD, USER_VERIFY_ACCOUNT, is_password_strong_enough
from app.auth.service import _generate_tokens
from app.client_user.schema import ClientUserSave
from app.user.model import User
from app.user.schema import UserSaveConsumer
from app.user.service import ServiceUser
from app.role.service import role as service_role
from app.seeders.roles import Role as role_seeders
from app.client_user.controller import client_user as client_user_controller

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ControllerAuth(ServiceUser):
    async def post_login_token(self, db: Session,*, obj_in: OAuth2PasswordRequestForm):
        try:
            user = self.get_by_email(db=db, email=obj_in.username)
            if not user:
                raise ValueError("email-isnt-registered")
            if not verify_password(obj_in.password, user.password):
                raise ValueError("invalid-data-sign")
            if not user.verified_at:
                raise ValueError("account-isnt-verified")
            response = _generate_tokens(user)
            return response
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
            
    async def post_refresh_token(self, db: Session, *, token: str):
        try:
            user = await get_refresh_user(token=token, db=db)
            if not user:
                raise HTTPException(status_code=404, detail="token-not-found")
            return _generate_tokens(user)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=ex)
    
    async def post_activate_user_account(self, obj_in: VerifyUser, session: Session):
        user = session.query(User).filter(User.email == obj_in.email).first()
        if not user:
            raise HTTPException(status_code=400, detail="This link is not valid.")

        user_token = user.get_context_string(context=USER_VERIFY_ACCOUNT)
        logging.info(f"Log-1 => {user.updated_at.strftime('%m%d%Y%H%M%S')}")
        try: 
            token_valid = verify_password(user_token, obj_in.token)
        except Exception as verify_exec:
            logging.exception(verify_exec)
            token_valid = False
        if not token_valid:
            raise HTTPException(status_code=400, detail="This token is not valid.")
    
        user.active = True
        user.updated_at = datetime.now()
        session.add(user)
        session.commit()
        session.refresh(user)
        logging.info(f"Log-2 => {user.updated_at.strftime('%m%d%Y%H%M%S')}")

        return user

    async def post_email_forgot_password_link(self, obj_in: str, background_tasks, db: Session):
        try:
            user = self.get_by_email(db=db, email=obj_in)
            if not user.active:
                raise HTTPException(status_code=500, detail="account-not-activated")
            # logic of send email
            # await send_password_reset_email(user=user, background_tasks=background_tasks) 
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=ex)

    async def put_reset_user_password(self, obj_in: Reset, db: Session):
        try:
            user = self.get_by_email(db=db, email=obj_in.email)
            if not user:
                raise HTTPException(status_code=404, detail="user-not-found")
            if not user.active:
                raise HTTPException(status_code=500, detail="account-not-activated")

            user_token = user.get_context_string(context=FORGOT_PASSWORD)
            token_valid = verify_password(user_token, obj_in.token)
            if not token_valid:
                raise HTTPException(status_code=500, detail="token-expired")
        
            data_user = {"password": get_hash_password(obj_in.password)}
            self.update(db=db, db_obj=user, obj_in=data_user)
        except Exception as ex:
            token_valid = False
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=ex)
    
    async def post_register_user(self, db: Session, *, obj_in: Optional[UserSaveConsumer]):
        try:
            if not is_password_strong_enough(obj_in.password):
                raise HTTPException(status_code=400, detail="not-strong-password")
            db_obj = User(**obj_in.model_dump(exclude_unset=True))
            db_obj.updated_at = datetime.now()
            db_obj.password=get_hash_password(obj_in.password)
            user = super().create(db=db, obj_in=db_obj)
            return user
        except Exception as ex: 
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=ex)

    async def post_register_consumer(self, obj_in: UserSaveConsumer, *, background_tasks: BackgroundTasks, db: Session):
        try:
            user = await self.post_register_user(db=db, obj_in=obj_in)
            role_customer = service_role.get_by_name(db=db, name=role_seeders.CONSUMER["name"])
            data = {
                'roles_id': role_customer.id
            }
            self.update(db=db, db_obj=user, obj_in=data)
            # await send_welcome_app(user=user, background_tasks=background_tasks)    
            # Account confirmation Email
            # await send_account_verification_email(user, background_tasks=background_tasks)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))

    async def post_register_client(self, obj_in: UserSaveConsumer, *, background_tasks: BackgroundTasks, db: Session):
        try:
            user = await self.post_register_user(db=db, obj_in=obj_in)
            role_client = service_role.get_by_name(db=db, name=role_seeders.CLIENT["name"])
            data = {
                'roles_id': role_client.id
            }
            self.update(db=db, db_obj=user, obj_in=data)
            obj_in_client = ClientUserSave(
                active=False,
                premium=False,
                user_id=user.id
            )
            await client_user_controller.post_create_client_user(db=db, obj_in=obj_in_client)
            # await send_welcome_app(user=user, background_tasks=background_tasks)    
            # Account confirmation Email
            # await send_account_verification_email(user, background_tasks=background_tasks)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))

auth = ControllerAuth(User)
