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
from pyuyuni.hosts import list_systems_requiring_reboot

@pytest.fixture(scope='session')
def config_file():
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


def test_hosts_requiring_reboots(api_client):
    """
    Ensure that hosts requiring reboots can be listed
    """
    _systems = list_systems_requiring_reboot(api_client)
    assert _systems
