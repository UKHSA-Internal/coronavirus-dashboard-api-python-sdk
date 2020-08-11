Coronavirus (COVID-19) in the UK - API Service
==============================================

|PyPi_Version| |PyPi_Status| |Format| |Supported_versions_of_Python| |Language grade: Python| |License|


Software Development Kit (SDK) for Python
-----------------------------------------

This is a Python SDK for the COVID-19 API, as published by Public Health England
on `Coronavirus (COVID-19) in the UK`_.

Documentation
.............

Comprehensive documentations and examples for this library is available on the
`documentations website`_.


SDK for other languages
.......................

Similar libraries are also available for `JavaScript`_, `R`_, `.Net`_, and `Elixir`_.


The API
-------

The API supplies the latest data for the COVID-19 outbreak in the United Kingdom. The
endpoint for the data provided using this SDK is:

::

    https://api.coronavirus.data.gov.uk/v1/data


See the `Developers Guide`_ for additional information on the API and see a list of
latest metrics.


Installation
------------

Python 3.7+ is required to install and use this library.

To install, please run:

.. code-block:: bash

    pip install uk-covid19

You may install the library for a specific version of Python as follows:

.. code-block:: python

    python -m pip install uk-covid19

You can simply replace ``python`` with a specific version for which you wish to install
the library - e.g. ``python3`` or ``python3.8``.





-----------

Developed and maintained by `Public Health England`_.

Copyright (c) 2020, Public Health England.

.. _`Coronavirus (COVID-19) in the UK`: http://coronavirus.data.gov.uk/
.. _`Public Health England`: https://www.gov.uk/government/organisations/public-health-england
.. _`Developers Guide`: https://coronavirus.data.gov.uk/developers-guide
.. _`JavaScript`: https://github.com/publichealthengland/coronavirus-dashboard-api-javascript-sdk
.. _`R`: https://github.com/publichealthengland/coronavirus-dashboard-api-R-sdk
.. _`.Net`: https://github.com/publichealthengland/coronavirus-dashboard-api-net-sdk
.. _`documentations website`: https://publichealthengland.github.io/coronavirus-dashboard-api-python-sdk/
.. _`Elixir`: https://github.com/publichealthengland/coronavirus-dashboard-api-elixir-sdk

.. |PyPi_Version| image:: https://img.shields.io/pypi/v/uk-covid19
.. |PyPi_Status| image:: https://img.shields.io/pypi/status/uk-covid19
.. |Format| image:: https://img.shields.io/pypi/format/uk-covid19
.. |Supported_versions_of_Python| image:: https://img.shields.io/pypi/pyversions/uk-covid19
.. |License| image:: https://img.shields.io/github/license/publichealthengland/coronavirus-dashboard-api-python-sdk
.. |Language grade: Python| image:: https://img.shields.io/lgtm/grade/python/g/publichealthengland/coronavirus-dashboard-api-python-sdk.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/publichealthengland/coronavirus-dashboard-api-python-sdk/context:python
