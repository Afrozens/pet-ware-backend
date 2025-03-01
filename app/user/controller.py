from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
from typing import Optional
import logging

from app.settings import get_settings
from app.aws.service import S3Service
from app.user.model import User
from app.user.schema import UserUpdate, UserInDB
from app.user.service import ServiceUser
from app.user.dependecies import user_verified_id
# from app.file.service import serviceFile
# from app.utils.formated import formated_url_file

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

s3_service = S3Service()
settings = get_settings()

class ControllerUser(ServiceUser):
    async def get_me(self, db: Session, *, user_id: str = Depends(user_verified_id)):
        try:
            user_current = db.query(self.model).filter(self.model.deleted_at == None).where(self.model.id == user_id).options(joinedload(self.model.client_user)).options(joinedload(self.model.role)).first()
            return user_current
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))

    async def put_update_user(self, db: Session, *, user_id: str = Depends(user_verified_id), obj_in: Optional[UserUpdate]):
        try:
            user_current = self.get(db=db, id=user_id)
            self.update(db=db, db_obj=user_current, obj_in=obj_in)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))

    async def delete_remove_user(self, db: Session, *, user_id: str = Depends(user_verified_id)):
        try:
            self.remove(db=db, id=user_id)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=ex)

    async def get_determinated_user(self, db: Session, *, user_id: str = Depends(user_verified_id)) -> Optional[UserInDB]:
        try:
            user = db.query(self.model).filter(self.model.deleted_at == None).where(self.model.id == user_id).options(joinedload(self.model.role)).options(joinedload(self.model.client_user)).first()
            if not user:
                raise ValueError("user-not-found")
            return user
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=ex)

user = ControllerUser(User)
