from sqlalchemy.orm import Session

from app.settings import get_settings
from app.role.model import Rol
from app.role.service import role
from app.seeders.roles import Role 

settings = get_settings()

def init_db(db: Session) -> None:
# Create Role If They Don't Exist
    client_role = role.get_by_name(db=db, name=Role.CLIENT["name"])
    if not client_role:
        client_role_in = Rol(
            name=Role.CLIENT["name"], description=Role.CLIENT["description"]
        )   
        role.create(db, obj_in=client_role_in)

    professional_role = role.get_by_name(db=db, name=Role.PROFESSIONAL["name"])
    if not professional_role:
        professional_role_in = Rol(
            name=Role.PROFESSIONAL["name"], description=Role.PROFESSIONAL["description"]
        )
        role.create(db, obj_in=professional_role_in)

    admin_role = role.get_by_name(db=db, name=Role.ADMINISTRATOR["name"])
    if not admin_role:
        admin_role_in = Rol(
            name=Role.ADMINISTRATOR["name"],
            description=Role.ADMINISTRATOR["description"],
        )
        role.create(db, obj_in=admin_role_in)