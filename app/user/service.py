from typing import Optional
from sqlalchemy.orm import Session

from app.service import CRUDBase
from app.user.model import User
from app.user.schema import UserCreate, UserUpdate

class ServiceUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(self.model).filter(User.email == email).first()

service_user = ServiceUser(User)