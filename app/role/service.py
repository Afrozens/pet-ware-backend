from typing import Optional
from sqlalchemy.orm import Session

from app.service import CRUDBase
from app.role.schema import Role, RoleBase
from app.role.model import Rol as RoleModel

class ServicesRole(CRUDBase[RoleModel, RoleBase, RoleBase]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Role]:
        return db.query(self.model).filter(self.model.name == name).first()

role = ServicesRole(RoleModel)