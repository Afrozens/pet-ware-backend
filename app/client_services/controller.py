from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
import logging

from app.category.model import Category
from app.service import CRUDBase
from app.client_services.model import ClientService
from app.client_services.schema import ClientServiceCreate, ClientServiceUpdate
from app.utils.paginate import converted_paginate_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ControllerClientService(CRUDBase[ClientService, ClientServiceCreate, ClientServiceUpdate]):
    async def put_update_client_service(self, db: Session, *, obj_in: ClientServiceUpdate, client_service_id: str):
        try:
            client_service_current = db.query(self.model).where(self.model.id == client_service_id).filter(self.model.deleted_at == None).first()
            if not client_service_current:
                raise ValueError('client-service-not-found')
            self.update(db=db, db_obj=client_service_current, obj_in=obj_in)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
        
    async def post_create_client_service(self, db: Session, *, obj_in: ClientServiceCreate):
        try:
            self.create(db=db, obj_in=obj_in)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
        
    async def get_multi_services(self, db: Session, *, page: int, limit: int, filter: str, client_user_id: str):
        try:
            base_query = db.query(self.model).where(self.model.deleted_at == None).filter(self.model.client_id == client_user_id).order_by(self.model.created_at.asc())
            
            if filter is not None and filter != "null":
                search = f"%{filter}%"
                query_search = base_query.filter(Category.name.like((search)))
            else:
                query_search = base_query
            return converted_paginate_data(page, limit, query_search)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
        
    async def delete_remove_client_service(self, db: Session, *, client_service_id: str):
        try:
            self.remove(db=db, id=client_service_id)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
        
client_service = ControllerClientService(ClientService)
