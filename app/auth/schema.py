from pydantic import BaseModel, ConfigDict, EmailStr

from app.user.schema import User

class AuthBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, arbitrary_types_allowed=True
    )

class VerifyUser(BaseModel):
    token: str
    email: EmailStr = None

class Login(AuthBase):
    access_token: str
    refresh_token: str
    user: User
    expires_in: int
    token_type: str = "Bearer"

class RefreshTokenRequest(BaseModel):
    refresh_token: str

class Email(BaseModel):
    email: EmailStr = None

class Reset(Email):
    token: str
    password: str