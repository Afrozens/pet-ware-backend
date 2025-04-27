from uuid import uuid4
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models import BaseModel
from app.user.model import User

class Rol(BaseModel):
    __tablename__ = 'roles'

    id = Column(
        UUID(as_uuid=True), primary_key=True,  index=True, default=uuid4)
    name = Column(String(100), index=True)
    description = Column(Text)

    #relaciones
    users = relationship('User', back_populates="role", uselist=False)
