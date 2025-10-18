from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from api.reconhecimento_genero.reconhecimento_genero_model import SexPredictor
from api.reconhecimento_genero.reconhecimento_genero_service import process_file
from infra.path_models import setting_genero
import os

# Define o prefixo da rota
router = APIRouter()

# Carrega o modelo uma única vez na inicialização
model_path = setting_genero.MODEL_GENERO
_predictor = SexPredictor(model_path)

@router.post("", summary="Recebe CSV/Excel e devolve Excel com Sexo Validado e Status")
async def validar_arquivo(arquivo: UploadFile = File(...)):
    """
    Recebe um arquivo CSV ou Excel contendo colunas:
    Nome, Data de Nascimento, CPF, Sexo

    Retorna um Excel com as colunas adicionais:
    - Sexo Validado
    - Status
    """
    try:
        content = await arquivo.read()
        excel_bytes = process_file(content, _predictor)

        filename = (arquivo.filename or "saida").rsplit(".", 1)[0] + "_validado.xlsx"

        return StreamingResponse(
            iter([excel_bytes]),
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": f'attachment; filename="{filename}"'
            },
        )
    except Exception as e:
        # Mostra detalhes no log do servidor para debug
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=f"Erro ao processar: {e}")
