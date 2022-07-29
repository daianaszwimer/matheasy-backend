# This file contains all dependency injection definitions
import os
from logging import Logger

from flask.logging import create_logger
from kink import di


def bootstrap_di() -> None:
    logger = create_logger(os.getenv("LOG_LEVEL", "INFO"))

    di[Logger] = logger