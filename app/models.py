from sqlalchemy import func, Column, DateTime
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.hybrid import hybrid_property

from app.database import Base

class BaseModel(Base):
    __abstract__ = True

    created_at = Column(TIMESTAMP(timezone=True), nullable=True, server_default=func.timezone('America/Bogota', func.now()), index=True)
    deleted_at = Column(DateTime, nullable=True, default=None)

    # soft delete
    @hybrid_property
    def is_deleted(self):
        return self.deleted_at is not None

    @is_deleted.expression
    def is_deleted(cls):
        return cls.deleted_at.isnot(None)

    def soft_delete(self):
        self.deleted_at = func.now()