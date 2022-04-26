import pytest

from app.factory import create_app
from app.settings import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app