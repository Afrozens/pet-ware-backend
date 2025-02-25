from uuid import uuid4
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    id = Column(
        UUID(as_uuid=True), primary_key=True,  index=True, default=uuid4)
    roles_id = Column(UUID(as_uuid=True), ForeignKey('roles.id'))
    
    profile_picture = Column(UUID(as_uuid=True), nullable=True)
    email = Column(String(150), unique=True)
    first_name = Column(String(150), nullable=True)
    last_name = Column(String(150), nullable=True)
    document = Column(String(150), nullable=True)
    type_document = Column(String(50), nullable=True)
    phone_number = Column(String(20), nullable=True)
    active = Column(Boolean, default=False)
    address = Column(String(150), nullable=True)
    place_id = Column(String(150), nullable=True)
    whatsapp = Column(Boolean, default=False)
    password = Column(String(100))

    verified_at = Column(DateTime, nullable=True, default=None)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)

    #relaciones
    role = relationship('Rol', back_populates="users", uselist=False)
    client_user = relationship('ClientUser', back_populates="user", uselist=False)
    files = relationship("File", back_populates="user")
    client_review_services = relationship('ClientReviewService', back_populates="user")
    user_service_get = relationship('UserServiceGet', back_populates="user")
    user_history_payment = relationship('UserHistoryPayment', back_populates="user")

