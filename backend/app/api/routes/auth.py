from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import verify_password,create_access_token
from app.models.user import User
from app.schemas.auth import LoginIn,TokenOut
router=APIRouter(prefix="/auth",tags=["Autenticação"])
@router.post("/login",response_model=TokenOut)
def login(data:LoginIn,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.username==data.username,User.active==True).first()
    if not user or not verify_password(data.password,user.password_hash): raise HTTPException(401,"Usuário ou senha inválidos")
    token=create_access_token(user.username,user.role)
    return {"access_token":token,"user":{"username":user.username,"role":user.role}}
