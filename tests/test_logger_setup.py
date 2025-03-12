import logging
from logger_setup import setup_logging

def test_logger_setup_debug(monkeypatch):
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    setup_logging()
    root_logger = logging.getLogger()
    assert root_logger.getEffectiveLevel() <= logging.DEBUG

def test_logger_setup_default(monkeypatch):
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    setup_logging()
    root_logger = logging.getLogger()
    assert root_logger.getEffectiveLevel() == logging.INFO

def test_logger_setup_clears_existing_handlers(monkeypatch):
    root_logger = logging.getLogger()
    dummy_handler = logging.StreamHandler()
    root_logger.addHandler(dummy_handler)
    # Confirm dummy_handler is present
    assert dummy_handler in root_logger.handlers
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    setup_logging()
    # After setup_logging, the dummy handler should be cleared
    assert dummy_handler not in root_logger.handlers

def test_logger_setup_no_existing_handlers(monkeypatch):
    # Ensure no pre-existing handlers
    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    setup_logging()
    # After setup, basicConfig should have added at least one handler
    assert len(root_logger.handlers) > 0
