#!/usr/bin/env python

import aozoracli.client

def main(options):
    ranking = aozoracli.client.get_ranking(options['type'], options['year'], options['month']).json()

    if ranking == None:
        print("Could not get aozora ranking data")
        return False

    if len(ranking) == 0:
        print("Not found ranking")
        return False

    return ranking

