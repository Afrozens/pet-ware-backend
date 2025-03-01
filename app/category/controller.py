from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.service import CRUDBase
from app.category.model import Category
from app.category.schema import CategorySave
from app.utils.paginate import converted_paginate_data

class ControllerCategory(CRUDBase[Category, CategorySave, CategorySave]):
    async def get_multi_categories(self, db: Session, *, page: int, limit: int, filter: str):
        try:
            base_query = db.query(self.model).where(self.model.deleted_at == None).order_by(self.model.name.asc())
            
            if filter is not None and filter != "null":
                search = f"%{filter}%"
                query_search = base_query.filter(self.model.name.like((search)))
            else:
                query_search = base_query
            return converted_paginate_data(page, limit, query_search)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e)

category = ControllerCategory(Category)
