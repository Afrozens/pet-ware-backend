from typing import Optional
from datetime import datetime
from pydantic import UUID4, BaseModel

class FileBase(BaseModel):
    name: str = None
    path: str = None
    ext: str = None
    folder: str = None
    size: int = None

class FileSave(FileBase):
    user_id: UUID4

class FileInDBBase(FileBase):
    id: UUID4

    created_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class File(FileInDBBase):
    pass