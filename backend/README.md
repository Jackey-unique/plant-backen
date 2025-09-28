# SDAP FastAPI Backend

## Setup

```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --host 0.0.0.0 --port 8215 --reload
```

The app serves under `/api` path. Vite dev server proxies `/api` to `http://localhost:8215/api`.

## Endpoints (sample)
- GET `/api/health`
- GET `/api/auth/current`
- GET `/api/dashboard/overview`
- GET `/api/greenhouse/list`
- GET `/api/device/list`
- POST `/api/ai/ask` { question }
- POST `/api/automation/targets` { temp, hum, co2, lux, auto }
- POST `/api/automation/toggle` { key, on }

