Django-Yandex-Direct
====================

Installation and usage
----------------------
1. Using pip:

.. code-block:: bash

    $  sudo pip install django-yandex-direct

2. Add to settings your credentials:

.. code-block:: python

    YANDEX_DIRECT_LOGIN = ''
    YANDEX_DIRECT_APP_ID = ''
    YANDEX_DIRECT_TOKEN = ''
    YANDEX_DIRECT_SANDBOX = True

3. Enjoy

.. code-block:: python

    from yandex_direct import api
    from pprint import pprint

    # Pythonic style
    pprint(api.get_regions().get('data'))

    # Native API style
    pprint(api.PingAPI().get('data'))
