from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

from app.database import get_session
from app.category.controller import category as category_controller
from app.category.schema import Category
from app.pagination import PaginateSchema

router = APIRouter()

@router.get('/all', status_code=status.HTTP_200_OK, response_model=PaginateSchema[Category])
async def get_categories_paginate(
    session: Session = Depends(get_session),
    page: int = 1,
    limit: int = 10,
    filter: str = Query(None, alias="filter")):
    data = await category_controller.get_multi_categories(db=session, page=page, limit=limit, filter=filter)
    return data