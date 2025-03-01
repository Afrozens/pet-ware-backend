from uuid import uuid4
from fastapi import File, HTTPException, Depends, UploadFile
from sqlalchemy.orm import Session, joinedload
from typing import Optional
import logging

from app.settings import get_settings
from app.aws.service import S3Service
from app.user.model import User
from app.user.schema import UserUpdate, UserInDB
from app.user.service import ServiceUser
from app.user.dependecies import user_verified_id
from app.file.service import service_file
from app.utils.formated import formated_file
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
        
    async def get_avatar_by_user(self, db: Session, *, avatar_id: str):
        try:
            url_s3_file = None
            image = await service_file.read_file(db=db, file_id=avatar_id)
            if image:
                url_s3_file = s3_service.download_file(f"{image.folder}/{image.name}", settings.BUCKET_NAME)
            return url_s3_file
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=ex)
        
    async def put_update_avatar_user(self, db: Session, *, file: UploadFile = File(...), user_id: str = Depends(user_verified_id)):
        try:
            user_current = db.query(self.model).where(self.model.deleted_at == None).filter(self.model.id == user_id).first()
            image_current = await service_file.read_file(db=db, file_id=user_current.profile_picture)
            if image_current:
                await service_file.remove_file(db=db, file_id=image_current.id)
                file_key = f"{image_current.folder}/{image_current.name}"
                await s3_service.delete_file(bucket_name=settings.BUCKET_NAME, file_key=file_key)

            # Upload new file to S3
            save_to = f"{uuid4()}.png"
            folder_current = 'user'
            upload_s3 = await s3_service.upload_file(file.file, settings.BUCKET_NAME, folder_current, save_to)

            if upload_s3:
                # Save file metadata in DB and update user's avatar
                files_obj_in = formated_file(filename=save_to, folder=folder_current, size=int(file.size))
                file_created = await service_file.create_file(db=db, user_id=user_id, obj_in=files_obj_in)
                obj_in = {'profile_picture': file_created.id}
                await self.put_update_user(db=db, user_id=user_id, obj_in=obj_in)
            
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=ex)
        
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
