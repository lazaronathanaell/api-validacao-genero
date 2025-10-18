from enum import Enum

class Status(str, Enum):
    CERTO = "CERTO"
    CORRIGIR = "CORRIGIR"
    VALIDAR = "VALIDAR"
