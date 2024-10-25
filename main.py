# main.py
import uvicorn
from fastapi import FastAPI
from src.core.config import engine
from src.domain.models import Base
from src.presentation.api import router as item_router

app = FastAPI()

# Cria as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

# Registro das rotas
app.include_router(item_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
