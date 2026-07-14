from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base,engine,SessionLocal
from app.core.config import APP_NAME,CORS_ORIGINS
from app.core.security import hash_password
from app.models.user import User
from app.models.product import Product
from app.api.routes import auth,dashboard,products
app=FastAPI(title=f"{APP_NAME} API",version="3.0.0")
app.add_middleware(CORSMiddleware,allow_origins=CORS_ORIGINS,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    db=SessionLocal()
    try:
        if not db.query(User).filter(User.username=="admin").first(): db.add(User(username="admin",password_hash=hash_password("1234"),role="admin"))
        if db.query(Product).count()==0:
            db.add_all([Product(name="Espeto de Carne",category="Espetos",cost=4.5,price=8,stock=50,min_stock=15),Product(name="Chopp 500ml",category="Bebidas",cost=3.8,price=10,stock=80,min_stock=20),Product(name="Pão de Alho",category="Espetos",cost=3,price=10,stock=30,min_stock=10)])
        db.commit()
    finally: db.close()
@app.get("/health")
def health(): return {"ok":True,"system":APP_NAME,"version":"3.0.0"}
app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(products.router)
