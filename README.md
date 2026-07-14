# REI'SPETOS OS v3 — Marco 1

Base modular com FastAPI, React/Vite, autenticação JWT, dashboard, produtos e suporte a PostgreSQL via DATABASE_URL.

## Render
Root Directory: backend
Build: pip install -r requirements.txt
Start: uvicorn app.main:app --host 0.0.0.0 --port $PORT

## Vercel
Root Directory: frontend
Variável: VITE_API_URL=https://SEU-BACKEND.onrender.com

Login: admin / 1234
