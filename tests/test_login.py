"""
Login tests
"""
import logging
import pytest
from pyuyuni.management import JSONHTTPClient
from pyuyuni.exceptions import (
    InvalidCredentialsException
)
from .utilities import load_config

@pytest.fixture(scope='session')
def config():
    """
    Load test configuration
    """
    return load_config("uyuni_config.yml")


@pytest.fixture(scope='session')
def api_client(config_file):
    """
    Instance client
    """
    return JSONHTTPClient(
        logging.ERROR,
        config_file["config"]["hostname"],
        config_file["config"]["username"],
        config_file["config"]["password"],
        port=config_file["config"]["port"],
        verify=False
    )


def test_valid_login(config):
    """
    Ensure valid logins are possible
    """
    assert JSONHTTPClient(
        logging.ERROR,
        config["config"]["hostname"],
        config["config"]["username"],
        config["config"]["password"],
        port=config["config"]["port"],
        verify=False
    )


def test_invalid_login(config):
    """
    Ensure exceptions on invalid logins
    """
    with pytest.raises(InvalidCredentialsException):
        JSONHTTPClient(
            logging.ERROR,
            config["config"]["hostname"],
            "giertz",
            "paulapinkepank",
            port=config["config"]["port"],
            verify=False
        )
