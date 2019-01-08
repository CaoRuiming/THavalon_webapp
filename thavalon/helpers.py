"""General-purpose helper functions"""
import os

from flask import current_app


def get_config(name, app=current_app, default=None):
    """
    Look up a configuration parameter. Searches environment variables
    and the Flask app configuration, in that order.
    """
    if name in os.environ:
        return os.environ[name]
    elif name in app.config:
        return app.config[name]
    else:
        return default


def env_is_prod():
    """Test if we're running in production."""
    return get_config('PROD') is not None


def env_is_dev():
    """Test if we're running in development."""
    return not env_is_prod()
