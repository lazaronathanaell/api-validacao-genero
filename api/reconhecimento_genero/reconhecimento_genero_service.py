import io
import re
import tempfile
import pandas as pd
from pathlib import Path

from api.reconhecimento_genero.reconhecimento_genero_model import SexPredictor
from api.reconhecimento_genero.status_enum import Status

_MAP = {
    "M": "M", "MASC": "M", "MASCULINO": "M",
    "F": "F", "FEM": "F", "FEMININO": "F",
}

def _norm_sexo(x):
    if x is None:
        return None
    v = re.sub(r"[^A-Za-z]", "", str(x).strip().upper())
    return _MAP.get(v)

def _read_table(file_bytes: bytes) -> pd.DataFrame:
    try:
        return pd.read_excel(io.BytesIO(file_bytes))
    except Exception:
        pass
    try:
        return pd.read_csv(io.BytesIO(file_bytes))
    except Exception:
        return pd.read_csv(io.BytesIO(file_bytes), encoding="latin-1", sep=";")

def process_file(file_bytes: bytes, predictor: SexPredictor) -> bytes:
    df = _read_table(file_bytes)

    if "Nome" not in df.columns:
        raise ValueError("Planilha precisa ter a coluna 'Nome'.")
    if "Sexo" not in df.columns:
        df["Sexo"] = None

    out = df.copy()

    out["Primeiro Nome"] = out["Nome"].apply(predictor.first_name)
    out["Modelo (M/F/U)"] = out["Primeiro Nome"].apply(predictor.classify)

    out["_Sexo_In"] = out["Sexo"].apply(_norm_sexo)

    sexo_validado, status = [], []
    for entrada, pred in zip(out["_Sexo_In"], out["Modelo (M/F/U)"]):
        if pred == "U":
            sexo_validado.append("UNISSEX")
            status.append(Status.VALIDAR.value)
        else:
            if entrada is None:
                sexo_validado.append(pred)
                status.append(Status.CORRIGIR.value)
            elif entrada == pred:
                sexo_validado.append(pred)
                status.append(Status.CERTO.value)
            else:
                sexo_validado.append(pred)
                status.append(Status.CORRIGIR.value)

    out["Sexo Validado"] = sexo_validado
    out["Status"] = status
    out = out.drop(columns=["_Sexo_In", "Primeiro Nome", "Modelo (M/F/U)"])

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir) / "tabela_validada.xlsx"
        with pd.ExcelWriter(tmp_path, engine="xlsxwriter") as writer:
            out.to_excel(writer, index=False)

        with open(tmp_path, "rb") as f:
            excel_bytes = f.read()

    return excel_bytes
