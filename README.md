# IA Reconversión 2025

Repositorio de trabajo personal para pasar de **dev full stack junior** a **AI/LLM Engineer aplicado** en ~12 semanas, con foco en:
- ML clásico orientado a negocio (EDA, modelos tabulares, XGBoost/LightGBM).
- GenAI / RAG con LangChain o LlamaIndex.
- Exposición vía **FastAPI**, **Docker** y **MLflow**.
- Portfolio orientado a **trabajo remoto internacional** (UE/UK primero).

> **Sistema operativo:** Windows 11
> **Python:** 3.x (entorno virtual `ia_env`)
> **Editor:** VS Code (con Black, Ruff, pre-commit y Continue configurados)

## 1. Estructura del proyecto

```text
ia-reconversion-2025/
├─ .vscode/             # Config de VS Code (formateo, cSpell, etc.)
├─ .continue/           # Config de la extensión Continue (modelos GPT)
├─ notebooks/           # Exploración, cursos y prototipos
│  ├─ 01_genai_intro/
│  ├─ 02_rag_health/
│  └─ 03_service_e2e/
├─ data/
│  ├─ raw/              # Datos originales
│  ├─ interim/          # Datos intermedios / procesados parcialmente
│  └─ processed/        # Datos listos para modelo
├─ src/                 # Código fuente reutilizable (pipelines, rag, common)
│  ├─ common/
│  ├─ rag/
│  └─ service/
├─ api/                 # FastAPI (endpoints para modelos/RAG)
│  └─ main.py
├─ configs/             # Archivos .yaml de configuración
├─ docker/              # Dockerfiles, compose y utilidades
├─ scripts/             # Scripts CLI (ingesta, entrenamiento, evaluación)
├─ experiments/         # Seguimiento manual de pruebas
├─ tests/               # Tests unitarios/integ.
├─ .env                 # Variables de entorno (NO subir)
├─ requirements.txt
└─ README.md
```

## 2. Requisitos previos

- Python 3.x
- git
- VS Code (recomendado)
- Docker Desktop (opcional pero recomendado para despliegues)
- Cuenta en OpenAI u otro proveedor LLM (para el RAG)

## 3. Instalación

```bash
# 1. Clonar el repo
git clone git@github.com:Emiliomr-AI/ia-reconversion-2025.git
cd ia-reconversion-2025

# 2. Crear entorno virtual (Windows)
python -m venv ia_env
ia_env\Scripts\activate

# 3. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 4. Instalar pre-commit (opcional, recomendado)
pre-commit install
```

## 4. Variables de entorno

Crea un archivo `.env` en la raíz con algo como:

```env
OPENAI_API_KEY=tu_api_key
PROJECT_NAME=ia-reconversion-2025
ENV=local
API_HOST=0.0.0.0
API_PORT=8000
VECTOR_DB_DIR=./data/interim/vectorstore
```

No subas este archivo al repo.

## 5. Notebooks

- `notebooks/01_genai_intro/`: calentamiento, APIs de LLM, embeddings.
- `notebooks/02_rag_health/`: experimento principal de RAG sobre PDFs/texto de salud.
- `notebooks/03_service_e2e/`: pruebas para llevar el modelo/flow a producción.

Regla: **todo lo que funcione en notebook y sea estable pásalo a `src/`**.

## 6. API (FastAPI)

Punto de entrada típico:

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

La API debería exponer:
- `/health` → comprobar que el servicio está arriba.
- `/predict` → para modelos tabulares.
- `/rag/query` → para el asistente de documentos.
- (opcional) `/metrics` → para Prometheus/Grafana si se añade.

Documentación automática en: http://localhost:8000/docs

## 7. Docker

En `docker/` irán los Dockerfile y/o `docker-compose.yml`.

Ejemplo de build:

```bash
docker build -t ia-reconversion-2025 -f docker/Dockerfile .
docker run -p 8000:8000 --env-file .env ia-reconversion-2025
```

## 8. MLflow (opcional pero previsto)

La idea es poder loguear experimentos (modelos tabulares o RAG evaluado).

```bash
mlflow ui --port 5000
```

Configura la URI en tus scripts de entrenamiento dentro de `src/` o `scripts/`.

## 9. Roadmap (12 semanas)

1. Semanas 1-2: refresco Python + pandas, ML clásico, estructura del repo.
2. Semanas 3-4: proyecto tabular con API.
3. Semanas 5-7: RAG en salud: ingesta, indexado, retrieval, evaluación.
4. Semanas 8-9: servicio E2E dockerizado + MLflow.
5. Semanas 10-12: pulir portfolio, documentación, grabar explicación en inglés, empezar a postular.

## 10. Estilo y calidad

- Formateo: Black
- Lint: Ruff
- Tests: pytest en `tests/`
- Commits: mensaje corto y descriptivo, p.ej. `feat(rag): add pdf ingestion pipeline`

## 11. Licencia

Pendiente de elegir (MIT recomendado para portfolio).

## 12. Autor

Proyecto personal de reconversión a AI/LLM Engineer (2025).
