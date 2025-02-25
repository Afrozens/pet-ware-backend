from uuid import uuid4
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models import BaseModel

class ClientUser(BaseModel):
    __tablename__ = 'clients_users'

    id = Column(
        UUID(as_uuid=True), primary_key=True,  index=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=True)
    
    description = Column(Text)
    type_document = Column(String(50), nullable=True)
    document = Column(String(150), nullable=True)
    premium = Column(Boolean, default=False)
    experience = Column(Text)

    #relaciones
    user = relationship('User', back_populates="client_user", uselist=False)
    frequently_askeds = relationship('ClientFrequentlyAskedQuestions', back_populates="client_user")
    client_services = relationship('ClientService', back_populates="client_user")
    client_review_services = relationship('ClientReviewService', back_populates="client_user")
    user_service_get = relationship('UserServiceGet', back_populates="client_user")
    user_history_payment = relationship('UserHistoryPayment', back_populates="client_user")
