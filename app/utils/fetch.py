import requests

def fetch(uri, params=None, headers=None):
    try:
        req = requests.get(uri, params=params, headers=headers)
        req.raise_for_status()

        return req.json()

    except requests.exceptions.RequestException as e:
        return e
