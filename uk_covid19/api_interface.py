#!/usr/bin python3

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python:
from typing import Iterable, Dict, Union, Iterator
from json import dumps
from http import HTTPStatus
from datetime import datetime
from xml.etree.ElementTree import Element as XMLElement

# 3rd party:
from requests import request, Response
import certifi

# Internal:
from uk_covid19.utils import save_data

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'Cov19API'
]


StructureType = Dict[str, Union[dict, str]]
FiltersType = Iterable[str]


class Cov19API:
    """
    COVID-19 API
    ------------
    Interface to access the API service for COVID-19 data in the United Kingdom.
    """
    endpoint = "https://api.coronavirus.data.gov.uk/v1/data"
    _valid_formats = [
        "csv",
        "json",
        "xml"
    ]
    _last_update: Union[str, None] = None
    total_pages: Union[int, None] = None

    def __init__(self, filters: FiltersType, structure: StructureType,
                 latest_by: Union[str, None] = None):
        """
        Parameters
        ----------
        filters: Iterable[str]
            API filters. See the API documentations for additional
            information.

        structure: Dict[str, Union[dict, str]]
            Structure parameter. See the API documentations for
            additional information.

        latest_by: Union[str, None]
            Retrieves the latest value for a specific metric. [Default: ``None``]
        """
        self.filters = filters
        self.structure = structure
        self.latest_by = latest_by

    @property
    def last_update(self) -> str:
        """
        Produces the timestamp for the last update in GMT.

        Returns
        -------
        str
            Timestamp, formatted as ISO-8601.

        .. note::
            The output is extracted from the header and is accurate to
            the second.

        Examples
        --------
        >>> filters = ["areaType=region"]
        >>> structure = {
        ...     "name": "areaName",
        ...     "newCases": "newCasesBySpecimenDate"
        ... }
        >>> data = Cov19API(
        ...     filters=filters,
        ...     structure=structure,
        ...     latest_by='newCasesBySpecimenDate'
        ... )
        >>> timestamp = data.last_update
        >>> print(timestamp)
        2020-07-27T20:29:16.000000Z

        .. warning::
            The ISO-8601 standard requires a ``"Z"`` character to be added
            to the end of the timestamp. This is a timezone feature and is
            not recognised by Python's ``datetime`` library. It is, however,
            most other libraries; e.g. ``pandas``. If you wish to parse the
            timestamp using the the ``datetime`` library, make sure that you
            remove the trailing ``"Z"`` character.

        >>> from datetime import datetime
        >>> parsed_timestamp = datetime.fromisoformat(timestamp.strip("Z"))
        >>> print(parsed_timestamp)
        2020-07-27 20:29:16
        """
        if self._last_update is None:
            self._last_update = self.head()['Last-Modified']

        timestamp = datetime.strptime(self._last_update, "%a, %d %b %Y %H:%M:%S GMT")

        return timestamp.isoformat() + ".000000Z"

    @property
    def api_params(self) -> dict:
        """
        API parameters, constructed based on ``filters``, ``structure``,
        and ``latest_by`` arguments as defined by the user.

        Returns
        -------
        Dict[str, str]
        """
        api_params = {
            "filters": str.join(";", self.filters),
            "structure": dumps(self.structure, separators=(",", ":")),
        }

        if self.latest_by is not None:
            api_params.update({
                "latestBy": self.latest_by
            })

        return api_params

    def head(self):
        """
        Request header for the given input arguments (``filters``,
        ``structure``, and ``lastest_by``).

        Returns
        -------
        Dict[str, str]

        Examples
        --------
        >>> filters = ["areaType=region"]
        >>> structure = {
        ...     "name": "areaName",
        ...     "newCases": "newCasesBySpecimenDate"
        ... }
        >>> data = Cov19API(
        ...     filters=filters,
        ...     structure=structure,
        ...     latest_by='newCasesBySpecimenDate'
        ... )
        >>> head = data.head()
        >>> print(head)
        {'Cache-Control': 'public, max-age=60', 'Content-Length': '0',
         ...
        }
        """
        api_params = self.api_params

        with request("HEAD", self.endpoint, params=api_params,
                     verify=certifi.where()) as response:
            response.raise_for_status()
            return response.headers

    @staticmethod
    def options():
        """
        Provides the options by calling the ``OPTIONS`` method of the API.

        Returns
        -------
        dict
            API options.

        Examples
        --------
        >>> from pprint import pprint
        >>> options = Cov19API.options()
        >>> pprint(options)
        {'info': {'description': "Public Health England's Coronavirus Dashboard API",
         'title': 'Dashboard API',
         'version': '1.0'},
         'openapi': '3.0.1',
          ...
        }
        """
        with request("OPTIONS", Cov19API.endpoint, verify=certifi.where()) as response:
            response.raise_for_status()
            return response.json()

    def _get(self, format_as: str) -> Iterator[Response]:
        """
        Extracts paginated data by requesting all of the pages
        and combining the results.

        Parameters
        ----------
        format_as: str
            Response format - Must be one of ``"json"``, ``"xml"``, or ``"csv"``.

        Returns
        -------
        Iterator[Response]
        """
        if format_as not in self._valid_formats:
            raise ValueError(
                f"`format_as` must be one of '{str.join(', ', self._valid_formats)}'"
            )

        api_params = self.api_params

        api_params.update({
            "format": format_as,
            "page": 1
        })

        while True:
            with request("GET", self.endpoint, params=api_params,
                         verify=certifi.where()) as response:
                if response.status_code >= HTTPStatus.BAD_REQUEST:
                    raise RuntimeError(f'Request failed: {response.text}')
                if response.status_code == HTTPStatus.NO_CONTENT:
                    self.total_pages = api_params["page"] - 1
                    break

                self._last_update = response.headers["Last-Modified"]

                yield response

            api_params["page"] += 1

    def get_json(self, save_as: Union[str, None] = None,
                 as_string: bool = False) -> Union[dict, str]:
        """
        Provides full data (all pages) in JSON.

        Parameters
        ----------
        save_as: Union[str, None]
            If defined, the results will (also) be saved as a
            file. [Default: ``None``]

            The value must be a path to a file with the correct
            extension -- i.e. ``.json`` for JSON).

        as_string: bool
            If ``False`` (default), returns the data as a dictionary.
            Otherwise, returns the data as a JSON string.

        Returns
        -------
        Union[Dict, str]

        Examples
        --------
        >>> filters = ["areaType=region"]
        >>> structure = {
        ...     "name": "areaName",
        ...     "newCases": "newCasesBySpecimenDate"
        ... }
        >>> data = Cov19API(
        ...     filters=filters,
        ...     structure=structure,
        ...     latest_by='newCasesBySpecimenDate'
        ... )
        >>> result = data.get_json()
        >>> print(result)
        {'data': [{'name': 'East Midlands', 'newCases': 0}, ... }
        """
        resp = {
            "data": list()
        }

        for response in self._get("json"):
            current_data = response.json()
            page_data = current_data['data']

            resp["data"].extend(page_data)

        resp["lastUpdate"] = self.last_update
        resp["length"] = len(resp["data"])
        resp["totalPages"] = self.total_pages

        if save_as is None:
            return resp

        data = dumps(resp, separators=(",", ":"))
        save_data(data, save_as, "json")

        if as_string:
            return dumps(resp, separators=(",", ":"))

        return resp

    def get_xml(self, save_as=None) -> XMLElement:
        """
        Provides full data (all pages) in XML.

        Parameters
        ----------
        save_as: Union[str, None]
            If defined, the results will (also) be saved as a
            file. [Default: ``None``]

            The value must be a path to a file with the correct
            extension -- i.e. ``.xml`` for XML).

        Returns
        -------
        xml.etree.ElementTree.Element

        Examples
        --------
        >>> from xml.etree.ElementTree import tostring
        >>> filters = ["areaType=region"]
        >>> structure = {
        ...     "name": "areaName",
        ...     "newCases": "newCasesBySpecimenDate"
        ... }
        >>> data = Cov19API(
        ...     filters=filters,
        ...     structure=structure,
        ...     latest_by='newCasesBySpecimenDate'
        ... )
        >>> result_xml = data.get_xml()
        >>> result_str = tostring(result_xml, encoding='unicode', method='xml')
        >>> print(result_str)
        <document>
            <data>
                <name>East Midlands</name>
                <newCases>0</newCases>
            </data>
            ...
        </document>
        """
        from xml.etree.ElementTree import SubElement, fromstring

        resp = XMLElement("document")

        for response in self._get("xml"):
            decoded_content = response.content.decode()

            # Parsing the XML:
            parsed_data = fromstring(decoded_content)

            # Extracting "data" elements from the tree:
            page_data = parsed_data.findall(".//data")

            resp.extend(page_data)

        extras = {
            "lastUpdate": self.last_update,
            "length": len(resp.findall(".//data")),
            "totalPages": self.total_pages
        }

        for elm_name, value in extras.items():
            elm = SubElement(resp, elm_name)
            elm.text = str(value)

        if save_as is None:
            return resp

        from xml.etree.ElementTree import tostring

        data = tostring(resp, encoding='unicode', method='xml')
        save_data(data, save_as, "xml")

        return resp

    def get_csv(self, save_as=None) -> str:
        """
        Provides full data (all pages) in CSV.

        .. warning::
            Please make sure that the ``structure`` is not hierarchical as
            CSV outputs are defined as 2D tables and as such, do not support
            hierarchies.

        Parameters
        ----------
        save_as: Union[str, None]
            If defined, the results will (also) be saved as a
            file. [Default: ``None``]

            The value must be a path to a file with the correct
            extension -- i.e. ``.csv`` for CSV).

        Returns
        -------
        str

        Examples
        --------
        >>> filters = ["areaType=region"]
        >>> structure = {
        ...     "name": "areaName",
        ...     "newCases": "newCasesBySpecimenDate"
        ... }
        >>> data = Cov19API(
        ...     filters=filters,
        ...     structure=structure,
        ...     latest_by='newCasesBySpecimenDate'
        ... )
        >>> result = data.get_csv()
        >>> print(result)
        name,newCases
        East Midlands,0
        ...
        """
        # Checks to ensure that the structure is
        # not hierarchical.
        if isinstance(self.structure, dict):
            non_str = filter(
                lambda val: not isinstance(val, str),
                self.structure.values()
            )

            if list(non_str):
                struct = dumps(self.structure, indent=4)
                raise ValueError("CSV structure cannot be nested. Received:\n%s" % struct)

        linebreak = "\n"
        resp = str()

        for page_num, response in enumerate(self._get("csv"), start=1):
            decoded_content = response.content.decode()

            # Removing CSV header (column names) where page
            # number is greater than 1.
            if page_num > 1:
                data_lines = decoded_content.split(linebreak)[1:]
                decoded_content = str.join(linebreak, data_lines)

            resp += decoded_content.strip() + linebreak

        if save_as is None:
            return resp

        save_data(resp, save_as, "csv")

        return resp

    def __str__(self):
        resp = "COVID-19 in the UK - API Service\nCurrent parameters: \n"
        return resp + dumps(self.api_params, indent=4)

    __repr__ = __str__
