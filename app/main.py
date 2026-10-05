from fastapi import FastAPI

from app import __version__
from app.core.config import settings
from app.core.logging import configure_logging
from app.integrations.sentry import init_sentry
from app.middleware import register_middleware
from app.views import api_router, public_router

configure_logging()
init_sentry()

app = FastAPI(title=settings.app_name, version=__version__)
register_middleware(app)
app.include_router(public_router)
app.include_router(api_router)
