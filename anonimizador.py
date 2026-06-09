from ollama import chat
from pydantic import BaseModel
from typing import Literal


# -------------------------
# MODELOS PYDANTIC
# -------------------------

class Entidad(BaseModel):
    tipo: Literal[
        "NOMBRE",
        "EMAIL",
        "TELEFONO",
        "DNI",
        "DIRECCION",
        "IBAN",
        "TARJETA"
    ]
    texto: str


class ResultadoPII(BaseModel):
    entidades: list[Entidad]


# -------------------------
# DETECCIÓN
# -------------------------

def detectar(texto, modelo):

    prompt = """
    Detecta datos personales en el texto.

    Categorías permitidas:
    - NOMBRE
    - EMAIL
    - TELEFONO
    - DNI
    - DIRECCION
    - IBAN
    - TARJETA

    Devuelve únicamente los datos encontrados.
    """

    respuesta = chat(
        model=modelo,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": texto
            }
        ],
        format=ResultadoPII.model_json_schema()
    )

    return ResultadoPII.model_validate_json(
        respuesta.message.content
    )


# -------------------------
# ANONIMIZACIÓN
# -------------------------

def anonimizar(texto, deteccion):

    texto_limpio = texto

    for entidad in deteccion.entidades:

        texto_limpio = texto_limpio.replace(
            entidad.texto,
            f"[{entidad.tipo}]"
        )

    return texto_limpio


# -------------------------
# PRUEBA LOCAL
# -------------------------

if __name__ == "__main__":

    with open(
        "ejemplo.txt",
        encoding="utf-8"
    ) as archivo:

        texto = archivo.read()

    deteccion = detectar(texto)

    print("\n--- ENTIDADES DETECTADAS ---\n")
    print(deteccion)

    texto_limpio = anonimizar(
        texto,
        deteccion
    )

    print("\n--- TEXTO ANONIMIZADO ---\n")
    print(texto_limpio)