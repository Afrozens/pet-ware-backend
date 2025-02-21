from sqlalchemy.orm import Session

from app.settings import get_settings
from app.role.model import Rol
from app.role.service import role
from app.seeders.roles import Role 

settings = get_settings()

def init_db(db: Session) -> None:
# Create Role If They Don't Exist
    premium_role = role.get_by_name(db=db, name=Role.PREMIUM["name"])
    if not premium_role:
        premium_role_in = Rol(
            name=Role.PREMIUM["name"], description=Role.PREMIUM["description"]
        )   
        role.create(db, obj_in=premium_role_in)

    client_role = role.get_by_name(db=db, name=Role.CLIENT["name"])
    if not client_role:
        user_role_in = Rol(
            name=Role.CLIENT["name"], description=Role.CLIENT["description"]
        )   
        role.create(db, obj_in=user_role_in)

    service_provisioner_role = role.get_by_name(db=db, name=Role.SERVICE["name"])
    if not service_provisioner_role:
        agent_role_in = Rol(
            name=Role.SERVICE["name"], description=Role.SERVICE["description"]
        )
        role.create(db, obj_in=agent_role_in)

    admin_role = role.get_by_name(db=db, name=Role.ADMINISTRATOR["name"])
    if not admin_role:
        admin_role_in = Rol(
            name=Role.ADMINISTRATOR["name"],
            description=Role.ADMINISTRATOR["description"],
        )
        role.create(db, obj_in=admin_role_in)