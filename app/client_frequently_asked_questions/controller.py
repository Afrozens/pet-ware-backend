from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
import logging

from app.service import CRUDBase
from app.client_frequently_asked_questions.model import ClientFrequentlyAskedQuestions
from app.client_frequently_asked_questions.schema import ClientFrenquentlyAskedQuestionsCreate, ClientFrenquentlyAskedQuestionsUpdate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ControllerAsked(CRUDBase[ClientFrequentlyAskedQuestions, ClientFrenquentlyAskedQuestionsCreate, ClientFrenquentlyAskedQuestionsUpdate]):
    async def put_update_frequently_asked(self, db: Session, *, obj_in: ClientFrenquentlyAskedQuestionsUpdate, frequently_asked_id: str):
        try:
            asked_current = db.query(self.model).where(self.model.id == frequently_asked_id).filter(self.model.deleted_at == None).first()
            if not asked_current:
                raise ValueError('frequently-asked-not-found')
            self.update(db=db, db_obj=asked_current, obj_in=obj_in)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
        
    async def post_create_frequently_asked(self, db: Session, *, obj_in: ClientFrenquentlyAskedQuestionsCreate):
        try:
            self.create(db=db, obj_in=obj_in)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
        
    async def get_frequently_askeds_all(self, db: Session, client_user_id: str):
        try:
            askeds = db.query(self.model).where(self.model.deleted_at == None).filter(self.model.client_id == client_user_id).order_by(self.model.created_at.asc()).all()
            return askeds
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
        
    async def delete_remove_frequently_asked(self, db: Session, *, frequently_asked_id: str):
        try:
            self.remove(db=db, id=frequently_asked_id)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise HTTPException(status_code=500, detail=(ex))
        
frequently_asked = ControllerAsked(ClientFrequentlyAskedQuestions)
