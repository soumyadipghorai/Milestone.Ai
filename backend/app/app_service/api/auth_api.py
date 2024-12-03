from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.db_models import *
from app_service.schema.auth_schema import UserRegistration, UserLogin
from models.database import get_db   
from utils.auth_utils import * 
from utils.db_operations import * 
from fastapi.security import OAuth2PasswordRequestForm
from uuid import uuid4
from _temp.config import ROLE_MAPPING
 
router = APIRouter(prefix="/v1", tags=["Registers an admin into the database"])

@router.post("/register-user")
def register_admin(user: UserRegistration, db: Session = Depends(get_db)): 
    Table = ROLE_MAPPING[user.role.lower()] 
    existing_user = db.query(Table).filter(Table.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    if user.role == "student" :
        new_user = Table( 
            id = str(uuid4()), name = user.name, email = user.email, 
            github_username = user.github_username, password = hash_password(user.password),
        )
    else : 
        new_user = Table( 
            id = str(uuid4()), name = user.name, email = user.email,
            password = hash_password(user.password)
        )
    
    return add_entry(entry = new_user, success_key="id", success_value= new_user.id)
 

@router.post("/user-login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    Table = ROLE_MAPPING[user.role.lower()] 
    db_user = db.query(Table).filter(Table.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.id})
    return {"access_token": access_token, "token_type": "bearer", "user_id" : db_user.id, "role" : user.role.lower()}
