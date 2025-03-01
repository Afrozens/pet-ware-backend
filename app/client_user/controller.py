from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
import logging

from app.service import CRUDBase
from app.client_user.model import ClientUser
from app.client_user.schema import ClientUserUpdate, ClientUserSave

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ControllerClientUser(CRUDBase[ClientUser, ClientUserSave, ClientUserUpdate]):
    async def post_create_client_user(self, db: Session, *, obj_in: ClientUserSave):
        try:
            self.create(db=db, obj_in=obj_in)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
        
    async def put_update_client_user(self, db: Session, *, obj_in: ClientUserUpdate, client_user_id: str):
        try:
            client_user_current = db.query(self.model).where(self.model.id == client_user_id).filter(self.model.deleted_at == None).first()
            if not client_user_current:
                raise ValueError('client-user-not-found')
            obj_in_user_client = ClientUserUpdate(
                description=obj_in.description,
                experience=obj_in.experience
            )
            self.update(db=db, db_obj=client_user_current, obj_in=obj_in_user_client)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
        
    async def get_client_user(self, db: Session, *, client_user_id: str):
        try:
            client_user_current = db.query(self.model).where(self.model.id == client_user_id).filter(self.model.deleted_at == None).options(joinedload(self.model.frequently_askeds)).options(joinedload(self.model.client_services)).first()
            return client_user_current
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
            
    async def delete_remove_client_user(self, db: Session, *, client_user_id: str):
        try:
            self.remove(db=db, id=client_user_id)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
                    
client_user = ControllerClientUser(ClientUser)
