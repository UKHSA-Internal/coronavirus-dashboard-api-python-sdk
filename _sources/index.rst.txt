.. uk-covid19 documentation master file, created by
   sphinx-quickstart on Sun Aug  9 13:29:11 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:github_url: https://github.com/publichealthengland/coronavirus-dashboard-api-python-sdk


Coronavirus (COVID-19) in the UK - API Service
==============================================
|PyPi_Version| |PyPi_Status| |Format| |Supported_versions_of_Python| |lgtm| |License|


Software Development Kit for Python
-----------------------------------

This website provides documentations and examples for the **Python SDK** library entitled
``uk-covid19``, as published by Public Health England on `Coronavirus (COVID-19) in the UK`_.

Similar libraries are also available for `JavaScript`_, `R`_, `.Net`_, and `Elixir`_.


The API
-------

The API supplies the latest data for the COVID-19 outbreak in the United Kingdom. The
endpoint for the data provided using this SDK is:

::

    https://api.coronavirus.data.gov.uk/v1/data


See the `Developers Guide`_ for additional information on the API and see a list of
latest metrics.


Pagination
..........

The API responses are restricted to 1000 records per request. If you need more records,
you will need to use the ``page`` query parameter to enable pagination.

As a bonus, the SDKs come with a built-in mechanism to bypass pagination restrictions in
the API and produce the entire data for a given combination of ``filters`` and
``structure`` in one go.

When accessing the API through one of the SDKs, you will always download the entire
dataset unless the ``latest_by`` argument is defined.

-------

.. toctree::
   :maxdepth: 3
   :glob:
   :caption: Table of Contents

   pages/getting_started
   pages/examples/examples.rst

   uk_covid19/index


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


-----


-----------

Developed and maintained by `Public Health England`_.

Copyright (c) 2020, Public Health England.

.. _`Coronavirus (COVID-19) in the UK`: http://coronavirus.data.gov.uk/
.. _`Public Health England`: https://www.gov.uk/government/organisations/public-health-england
.. _`Developers Guide`: https://coronavirus.data.gov.uk/developers-guide
.. _`JavaScript`: https://github.com/publichealthengland/coronavirus-dashboard-api-javascript-sdk
.. _`R`: https://github.com/publichealthengland/coronavirus-dashboard-api-R-sdk
.. _`.Net`: https://github.com/publichealthengland/coronavirus-dashboard-api-net-sdk
.. _`Elixir`: https://github.com/publichealthengland/coronavirus-dashboard-api-elixir-sdk

.. |PyPi_Version| image:: https://img.shields.io/pypi/v/uk-covid19
.. |PyPi_Status| image:: https://img.shields.io/pypi/status/uk-covid19
.. |Format| image:: https://img.shields.io/pypi/format/uk-covid19
.. |Supported_versions_of_Python| image:: https://img.shields.io/pypi/pyversions/uk-covid19
.. |License| image:: https://img.shields.io/github/license/publichealthengland/coronavirus-dashboard-api-python-sdk
.. |lgtm| image:: https://img.shields.io/lgtm/grade/python/github/publichealthengland/coronavirus-dashboard-api-python-sdk