from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel

class ClientFrenquentlyAskedQuestionsBase(BaseModel):
    description: str = None
    title: str = None
    
class ClientFrenquentlyAskedQuestionsCreate(ClientFrenquentlyAskedQuestionsBase):
    client_id: UUID4 = None

class ClientFrenquentlyAskedQuestionsUpdate(ClientFrenquentlyAskedQuestionsBase):
    pass

class ClientFrenquentlyAskedQuestionsInDBBase(ClientFrenquentlyAskedQuestionsBase):
    id: UUID4
    client_id: UUID4

    created_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        from_attributes = True

class ClientFrenquentlyAskedQuestions(ClientFrenquentlyAskedQuestionsInDBBase):
    pass
