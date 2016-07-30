import requests

def main():
    print("Start aozora command line tool")
    r = requests.get("http://153.127.202.91/api/v0.1/books/")
    print(r.json())
