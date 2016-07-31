import requests

API_HOST = "http://153.127.202.91/api/v0.1"

def get_books():
    return requests.get(API_HOST + "/books")
