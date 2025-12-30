import pytest

from src.config import Config

@pytest.fixture
def config() -> Config:
    Config.init()
    return Config