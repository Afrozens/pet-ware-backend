from datetime import timedelta
from fastapi.responses import JSONResponse
import logging

from app.settings import get_settings
from app.auth.config import generate_token, str_encode
from app.auth.utils import unique_string

settings = get_settings()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def _generate_tokens(user):
    refresh_key = unique_string(100)
    access_key = unique_string(50)
    
    access_token_expires = timedelta(minutes=15)
    refresh_token_expires = timedelta(days=5)

    at_payload = {
        "sub": str_encode(str(user.id)),
        'a': access_key,
    }

    access_token = generate_token(at_payload, settings.JWT_SECRET, access_token_expires)

    refresh_token_payload = {
        "sub": str_encode(str(user.id)),
        "t": refresh_key,
        'a': access_key
    }
    refresh_token = generate_token(refresh_token_payload, settings.SECRET_KEY, refresh_token_expires)
    
    content = {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": access_token_expires.seconds,
    }
    
    response = JSONResponse(content=content)
   
    return response