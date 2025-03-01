from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

from app.database import get_session
from app.client_services.controller import client_service as client_service_controller
from app.client_services.schema import ClientServiceUpdate, ClientServiceCreate, ClientService
from app.pagination import PaginateSchema

router = APIRouter()

@router.put('/update/{client_service_id}', status_code=status.HTTP_200_OK)
async def update_client_service(data: ClientServiceUpdate, client_service_id: str, session: Session = Depends(get_session)):
    await client_service_controller.put_update_client_service(db=session, obj_in=data, client_service_id=client_service_id)

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_client_service(data: ClientServiceCreate, session: Session = Depends(get_session)):
    await client_service_controller.post_create_client_service(db=session, obj_in=data)

@router.get('/all/{client_user_id}', status_code=status.HTTP_200_OK, response_model=PaginateSchema[ClientService])
async def get_client_services_paginate(
    client_user_id: str,
    session: Session = Depends(get_session),
    page: int = 1,
    limit: int = 10,
    filter: str = Query(None, alias="filter")):
    data = await client_service_controller.get_multi_services(db=session, page=page, limit=limit, filter=filter, client_user_id=client_user_id)
    return data

@router.delete('/{client_service_id}', status_code=status.HTTP_200_OK)
async def delete_client_service(client_service_id: str, session: Session = Depends(get_session)):
    await client_service_controller.delete_remove_client_service(db=session, client_service_id=client_service_id)