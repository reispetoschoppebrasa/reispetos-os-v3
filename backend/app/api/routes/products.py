from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.api.deps import current_user
from app.core.database import get_db
from app.models.product import Product
router=APIRouter(prefix="/products",tags=["Produtos"])
@router.get("")
def list_products(user=Depends(current_user),db:Session=Depends(get_db)):
    return db.query(Product).filter(Product.active==True).order_by(Product.name).all()
