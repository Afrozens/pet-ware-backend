from uuid import uuid4
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Text, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models import BaseModel

class UserHistoryPayment(BaseModel):
    __tablename__ = 'user_history_payments'

    id = Column(
        UUID(as_uuid=True), primary_key=True,  index=True, default=uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey('clients_users.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user_service_get = Column(UUID(as_uuid=True), ForeignKey('user_service_gets.id'))
    file_id = Column(UUID(as_uuid=True), ForeignKey('files.id'), nullable=True)
    history_payment_id = Column(UUID(as_uuid=True), ForeignKey('history_payments.id'))
    
    status = Column(String(50))
    concept = Column(String(150), nullable=True)
    reference = Column(String(50), nullable=True)
    dates = Column(String(150), nullable=True)

    #relaciones
    history_payment = relationship('HistoryPayment', back_populates="user_history_payment", uselist=False)
    file = relationship('File', back_populates="user_history_payment", uselist=False)
    user = relationship('User', back_populates="user_history_payment", uselist=False)
    client_user = relationship('ClientUser', back_populates="user_history_payment", uselist=False)
    user_service_get = relationship('UserServiceGet', back_populates="user_history_payment", uselist=False)