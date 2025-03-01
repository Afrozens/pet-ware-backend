from pydantic import UUID4
from fastapi import HTTPException

def user_verified_id(id: UUID4):
    if not id:
        raise HTTPException(status_code=404, detail='user-not-found')
    return id
