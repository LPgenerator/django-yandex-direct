Django-Yandex-Direct
====================

Quick installation
------------------
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

    pprint(api.get_regions().get('data'))
