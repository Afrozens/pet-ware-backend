from typing import Optional, List
from pydantic import UUID4, BaseModel

class ClientServiceBase(BaseModel):
    active: bool = False
    details: str = None
    price_hour: int = None
    icon: str = None
    delivery: bool = False
    day_week: List[str] = None
    range_hours: str = None
    location: str = None
    place_id: str = None

class ClientServiceCreate(ClientServiceBase):
    client_id: UUID4 = None
    category_id: UUID4 = None

class ClientServiceUpdate(ClientServiceBase):
    category_id: UUID4 = None

class ClientServiceInDB(ClientServiceBase):
    id: UUID4 = None
    client_id: UUID4 = None
    category_id: UUID4 = None

    created_at: str = None
    deleted_at: Optional[str] = None

class ClientService(ClientServiceInDB):
    pass