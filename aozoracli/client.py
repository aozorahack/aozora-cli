import requests
import os

AOZORAPI_HOST = os.environ.get("AOZORAPI_HOST", "153.127.202.91")
AOZORAPI_URL = "http://{}/api/v0.1".format(AOZORAPI_HOST)

def main():
     print("Start aozora command line tool")

def get_books(payload=None):
    return requests.get(AOZORAPI_URL + "/books", params=payload)
