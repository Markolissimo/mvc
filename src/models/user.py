from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from .base import BaseModel
from pydantic import BaseModel as PydanticBaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    """SQLAlchemy model for User entity."""
    __tablename__ = "users"

    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    posts = relationship("Post", back_populates="user")

class UserCreate(PydanticBaseModel):
    """Pydantic model for user creation."""
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=8, description="User's password (min 8 characters)")

class UserLogin(PydanticBaseModel):
    """Pydantic model for user login."""
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., description="User's password")

class UserResponse(PydanticBaseModel):
    """Pydantic model for user response."""
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True 