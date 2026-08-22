from fastapi import FastAPI


app = FastAPI(
    title="AI Action Firewall",
    description="Security layer for AI-agent actions.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the current API health status."""
    return {"status": "healthy"}