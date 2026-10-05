import logging
import sys

from app.core.config import settings

FORMAT = "%(asctime)s %(levelname)s [%(name)s] %(message)s"


def configure_logging() -> None:
    level = logging.DEBUG if settings.debug else logging.INFO
    logging.basicConfig(level=level, format=FORMAT, stream=sys.stdout)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

    access = logging.getLogger("access")
    access.setLevel(logging.INFO)
    access.propagate = False
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(message)s"))
    access.handlers = [handler]
