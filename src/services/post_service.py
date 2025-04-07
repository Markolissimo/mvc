from sqlalchemy.orm import Session
from ..models.post import Post, PostCreate
from ..models.user import User
from fastapi import HTTPException, status
from cachetools import TTLCache
from datetime import datetime, timedelta

class PostService:
    """Service layer for post-related operations."""
    
    _posts_cache = TTLCache(maxsize=100, ttl=300)

    @staticmethod
    def create_post(db: Session, post: PostCreate, user_id: int) -> Post:
        """Create a new post for a user."""
        db_post = Post(
            text=post.text,
            user_id=user_id
        )
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

    @staticmethod
    def get_user_posts(db: Session, user_id: int) -> list[Post]:
        """Get all posts for a user with caching."""
        cache_key = f"user_posts_{user_id}"
        
        cached_posts = PostService._posts_cache.get(cache_key)
        if cached_posts is not None:
            return cached_posts

        posts = db.query(Post).filter(Post.user_id == user_id).all()
        
        PostService._posts_cache[cache_key] = posts
        return posts

    @staticmethod
    def delete_post(db: Session, post_id: int, user_id: int) -> bool:
        """Delete a post if it belongs to the user."""
        post = db.query(Post).filter(
            Post.id == post_id,
            Post.user_id == user_id
        ).first()
        
        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found or not authorized"
            )
        
        db.delete(post)
        db.commit()
        
        cache_key = f"user_posts_{user_id}"
        PostService._posts_cache.pop(cache_key, None)
        
        return True 