#!/usr/bin/python3
"""searches a letter and prints response if it is JSON formatted and
not empty"""

import sys
import requests

if __name__ == "__main__":
    q = sys.argv[1]
    r = requests.get(
        "https://swapi.co/api/people/?search={}".format(q))
    r_json = r.json()
    print("Number of results: {}".format(r_json.get("count")))
    try:
        for item in r_json.get("results"):
            print(item.get("name"))
    except:
        pass
