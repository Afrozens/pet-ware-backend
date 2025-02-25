from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_session
from app.file.controller import file as controller_file

router = APIRouter()

@router.get('/image/{file_id}', status_code=status.HTTP_200_OK)
async def get_image_by_id(file_id: str, session: Session = Depends(get_session)):
    image_url = await controller_file.get_image_by(db=session, file_id=file_id)
    return image_url