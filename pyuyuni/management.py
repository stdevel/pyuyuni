"""
Uyuni JSON over HTTP client
"""

import logging
import ssl
import json
import requests
from .exceptions import (
    InvalidCredentialsException,
    SSLCertVerificationError,
    SessionException
)


class JSONHTTPClient:
    """
    Class for communicating with the Uyuni API

    .. class:: JSONHTTPClient
    """

    LOGGER = logging.getLogger("JSONHTTPClient")
    """
    logging: Logger instance
    """
    HEADERS = {
        "User-Agent": "pyuyuni (https://github.com/stdevel/pyuyuni)",
        "Content-Type": "application/json"
    }
    """
    dict: Default headers set for every HTTP request
    """

    def __init__(
            self, log_level, hostname, username, password,
            port=443, verify=True
    ):
        """
        Constructor creating the class. It requires specifying a
        hostname, username and password to access the API. After
        initialization, a connected is established.

        :param log_level: log level
        :type log_level: logging
        :param username: API username
        :type username: str
        :param password: corresponding password
        :type password: str
        :param hostname: Uyuni host
        :type hostname: str
        :param port: HTTPS port
        :type port: int
        :param verify: SSL verification
        :type verify: bool
        """
        # set logging
        self.LOGGER.setLevel(log_level)
        self.LOGGER.error(
            "About to create Uyuni JSONHTTPClient '%s'@'%s'",
            username, hostname
        )

        # set connection information
        self.LOGGER.debug("Set hostname to '%s'", hostname)
        self.url = f"https://{hostname}:{port}/rhn/manager/api"
        self.verify = verify
        self.username = username
        self.password = password

        # start session
        self._cookie = None
        self._connect()


    def _connect(self):
        """
        This function establishes a connection to Uyuni
        """
        # set API session and key
        try:
            self._session = requests.Session()
            _data = {
                "login": self.username,
                "password": self.password
            }
            _login = self._session.post(
                f"{self.url}/auth/login",
                json=_data,
                headers=self.HEADERS,
                verify=self.verify
            )
            _cookies = self._session.cookies.get_dict()

            # check if login succeeded
            if not json.loads(_login.text)['success']:
                raise InvalidCredentialsException("Username/password combination is invalid")
            if not _cookies['pxt-session-cookie']:
                raise SessionException("Didn't receive a valid cookie")

            # set cookie
            self._cookie = _cookies['pxt-session-cookie']
        except ssl.SSLCertVerificationError as err:
            self.LOGGER.error(err)
            raise SSLCertVerificationError(str(err)) from err
