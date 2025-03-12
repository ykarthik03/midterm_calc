# logger_setup.py

import os
import logging

def setup_logging():
    log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
    log_level = getattr(logging, log_level_str, logging.INFO)
    root_logger = logging.getLogger()

    # Clear existing handlers if any
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=log_level, format=log_format)
    logging.info("Logging is configured with level: %s", log_level_str)
