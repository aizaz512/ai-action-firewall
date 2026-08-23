from fastapi import FastAPI

from backend.app.api.health import router as health_router

app = FastAPI(
    title="AI Action Firewall",
    description="Security layer for AI-agent actions.",
    version="0.1.0",
)

app.include_router(health_router)