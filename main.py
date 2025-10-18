from fastapi import FastAPI
from api.reconhecimento_genero.reconhecimento_genero_router import router as reconhecimento_genero_router

app = FastAPI(
    title="API de Reconhecimento",
    version="1.0"
)

app.include_router(reconhecimento_genero_router, prefix="/validar", tags=["Reconhecimento de Gênero"])
