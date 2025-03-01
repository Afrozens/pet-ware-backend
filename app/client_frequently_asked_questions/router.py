from typing import List
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

from app.client_frequently_asked_questions.schema import ClientFrenquentlyAskedQuestions, ClientFrenquentlyAskedQuestionsCreate, ClientFrenquentlyAskedQuestionsUpdate
from app.database import get_session
from app.client_frequently_asked_questions.controller import frequently_asked as frequently_asked_controller

router = APIRouter()

@router.put('/update/{frequently_asked_id}', status_code=status.HTTP_200_OK)
async def update_frequently_asked(data: ClientFrenquentlyAskedQuestionsUpdate, frequently_asked_id: str, session: Session = Depends(get_session)):
    await frequently_asked_controller.put_update_frequently_asked(db=session, obj_in=data, frequently_asked_id=frequently_asked_id)

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_frequently_asked(data: ClientFrenquentlyAskedQuestionsCreate, session: Session = Depends(get_session)):
    await frequently_asked_controller.post_create_frequently_asked(db=session, obj_in=data)

@router.get('/all/{client_user_id}', status_code=status.HTTP_200_OK, response_model=List[ClientFrenquentlyAskedQuestions])
async def get_frequently_askeds(
    client_user_id: str,
    session: Session = Depends(get_session)):
    data = await frequently_asked_controller.get_frequently_askeds_all(db=session, client_user_id=client_user_id)
    return data

@router.delete('/{frequently_asked_id}', status_code=status.HTTP_200_OK)
async def delete_frequently_asked(frequently_asked_id: str, session: Session = Depends(get_session)):
    await frequently_asked_controller.delete_remove_frequently_asked(db=session, frequently_asked_id=frequently_asked_id)