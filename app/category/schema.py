from typing import Optional
from pydantic import UUID4, BaseModel

class CategoryBase(BaseModel):
    name: str = None
    description: str = None

class CategorySave(CategoryBase):
    pass

class CategoryInDB(CategoryBase):
    id: UUID4 = None

    created_at: str = None
    deleted_at: Optional[str] = None

class Category(CategoryInDB):
    pass

class CategoryWithServices(CategoryInDB):
    # client_services: Optional
    pass