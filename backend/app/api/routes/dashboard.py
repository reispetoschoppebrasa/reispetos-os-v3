from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.api.deps import current_user
from app.core.database import get_db
from app.models.product import Product
router=APIRouter(prefix="/dashboard",tags=["Dashboard"])
@router.get("")
def dashboard(user=Depends(current_user),db:Session=Depends(get_db)):
    products=db.query(Product).filter(Product.active==True).all()
    critical=[p for p in products if p.stock<=p.min_stock]
    return {"faturamento_hoje":0,"lucro_estimado":0,"mesas_abertas":0,"estoque_critico":len(critical),"produtos_ativos":len(products),"valor_estoque":sum((p.stock or 0)*(p.cost or 0) for p in products),"status":"Base v3 pronta para evolução"}
