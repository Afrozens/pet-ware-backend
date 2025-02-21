from pydantic import BaseModel
from typing import Generic, TypeVar, List

T = TypeVar('T')

class PaginateSchema(BaseModel, Generic[T]):
    page_number: int = None
    page_size: int = None
    total_pages: int = None
    total_record: int = None
    data: List[T] = None