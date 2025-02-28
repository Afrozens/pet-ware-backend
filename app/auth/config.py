from passlib.context import CryptContext
from datetime import datetime, timedelta
import base64, jwt, logging

from app.settings import get_settings
from app.user.model import User

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
settings = get_settings()
ALGORITHM = "HS256"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_hash_password(password: str) -> str: 
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def str_encode(string: str) -> str:
    return base64.b85encode(string.encode('utf-8')).decode('utf-8')

def str_decode(string: str) -> str:
    return base64.b85decode(string.encode('utf-8')).decode('utf-8')

def get_token_payload(token: str, secret: str):
    payload = jwt.decode(token, secret, algorithms=ALGORITHM)
    return payload

def generate_token(payload: dict, secret: str, expiry: timedelta):
    expire = datetime.now() + expiry
    payload.update({"exp": expire})
    return jwt.encode(payload, secret, algorithm=ALGORITHM)

async def get_refresh_user(token: str, db):
    payload = get_token_payload(token, settings.SECRET_KEY)
    if payload: 
            user_id = str_decode(str(payload.get('sub')))
            user = db.query(User).filter(User.id == user_id).where(User.deleted_at == None).first()
            if user: 
                return user
    return None

async def get_token_user(token: str, db):
    payload = get_token_payload(token, settings.JWT_SECRET)
    if payload: 
        user_id = str_decode(str(payload.get('sub')))
        user = db.query(User).filter(User.id == user_id).where(User.deleted_at == None).first()
        if user: 
            return user
    return None