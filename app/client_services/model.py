from uuid import uuid4
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Text, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models import BaseModel
from app.client_user.model import ClientUser
from app.user_service_get.model import UserServiceGet

class ClientService(BaseModel):
    __tablename__ = 'clients_services'

    id = Column(
        UUID(as_uuid=True), primary_key=True,  index=True, default=uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey('clients_users.id'), nullable=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), nullable=True)
    
    active = Column(Boolean, default=False)
    price_hour = Column(Integer)
    details = Column(Text)
    icon = Column(String(50), nullable=True)
    delivery = Column(Boolean, default=False)
    day_week = Column(ARRAY(String(5)))
    range_hours = Column(String(50))
    location = Column(String(150))
    place_id = Column(String(150))

    #relaciones
    client_user = relationship('ClientUser', back_populates="client_services", uselist=False)
    category = relationship('Category', back_populates="client_services", uselist=False)
    user_service_get = relationship('UserServiceGet', back_populates="client_services")
