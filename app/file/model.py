from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models import BaseModel
from app.user_history_payment.model import UserHistoryPayment
from app.history_payment.model import HistoryPayment

class File(BaseModel):
    __tablename__ = 'files'

    id = Column(
        UUID(as_uuid=True), primary_key=True,  index=True, default=uuid4
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))

    name = Column(String(150))
    path = Column(String(255))
    ext = Column(String(255))
    size = Column(Integer)
    folder = Column(String(255))

    # relations
    user = relationship("User", back_populates="files", uselist=False)
    user_history_payment = relationship('UserHistoryPayment', back_populates="file", uselist=False)
    history_payment = relationship('HistoryPayment', back_populates="file", uselist=False)

