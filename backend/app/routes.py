from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import User, LearnerProfile
from schemas import UserRegister, UserLogin, Token, LearnerProfileCreate, LearnerProfileResponse
from auth import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/auth/register", response_model=Token)
def register(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed = hash_password(user.password)
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password_hash=hashed,
        role_id=user.role_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    token = create_access_token({"sub": new_user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/auth/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/profile/create", response_model=LearnerProfileResponse)
def create_profile(profile: LearnerProfileCreate, db: Session = Depends(get_db)):
    new_profile = LearnerProfile(
        user_id=1,
        learning_level=profile.learning_level,
        preferred_language=profile.preferred_language,
        learning_goals=profile.learning_goals
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile