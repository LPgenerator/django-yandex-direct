# coding: utf-8

import simplejson
import requests

import defaults


class YandexDirectException(Exception):
    """
    Yandex.Direct api exceptions
    """


class YandexDirectNoDataException(Exception):
    """
    Raised when api result without data key
    """


class YandexDirectConnectionError(Exception):
    """
    Raised if http status code is not equal to standard 200
    """


class Api(object):
    def __init__(self):
        self.credentials = {
            "login": defaults.LOGIN,
            "application_id": defaults.APP_ID,
            "token": defaults.TOKEN,
            "locale": defaults.LOCALE,
        }
        self.method = None
        self.params = None
        self.root = None

    def __set_root(self):
        if self.root is None:
            self.root = defaults.PROD_URL
            if defaults.SANDBOX is True:
                self.root = defaults.SANDBOX_URL

    def __set_method(self, m):
        self.method = ''.join(
            map(lambda s: s[0].upper() + s[1:], m.split('_')))

    def __set_params(self, args, params=None):
        request_data = {'method': self.method, 'param': params or args}
        request_data.update(self.credentials)
        self.params = simplejson.dumps(
            request_data, ensure_ascii=False).encode('utf8')

    def __do_request(self):
        r = requests.post(self.root, data=self.params)
        if r.status_code != 200:
            raise YandexDirectConnectionError(r.status_code)

        result = r.json()
        if result.get('error_code'):
            raise YandexDirectException(result)

        if not result.get('data'):
            raise YandexDirectNoDataException(result)
        return result

    def get_auth_url(self):
        return defaults.AUTH_URL % self.credentials

    def __getattr__(self, method):
        def request_api(*args, **kwargs):
            self.__set_root()
            self.__set_method(method)
            self.__set_params(args, kwargs)
            return self.__do_request()

        return request_api


api = Api()
