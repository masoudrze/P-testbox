import pytest

from core.config import settings


@pytest.fixture(scope="session")
def base_url():
    return settings.base_url