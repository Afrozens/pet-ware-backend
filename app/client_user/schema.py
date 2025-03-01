from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel

class ClientUserBase(BaseModel):
    description: str = None
    premium: bool = False
    experience: str = None
    active: bool = False

    verified_at: Optional[datetime] = None
    
class ClientUserSave(BaseModel):
    user_id: UUID4
    active: bool = False
    premium: bool = False

class ClientUserUpdate(ClientUserBase):
    pass

class ClientUserInDBBase(ClientUserBase):
    id: UUID4
    user_id: UUID4

    created_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        from_attributes = True

class ClientUser(ClientUserInDBBase):
    pass
