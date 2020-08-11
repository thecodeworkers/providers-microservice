import requests

class Fetch():
    def __init__(self, uri, method='GET', data=None, params=None, headers=None):
        self._uri = uri
        self._method = method
        self._data = data
        self._params = params
        self._headers = headers

    def prepare(self):
        try:
            prepare_request = requests.Request(self._method, self._uri, data=self._data, headers=self._headers).prepare()
            params_encoded = prepare_request.body

            return params_encoded

        except Exception as error:
            return error

    def send(self):
        try:
            api_request = requests.request(self._method, self._uri, data=self._data, headers=self._headers)
            response = api_request.json()

            api_request.raise_for_status()

            return response

        except requests.exceptions.RequestException as e:
            return response
