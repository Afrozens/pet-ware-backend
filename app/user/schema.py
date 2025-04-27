from typing import Optional
from pydantic import UUID4, BaseModel

from app.client_user.schema import ClientUser
from app.role.schema import Role

class UserBase(BaseModel):
    profile_picture: UUID4
    email: str = None
    first_name: str = None
    last_name: str = None
    type_document: str = None
    document: str = None
    active: bool = False
    place_id: str = None
    whatsapp: bool = False
    phone_number: str = None
    address: str = None

class UserSaveConsumer(BaseModel):
    email: str
    password: str
    
class UserSaveClient(UserSaveConsumer):
    first_name: str = None
    last_name: str = None
    phone_number: str = None
    type_document: str = None
    document: str = None
    address: str = None
    place_id: str = None
    
class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDB(UserBase):
    id: UUID4 = None
    roles_id: UUID4 = None

    created_at: str = None
    verified_at: str = None
    deleted_at: str = None
    updated_at: str = None

class User(UserInDB):
    pass

class UserWithRelations(User):
    role: Optional[Role] = None
    client_user: Optional[ClientUser] = None
