from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
import logging

from app.service import CRUDBase
from app.client_user.model import ClientUser
from app.client_user.schema import ClientUserUpdate, ClientUserSave

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ControllerAgency(CRUDBase[ClientUser, ClientUserSave, ClientUserUpdate]):
    async def post_create_client_user(self, db: Session, *, obj_in: ClientUserSave):
        try:
            self.create(db=db, obj_in=obj_in)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))

client_user = ControllerAgency(ClientUser)
