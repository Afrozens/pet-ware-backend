from typing import Optional
from pydantic import UUID4, BaseModel

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

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDB(UserBase):
    id: UUID4 = None
    roles_id: UUID4 = None

    created_at: str = None
    verified_at: Optional[str] = None
    deleted_at: Optional[str] = None
    updated_at: Optional[str] = None

class User(UserInDB):
    pass