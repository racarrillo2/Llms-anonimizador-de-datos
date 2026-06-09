import streamlit as st
import pandas as pd

from anonimizador import detectar, anonimizar


st.set_page_config(
    page_title="Anonimizador RGPD",
    page_icon="🔒"
)

st.title("🔒 Anonimizador de Datos Personales")

# -------------------------
# SELECCIÓN DE MODELO
# -------------------------

modelo = st.selectbox(
    "Selecciona el modelo",
    [
        "qwen3:4b",
        "granite4.1:3b",
        "gemma4:e2b"
    ]
)

# -------------------------
# ENTRADA DE TEXTO
# -------------------------

archivo = st.file_uploader(
    "Sube un archivo .txt",
    type=["txt"]
)

if archivo:
    texto = archivo.read().decode("utf-8")

    st.text_area(
        "Contenido cargado",
        value=texto,
        height=300,
        disabled=True
    )

else:
    texto = st.text_area(
        "Pega aquí el texto",
        height=300
    )

# -------------------------
# BOTÓN
# -------------------------

if st.button("Anonimizar"):

    if texto.strip() == "":
        st.warning("Introduce un texto")

    else:

        # AQUÍ ESTABA EL ERROR
        deteccion = detectar(
            texto,
            modelo
        )

        texto_limpio = anonimizar(
            texto,
            deteccion
        )

        # -------------------------
        # RESULTADO
        # -------------------------

        st.subheader("Texto anonimizado")

        st.text_area(
            "Resultado",
            value=texto_limpio,
            height=300,
            key="resultado"
        )

        # -------------------------
        # TABLA
        # -------------------------

        datos = []

        for entidad in deteccion.entidades:

            datos.append(
                {
                    "Tipo": entidad.tipo,
                    "Texto": entidad.texto
                }
            )

        df = pd.DataFrame(datos)

        st.subheader("Datos detectados")

        st.dataframe(
            df,
            use_container_width=True
        )

        # -------------------------
        # DESCARGA
        # -------------------------

        st.download_button(
            label="📥 Descargar resultado",
            data=texto_limpio,
            file_name="anonimizado.txt",
            mime="text/plain"
        )