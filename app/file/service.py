from sqlalchemy.orm import Session
import logging

from app.service import CRUDBase
from app.file.model import File
from app.file.schema import FileSave, FileInDBBase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class service_files(CRUDBase[File, FileSave, FileSave]):
    async def read_file(self, db: Session, file_id: str):
        try:
            if not file_id:
                raise 'The id determinted isnt found'
            return self.get(db=db, id=file_id)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise f'There is a error: {str(ex)}'

    async def create_file(self, db: Session, *, user_id: str, obj_in) -> FileInDBBase:
        try:
            db_obj = self.model(
                user_id=user_id,
                **obj_in
            )
            file_current = self.create(db=db, obj_in=db_obj)
            return file_current
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise f'There is a error: {str(ex)}'

    async def remove_file(self, db: Session, file_id: str):
        try:
            self.remove(db=db, id=file_id)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise f'There is a error: {str(ex)}'

service_file = service_files(File)
