from urllib.parse import urlparse
from fastapi import APIRouter, HTTPException, status, File, UploadFile

from app.aws.service import S3Service
from app.settings import get_settings

router = APIRouter()
settings = get_settings()
s3_service = S3Service()

@router.post('/upload-file/{file_name}/{folder}', status_code=status.HTTP_201_CREATED)
async def upload_file(file_name: str, folder: str , file: UploadFile = File(...)):
    upload_s3 = await s3_service.upload_file(file.file, settings.BUCKET_NAME, folder, file_name)
    if upload_s3:
        file_current = f"{folder}/{file_name}"
        url = s3_service.download_file(file_current, settings.BUCKET_NAME)
        return url
    raise HTTPException(status_code=500, detail='There is a error in upload file')