from fastapi import FastAPI
from infrastructure.api.router_factory import RouterFactory
from infrastructure.logging.logging_config import setup_logging
from infrastructure.config.services.config import Config
from infrastructure.di.container import Container
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
config = Config(project_root / ".env")

setup_logging(config.get("LOG_LEVEL", "INFO"))

container = Container.from_yaml("services.yaml")

app = FastAPI(title="Web Scraper API")

router_factory: RouterFactory = container.get('router_factory')
router = router_factory.create()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("infrastructure.api.main:app", host="0.0.0.0", port=8000, reload=True)
