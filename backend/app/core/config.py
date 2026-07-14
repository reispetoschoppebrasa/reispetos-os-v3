import os
APP_NAME=os.getenv("APP_NAME","REI'SPETOS OS")
SECRET_KEY=os.getenv("SECRET_KEY","troque-esta-chave-em-producao")
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=720
DATABASE_URL=os.getenv("DATABASE_URL","sqlite:///./reispetos_v3.db")
CORS_ORIGINS=[x.strip() for x in os.getenv("CORS_ORIGINS","http://localhost:5173,https://reispetos-os-v3.vercel.app").split(",") if x.strip()]
