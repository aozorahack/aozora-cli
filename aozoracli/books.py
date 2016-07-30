#!/usr/bin/env python

import aozoracli.client

def main(id, name):
    books = aozoracli.client.get_books().json()

    if books == None:
        print("Could not get aozora books data")
        return False

    if id == None and name == None:
        print(books)
        return True

    if id != None:
        filtered_books = [b for b in books if b['book_id'] == id]
        if len(filtered_books) == 0:
            print("Not found books")
            return False
        print(filtered_books)
        return True

    if name != None:
        filtered_books = [b for b in books if b['title'] == name]
        if len(filtered_books) == 0:
            print("Not found books")
            return False
        print(filtered_books)
        return True

