"""
Login tests
"""
import logging
import pytest
import json
from pyuyuni.management import JSONHTTPClient
from pyuyuni.exceptions import (
    InvalidCredentialsException,
    SessionException
)
from .utilities import load_config

@pytest.fixture(scope='session')
def config():
    """
    Load test configuration
    """
    return load_config("uyuni_config.yml")


@pytest.fixture(scope='session')
def api_client(config):
    """
    Instance client
    """
    return JSONHTTPClient(
        logging.ERROR,
        config["config"]["hostname"],
        config["config"]["username"],
        config["config"]["password"],
        port=config["config"]["port"],
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


def test_valid_query(api_client):
    """
    Ensure that valid queries can be executed
    """
    _result = api_client.query(
        "system/listSystems"
    )
    assert _result["success"]
    assert _result["result"]


def test_invalid_query(api_client):
    """
    Ensure that invalid queries can't be executed
    """
    with pytest.raises(SessionException):
        _result = api_client.query(
            "hurrdurr/api_goes_brrr"
        )
