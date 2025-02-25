from uuid import uuid4
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Text, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models import BaseModel

class HistoryPayment(BaseModel):
    __tablename__ = 'history_payments'

    id = Column(
        UUID(as_uuid=True), primary_key=True,  index=True, default=uuid4)
    file_id = Column(UUID(as_uuid=True), ForeignKey('files.id'))
    
    bank_code = Column(String(150))
    reference = Column(String(150))
    dates = Column(String(150))
    concept = Column(String(150))

    #relaciones
    user_history_payment = relationship('UserHistoryPayment', back_populates="history_payment", uselist=False)
    file = relationship('File', back_populates="history_payment", uselist=False)
