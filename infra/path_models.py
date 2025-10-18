import os
from pydantic import BaseModel

class SettingGenero(BaseModel):
    MODEL_GENERO: str = os.getenv("MODEL_PATH", "models/genero_model/modelo_genero.pkl")
    

# instâncias separadas
setting_genero = SettingGenero()

