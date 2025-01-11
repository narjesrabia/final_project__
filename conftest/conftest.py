import os
import pytest

@pytest.fixture(scope="session", autouse=True)
def set_django_settings():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
