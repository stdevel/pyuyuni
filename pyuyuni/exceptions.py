"""
Exceptions used by the management classes
"""


class SessionException(Exception):
    """
    Exception for session errors

    .. class:: SessionException
    """


class InvalidCredentialsException(Exception):
    """
    Exception for invalid credentials

    .. class:: InvalidCredentialsException
    """


class SSLCertVerificationError(Exception):
    """
    Exception for invalid SSL certificates

    .. class:: SSLCertVerificationError
    """


class EmptySetException(Exception):
    """
    Exception for empty result sets

    .. class:: EmptySetException
    """
