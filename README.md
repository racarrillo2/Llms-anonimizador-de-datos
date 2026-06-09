# 🔒 Anonimizador de Datos Personales (RGPD)

## Descripción

Este proyecto implementa una aplicación web local para la detección y anonimización de datos personales (PII - Personally Identifiable Information) utilizando modelos de lenguaje ejecutados localmente mediante Ollama.

La aplicación permite procesar textos que contienen información sensible y reemplazar automáticamente los datos personales por etiquetas genéricas antes de enviar o almacenar la información.

Todo el procesamiento se realiza de forma local, sin utilizar servicios externos ni APIs de terceros, cumpliendo así con requisitos de privacidad y protección de datos.

---

## Objetivo

Permitir la anonimización de información sensible presente en:

* Correos electrónicos
* Tickets de soporte
* Historiales de incidencias
* Documentos de atención al cliente
* Cualquier texto con datos personales

---

## Tecnologías utilizadas

* Python 3.12
* Streamlit
* Ollama
* Qwen3 4B
* Pydantic
* Pandas

---

## Arquitectura del proyecto

El proyecto está dividido en dos partes:

### Lógica de negocio

Archivo:

```text
anonimizador.py
```

Responsabilidades:

* Definir los modelos Pydantic
* Detectar datos personales mediante Ollama
* Validar la salida estructurada
* Anonimizar el texto sustituyendo los datos detectados

### Interfaz web

Archivo:

```text
app.py
```

Responsabilidades:

* Mostrar la interfaz Streamlit
* Permitir introducir texto o cargar archivos
* Mostrar el texto anonimizado
* Mostrar la tabla de entidades detectadas
* Permitir descargar el resultado

---

## Estructura del proyecto

```text
LLSM/
│
├── app.py
├── anonimizador.py
├── ejemplo.txt
├── requirements.txt
├── README.md
│
└── datos/
    └── resultados.txt
```

---

## Categorías detectadas

La aplicación detecta las siguientes entidades:

* NOMBRE
* EMAIL
* TELEFONO
* DNI
* DIRECCION
* IBAN
* TARJETA

Estas categorías están definidas mediante `Literal` de Pydantic para evitar categorías inventadas por el modelo.

---

## Funcionamiento

### 1. Detección

El texto se envía al modelo local de Ollama.

El modelo devuelve una salida estructurada con:

```json
{
  "entidades": [
    {
      "tipo": "EMAIL",
      "texto": "juan@gmail.com"
    }
  ]
}
```

### 2. Validación

La respuesta se valida mediante modelos Pydantic.

### 3. Anonimización

El código Python reemplaza cada entidad detectada por una etiqueta.

Ejemplo:

```text
Juan Pérez escribió a juan@gmail.com
```

Resultado:

```text
[NOMBRE] escribió a [EMAIL]
```

### 4. Presentación

La aplicación muestra:

* Texto anonimizado
* Tabla de entidades detectadas
* Botón de descarga

---

## Instalación

### Clonar o descargar el proyecto

Ubicarse en la carpeta del proyecto.

### Crear entorno virtual

```bash
python -m venv venv312
```

### Activar entorno virtual

Windows:

```bash
venv312\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Instalación de Ollama

Descargar e instalar Ollama:

https://ollama.com

Descargar el modelo:

```bash
ollama pull qwen3:4b
```

Verificar modelos instalados:

```bash
ollama list
```

---

## Ejecución

### Iniciar Ollama

```bash
ollama serve
```

### Ejecutar Streamlit

```bash
streamlit run app.py
```

---

## Uso

1. Seleccionar el modelo.
2. Pegar texto o cargar un archivo `.txt`.
3. Pulsar **Anonimizar**.
4. Revisar el resultado.
5. Descargar el texto anonimizado.

---

## Ejemplo

Entrada:

```text
Hola, soy Juan Pérez.

Mi email es juan@gmail.com.

Mi teléfono es 612345678.
```

Salida:

```text
Hola, soy [NOMBRE].

Mi email es [EMAIL].

Mi teléfono es [TELEFONO].
```

---

## Ventajas de esta solución

* Procesamiento 100% local.
* No se envían datos a servicios externos.
* Compatible con RGPD.
* Salida validada mediante Pydantic.
* Fácil de extender con nuevas categorías.
* Interfaz web sencilla mediante Streamlit.

---

## Autor

Proyecto desarrollado como práctica de detección y anonimización de datos personales mediante modelos LLM ejecutados localmente con Ollama.
