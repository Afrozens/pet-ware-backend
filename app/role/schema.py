from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel

class RoleBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class RoleInDBBase(RoleBase):
    id: UUID4

    created_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class RoleUpdate(BaseModel):
    role: str = None
    
class Role(RoleInDBBase):
    pass