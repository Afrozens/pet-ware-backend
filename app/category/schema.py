from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel

class CategoryBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class CategoryInDBBase(CategoryBase):
    id: UUID4
    created_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class CategoryUpdate(BaseModel):
    role: str = None
    
class Category(CategoryInDBBase):
    pass