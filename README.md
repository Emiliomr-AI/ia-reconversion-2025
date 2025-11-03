# IA Reconversión 2025
Roadmap: 12 semanas (Intro → RAG salud → Servicio e2e).
## Estructura
- `notebooks/` exploración y cursos
- `src/` código reusable (common, rag, service)
- `data/` raw/interim/processed
- `api/` FastAPI
- `configs/` parámetros por entorno
## Setup
1) `.\ia_env\Scripts\activate`
2) `pip install -r requirements.txt`
3) Crear `.env` con `OPENAI_API_KEY=...`
## Run checks
- `python experiments/2025-11-03_hello_openai.py`
- (próx.) `uvicorn api.main:app --reload`
This project use FastAPI and LangChin for retrieval.
