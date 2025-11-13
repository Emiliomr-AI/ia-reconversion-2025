from fastapi import FastAPI

app = FastAPI(title="ia-reconversion-2025")


@app.get("/health")
def health():
    return {"status": "ok"}
