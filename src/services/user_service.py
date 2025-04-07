from sqlalchemy.orm import Session
from ..models.user import User, UserCreate
from ..auth import get_password_hash, verify_password, create_access_token
from datetime import timedelta
from fastapi import HTTPException, status

class UserService:
    """Service layer for user-related operations."""
    
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        """Create a new user in the database."""
        db_user = User(
            email=user.email,
            password_hash=get_password_hash(user.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> str:
        """Authenticate user and return JWT token."""
        user = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"sub": str(user.id)}, expires_delta=access_token_expires
        )
        return access_token

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User:
        """Get user by ID."""
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user 