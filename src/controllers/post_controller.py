from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.post import PostCreate, PostResponse
from ..services.post_service import PostService
from ..auth import get_current_user
from typing import List

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    """Create a new post."""
    # Validate payload size (1MB limit)
    if len(post.text.encode('utf-8')) > 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Post content exceeds 1MB limit"
        )
    
    new_post = PostService.create_post(db, post, user_id)
    return new_post

@router.get("/", response_model=List[PostResponse])
async def get_posts(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    """Get all posts for the current user."""
    posts = PostService.get_user_posts(db, user_id)
    return posts

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    """Delete a post."""
    PostService.delete_post(db, post_id, user_id)
    return None 