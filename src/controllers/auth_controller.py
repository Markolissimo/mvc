from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import UserCreate, UserLogin
from ..services.user_service import UserService
from ..auth import get_current_user

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    """Sign up a new user."""
    # Check if user already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    new_user = UserService.create_user(db, user)
    return {"message": "User created successfully", "user_id": new_user.id}

@router.post("/login")
async def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """Login user and return JWT token."""
    token = UserService.authenticate_user(db, user_data.email, user_data.password)
    return {"access_token": token, "token_type": "bearer"} 