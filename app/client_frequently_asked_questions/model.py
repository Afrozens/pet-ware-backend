from uuid import uuid4
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models import BaseModel

class ClientFrequentlyAskedQuestions(BaseModel):
    __tablename__ = 'clients_frequently_asked_questions'

    id = Column(
        UUID(as_uuid=True), primary_key=True,  index=True, default=uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey('clients_users.id'), nullable=True)
    
    title = Column(String(150))
    description = Column(Text)

    #relaciones
    client_user = relationship('ClientUser', back_populates="frequently_askeds", uselist=False)

