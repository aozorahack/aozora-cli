import requests
import os

AOZORAPI_HOST = os.environ.get("AOZORAPI_HOST", "www.aozorahack.net")
AOZORAPI_URL = "http://{}/api/v0.1".format(AOZORAPI_HOST)

def main():
     print("Start aozora command line tool")

def get_books(id=None, payload=None):
    url = _create_api_url("books", id)
    return requests.get(url, params=payload)

def get_persons(id=None, payload=None):
    url = _create_api_url("persons", id)
    return requests.get(url, params=payload)

def get_content(id, payload=None):
    url = _create_api_url("books", id)
    url += '/content'
    return requests.get(url, params=payload, allow_redirects=True)

def _create_api_url(path, id=None):
    url = AOZORAPI_URL + "/" + path
    if id != None:
        url += "/{}".format(id)
    return url

