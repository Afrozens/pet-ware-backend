from fastapi import HTTPException
from sqlalchemy.orm import Session
import logging

from app.settings import get_settings
from app.aws.service import S3Service
from app.file.service import serviceFile

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

s3_service = S3Service()
settings = get_settings()

class ControllerFile():
    async def get_image_by(self, db: Session, *, file_id: str):
        try:
            url_s3_file = None
            image = await serviceFile.read_file(db=db, file_id=file_id)
            if image:
                url_s3_file = s3_service.download_file(f"{image.folder}/{image.name}", settings.BUCKET_NAME)
            return url_s3_file
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=f'There is a error: {str(ex)}')

file = ControllerFile()