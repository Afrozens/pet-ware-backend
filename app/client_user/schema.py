from datetime import datetime
from typing import Optional, List
from pydantic import UUID4, BaseModel

from app.client_frequently_asked_questions.schema import ClientFrenquentlyAskedQuestions
from app.client_services.schema import ClientService

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

class ClientUserWithRelations(ClientUser):
    frequently_askeds: Optional[List[ClientFrenquentlyAskedQuestions]] = None
    client_services: Optional[List[ClientService]] = None
