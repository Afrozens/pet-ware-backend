from uuid import uuid4
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Text, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models import BaseModel

class UserServiceGet(BaseModel):
    __tablename__ = 'user_service_gets'

    id = Column(
        UUID(as_uuid=True), primary_key=True,  index=True, default=uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey('clients_users.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    client_services_id = Column(UUID(as_uuid=True), ForeignKey('clients_services.id'))
    
    conclude = Column(Boolean, default=False)
    note = Column(Text)
    date = Column(String(150))
    total_price = Column(Integer)
    total_hour = Column(Integer)

    #relaciones
    client_user = relationship('ClientUser', back_populates="user_service_get", uselist=False)
    user = relationship('User', back_populates="user_service_get", uselist=False)
    client_services = relationship('ClientService', back_populates="user_service_get", uselist=False)
    user_history_payment = relationship('UserHistoryPayment', back_populates="user_service_get", uselist=False)
