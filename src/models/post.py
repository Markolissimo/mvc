from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import BaseModel
from pydantic import BaseModel as PydanticBaseModel, Field
from typing import Optional

class Post(BaseModel):
    """SQLAlchemy model for Post entity."""
    __tablename__ = "posts"

    text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="posts")

class PostCreate(PydanticBaseModel):
    """Pydantic model for post creation."""
    text: str = Field(..., max_length=1000000, description="Post content (max 1MB)")

class PostResponse(PydanticBaseModel):
    """Pydantic model for post response."""
    id: int
    text: str
    user_id: int
    created_at: str

    class Config:
        from_attributes = True 