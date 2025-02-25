from uuid import uuid4
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Text, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models import BaseModel

class ClientReviewService(BaseModel):
    __tablename__ = 'clients_reviews_services'

    id = Column(
        UUID(as_uuid=True), primary_key=True,  index=True, default=uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey('clients_users.id'), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=True)
    
    description = Column(Text)
    title = Column(String(150))
    rating = Column(Integer)
    active = Column(Boolean, default=False)

    #relaciones
    client_user = relationship('ClientUser', back_populates="client_review_services", uselist=False)
    user = relationship('User', back_populates="client_review_services", uselist=False)