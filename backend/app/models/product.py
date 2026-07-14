from sqlalchemy import Column,Integer,String,Float,Boolean,DateTime
from sqlalchemy.sql import func
from app.core.database import Base
class Product(Base):
    __tablename__="products"
    id=Column(Integer,primary_key=True)
    name=Column(String(140),nullable=False)
    category=Column(String(80),default="Outros")
    cost=Column(Float,default=0)
    price=Column(Float,default=0)
    stock=Column(Float,default=0)
    min_stock=Column(Float,default=0)
    active=Column(Boolean,default=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
