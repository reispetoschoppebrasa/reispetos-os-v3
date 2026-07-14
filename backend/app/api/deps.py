from fastapi import Depends,HTTPException
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from jose import jwt,JWTError
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.config import SECRET_KEY,ALGORITHM
from app.models.user import User
bearer=HTTPBearer(auto_error=False)
def current_user(credentials:HTTPAuthorizationCredentials=Depends(bearer),db:Session=Depends(get_db)):
    if not credentials: raise HTTPException(401,"Não autenticado")
    try: username=jwt.decode(credentials.credentials,SECRET_KEY,algorithms=[ALGORITHM]).get("sub")
    except JWTError: raise HTTPException(401,"Token inválido")
    user=db.query(User).filter(User.username==username,User.active==True).first()
    if not user: raise HTTPException(401,"Usuário inválido")
    return user
