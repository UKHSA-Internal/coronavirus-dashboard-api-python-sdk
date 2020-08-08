#!/usr/bin python3

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python:
from pprint import pformat
from urllib.parse import unquote

# 3rd party:
from requests import Response

# Internal: 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'FailedRequestError'
]


class FailedRequestError(RuntimeError):
    """
    Exception for failed HTTP request.
    """

    message = """
Request failed .... {status_code} - {reason}
Response .......... {response_text}
URL ............... {url}
Decoded URL ....... {decoded_url}
Parameters:
{params}
"""

    def __init__(self, response: Response, params: dict):
        """
        Parameters
        ----------
        response: Response
            HTTP request ``Response`` object, as produced by the ``requests``
            library.

        params: dict
            Dictionary of parameters.
        """
        message = self.message.format(
            status_code=response.status_code,
            reason=response.reason,
            response_text=response.content.decode() or "No response",
            url=response.url,
            decoded_url=unquote(response.url),
            params=pformat(params, indent=2)
        )

        super().__init__(message)
