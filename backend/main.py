from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.auth import router as auth_router
from routers.dashboard import router as dashboard_router
from routers.greenhouse import router as greenhouse_router
from routers.device import router as device_router
from routers.ai import router as ai_router
from routers.automation import router as automation_router


def create_app() -> FastAPI:
    app = FastAPI(title="SDAP Backend", version="0.1.0")

    # CORS for local dev (vite default dev server runs at 5173)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Mount under /api to match vite proxy target
    app.include_router(auth_router, prefix="/api")
    app.include_router(dashboard_router, prefix="/api")
    app.include_router(greenhouse_router, prefix="/api")
    app.include_router(device_router, prefix="/api")
    app.include_router(ai_router, prefix="/api")
    app.include_router(automation_router, prefix="/api")

    @app.get("/api/health")
    def health():
        return {"code": 200, "message": "OK", "data": {"service": "sdap-backend"}}

    return app


app = create_app()


