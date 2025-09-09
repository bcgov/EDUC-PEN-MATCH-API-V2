from fastapi import FastAPI
from .api import router
from .config import settings
from .logging_conf import configure_logging

configure_logging()
app = FastAPI(title=settings.APP_NAME)
app.include_router(router)
