from uuid import uuid4
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models import BaseModel

class Category(BaseModel):
    __tablename__ = 'categories'

    id = Column(
        UUID(as_uuid=True), primary_key=True,  index=True, default=uuid4)
    name = Column(String(100), index=True)
    description = Column(Text)

    # relations
    client_services = relationship('ClientService', back_populates="category")

