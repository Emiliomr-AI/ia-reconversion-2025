param([Parameter(Mandatory=$true)][ValidateSet("init","lint","format","test","type","smoke","api")] [string]$cmd)

switch ($cmd) {
  "init"   { python -m pip install -U pip; pip install -r requirements.txt; pre-commit install }
  "lint"   { python -m ruff check . --fix }
  "format" { python -m black . }
  "test"   { python -m pytest -q }
  "type"   { python -m mypy src }
  "api"    { python -m uvicorn api.main:app --host 127.0.0.1 --port 8000 }
  "smoke"  {
    python -m ruff check .
    python -m black --check .
    python -m pytest -q
    python -m mypy src
    $p = Start-Process python -ArgumentList "-m","uvicorn","api.main:app","--host","127.0.0.1","--port","8000" -PassThru
    Start-Sleep -Seconds 2
    (Invoke-WebRequest http://127.0.0.1:8000/health -UseBasicParsing).Content
    Stop-Process -Id $p.Id -Force
  }
}
