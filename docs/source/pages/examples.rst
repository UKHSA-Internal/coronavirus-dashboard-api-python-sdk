Examples
--------

This section provides simple examples for the library.


General use
...........

We would like to extract the number of new cases, cumulative cases, new deaths and
cumulative deaths for England using the API.

We start off by importing the library into our workspace:

.. code-block:: python

    from uk_covid19 import Cov19API


Next, we construct the value of the ``filters`` parameter:

.. code-block:: python

    england_only = [
        'areaType=nation',
        'areaName=England'
    ]

Next step is to construct the value of the ``structure`` parameter. To do so, we need to
find out the name of the metric in which we are interested. You can find this information
in the _`Developers Guide` on the Coronavirus Dashboard website.

In the case of this example, the metrics are as follows:

- ``newCasesByPublishDate``: New cases (by publish date)
- ``cumCasesByPublishDate``: Cumulative cases (by publish date)
- ``newDeathsByDeathDate``: New deaths (by death date)
- ``cumDeathsByDeathDate``: Cumulative deaths (by death date)

In its simplest form, we construct the structure as follows:

.. code-block:: python

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeathsByDeathDate": "newDeathsByDeathDate",
        "cumDeathsByDeathDate": "cumDeathsByDeathDate"
    }


Now, we may use ``filters`` and ``structure`` to initialise the ``Covid19API`` object:

.. code-block:: python

    api = Cov19API(filters=england_only, structure=cases_and_deaths)
    data = api.get_json()  # Returns a dictionary
    print(data)


You may also use ``data.get_xml()`` or ``data.get_csv()`` to download the data in other
available formats.

::

    {
        'data': [
            {
                'date': '2020-07-28',
                'areaName': 'England',
                'areaCode': 'E92000001',
                'newCasesByPublishDate': 547,
                'cumCasesByPublishDate': 259022,
                'newDeathsByDeathDate': None,
                'cumDeathsByDeathDate': None
            },
            {
                'date': '2020-07-27',
                'areaName': 'England',
                'areaCode': 'E92000001',
                'newCasesByPublishDate': 616,
                'cumCasesByPublishDate': 258475,
                'newDeathsByDeathDate': 20,
                'cumDeathsByDeathDate': 41282
            },
            ...
        ],
        'lastUpdate': '2020-07-28T15:34:31.000000Z',
        'length': 162,
        'totalPages': 1
    }

Timestamps
..........

There are two options to get the timestamp for the last update:

- Using the ``.last_update`` property.
- Using the ``.get_release_timestamp()`` (static) method.

.. note::

    Please note that the timestamp produced by the ``.last_update`` property is not the
    same as the which is produced by the ``.get_release_timestamp()`` method. The former
    supplies the API timestamp - i.e. the time at which the data were deployed to the
    database - whilst the latter supplies the time at which the data were **released** to
    the API and by extension the website. There will always be a difference lag between
    the two timestamps as the data undergo a quality assurance process before they are
    released to the API / website.

.. code-block:: python

    from uk_covid19 import Cov19API

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeathsByDeathDate": "newDeathsByDeathDate",
        "cumDeathsByDeathDate": "cumDeathsByDeathDate"
    }

    england_only = [
        'areaType=nation',
        'areaName=England'
    ]

    api = Cov19API(filters=england_only, structure=cases_and_deaths)
    api_timestamp = api.last_update

    print(api_timestamp)

::

    2020-07-28T14:34:31.000000Z


.. code-block:: python

    from uk_covid19 import Cov19API

    release_timestamp = Cov19API.get_release_timestamp()

    print(release_timestamp)

::

    2020-07-28T15:00:00.431323Z


.. note::

    The ``.last_update`` timestamp is produced if and *only* if the ``Cov19API``
    object is instantiated - i.e. when specific ``filters`` and ``structure`` parameters have
    been set. On the other hand, ``.get_release_timestamp()`` is a static method and therefore
    independent of parameters. This is because the ``.last_update`` timestamp is specific to
    a set of query metrics and is extracted from the ``HEAD`` of an API request. The
    ``.get_release_timestamp()`` method is, however, extracted from a static file which is
    generated a the precise moment when the data is released.


.. warning::

    It may take up to 60 seconds for the data to be updated when the *release timestamp*
    (``.get_release_timestamp()``) is updated. This is because the cache refresh before the
    new data becomes available. The **API timestamp** (``.last_update``), however, is only
    updated when the cache has been refreshed. This means that you can only be certain that
    you are receiving the most up-to-data data when the ``.last_update`` timestamp for your
    specific parameters have been updated.


Latest data
...........

To get the latest data by a specific metric, run:

.. code-block:: python

    from uk_covid19 import Cov19API

    all_nations = [
        "areaType=nation"
    ]

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeathsByDeathDate": "newDeathsByDeathDate",
        "cumDeathsByDeathDate": "cumDeathsByDeathDate"
    }

    api = Cov19API(
        filters=all_nations,
        structure=cases_and_deaths,
        latest_by="newCasesByPublishDate"
    )

    data = api.get_json()

    print(data)

::

    {
        "data": [
            {
                "date": "2020-07-28",
                "areaName": "England",
                "areaCode": "E92000001",
                "newCasesByPublishDate": 547,
                "cumCasesByPublishDate": 259022,
                "newDeathsByDeathDate": None,
                "cumDeathsByDeathDate": None
            },
            {
                "date": "2020-07-28",
                "areaName": "Northern Ireland",
                "areaCode": "N92000002",
                "newCasesByPublishDate": 9,
                "cumCasesByPublishDate": 5921,
                "newDeathsByDeathDate": None,
                "cumDeathsByDeathDate": None
            },
            {
                "date": "2020-07-28",
                "areaName": "Scotland",
                "areaCode": "S92000003",
                "newCasesByPublishDate": 4,
                "cumCasesByPublishDate": 18558,
                "newDeathsByDeathDate": None,
                "cumDeathsByDeathDate": None
            },
            {
                "date": "2020-07-28",
                "areaName": "Wales",
                "areaCode": "W92000004",
                "newCasesByPublishDate": 21,
                "cumCasesByPublishDate": 17191,
                "newDeathsByDeathDate": None,
                "cumDeathsByDeathDate": None
            }
        ],
        "lastUpdate": "2020-07-28T15:34:31.000000Z",
        "length": 4,
        "totalPages": 1
    }


Saving the data
...............

Set the ``save_as`` input argument to a path to save the data in a file. This
functionality is only available for ``.get_json()``, ``.get_xml()`` and ``.get_csv()``
methods.

Note that the ``save_as`` argument must be set to a file name with the correct extension;
that is, ``.json`` for JSON data, ``.xml`` for XML data, and ``.csv`` for CSV data. It is
assumed that the directory in which you wish to save the file already exists.

You may use relative or absolute paths.

.. code-block:: python

    from uk_covid19 import Cov19API

    all_nations = [
        "areaType=nation"
    ]

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeathsByDeathDate": "newDeathsByDeathDate",
        "cumDeathsByDeathDate": "cumDeathsByDeathDate"
    }

    api = Cov19API(
        filters=all_nations,
        structure=cases_and_deaths,
        latest_by="newCasesByPublishDate"
    )

    api.get_csv(save_as="some_existing_directory/data.csv")


This will create a file entitled ``data.csv`` under ``some_existing_directory``. The
contents of the file would be as follows:

::

    date,areaName,areaCode,newCasesByPublishDate,cumCasesByPublishDate,newDeathsByDeathDate,cumDeathsByDeathDate
    2020-07-28,England,E92000001,547,259022,,
    2020-07-28,Northern Ireland,N92000002,9,5921,,
    2020-07-28,Scotland,S92000003,4,18558,,
    2020-07-28,Wales,W92000004,21,17191,,


Data as JSON string
...................

Set the ``as_string`` input argument to ``True`` for the ``.get_json()`` method if you
wish to receive the result as a JSON string instead of a ``dict`` object:

.. code-block:: python

    from uk_covid19 import Cov19API

    all_nations = [
        "areaType=nation"
    ]

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeathsByDeathDate": "newDeathsByDeathDate",
        "cumDeathsByDeathDate": "cumDeathsByDeathDate"
    }

    api = Cov19API(
        filters=all_nations,
        structure=cases_and_deaths,
        latest_by="newCasesByPublishDate"
    )

    data = api.get_json(as_string=True)

    print(data)

::

    {"data":[{"date":"2020-07-28","areaName":"England","areaCode":"E92000001","newCasesByPublishDate":547,"cumCasesByPublishDate":259022,"newDeathsByDeathDate":null,"cumDeathsByDeathDate":null},{"date":"2020-07-28","areaName":"Northern Ireland","areaCode":"N92000002","newCasesByPublishDate":9,"cumCasesByPublishDate":5921,"newDeathsByDeathDate":null,"cumDeathsByDeathDate":null},{"date":"2020-07-28","areaName":"Scotland","areaCode":"S92000003","newCasesByPublishDate":4,"cumCasesByPublishDate":18558,"newDeathsByDeathDate":null,"cumDeathsByDeathDate":null},{"date":"2020-07-28","areaName":"Wales","areaCode":"W92000004","newCasesByPublishDate":21,"cumCasesByPublishDate":17191,"newDeathsByDeathDate":null,"cumDeathsByDeathDate":null}],"lastUpdate":"2020-07-28T15:34:31.000000Z","length":4,"totalPages":1}


Data as Pandas DataFrame
........................

You can use the ``.get_dataframe()`` method to get the data as a Pandas DataFrame object.

.. warning::

    The ``pandas`` library is not included in the dependencies of this
    library and must be installed separately.

.. code-block:: python

    from uk_covid19 import Cov19API

    all_nations = [
        "areaType=nation"
    ]

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeathsByDeathDate": "newDeathsByDeathDate",
        "cumDeathsByDeathDate": "cumDeathsByDeathDate"
    }

    api = Cov19API(
        filters=all_nations,
        structure=cases_and_deaths
    )

    df = api.get_dataframe()

    print(df.head())

::

             date          areaName   areaCode  newCasesByPublishDate  cumCasesByPublishDate newDeathsByDeathDate cumDeathsByDeathDate
    0  2020-08-08           England  E92000001                    679               267324.0                 None                 None
    1  2020-08-08  Northern Ireland  N92000002                      0                    NaN                 None                 None
    2  2020-08-08          Scotland  S92000003                     60                18950.0                 None                 None
    3  2020-08-08             Wales  W92000004                     19                17425.0                 None                 None
