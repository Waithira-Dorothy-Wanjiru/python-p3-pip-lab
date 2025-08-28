import sys
import requests
import pytest

def python_version():
    """Return Python version info."""
    return sys.version_info

def requests_version():
    """Return installed requests version."""
    return requests.__version__

def pytest_version():
    """Return installed pytest version."""
    return pytest.__version__
