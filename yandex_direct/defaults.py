# -*- coding: utf-8 -*-

from django.conf import settings


def get_settings(key, default):
    return getattr(settings, key, default)


LOGIN = get_settings("YANDEX_DIRECT_LOGIN", '')
APP_ID = get_settings("YANDEX_DIRECT_APP_ID", '')
TOKEN = get_settings("YANDEX_DIRECT_TOKEN", '')
LOCALE = get_settings("YANDEX_DIRECT_LOCALE", 'ru')
SANDBOX = get_settings("YANDEX_DIRECT_SANDBOX", False)
SANDBOX_URL = get_settings(
    "YANDEX_DIRECT_SANDBOX_URL",
    "https://api-sandbox.direct.yandex.ru/live/v4/json/")
PROD_URL = get_settings(
    "YANDEX_DIRECT_PROD_URL",
    "https://api.direct.yandex.ru/live/v4/json/")
AUTH_URL = '"https://oauth.yandex.ru/authorize?response_type=code&' \
           'client_id=%(application_id)s&state="'
