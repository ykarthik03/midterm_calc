"""
Tests for the config module.
"""

from config import get_config

def test_get_config_default():
    assert get_config("NON_EXISTENT_KEY", "default") == "default"

def test_get_config_env(monkeypatch):
    monkeypatch.setenv("MY_CONFIG", "value123")
    assert get_config("MY_CONFIG") == "value123"
