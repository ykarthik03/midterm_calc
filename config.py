"""
Module: config
Provides a helper to retrieve configuration values from environment variables.
"""

import os

def get_config(key, default=None):
    """
    Return the value of the environment variable 'key', or 'default' if not set.
    """
    return os.getenv(key, default)
