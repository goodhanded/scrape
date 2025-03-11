from fastapi import FastAPI
from infrastructure.api.routes import scrape_job_routes
from infrastructure.logging.logging_config import setup_logging
from infrastructure.config.services.config import Config
from infrastructure.di.container import Container
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
config = Config(project_root / ".env")

setup_logging(config.get("LOG_LEVEL", "INFO"))

container = Container.from_yaml("services.yaml")

app = FastAPI(title="Web Scraper API")
app.include_router(scrape_job_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("infrastructure.api.main:app", host="0.0.0.0", port=8000, reload=True)
