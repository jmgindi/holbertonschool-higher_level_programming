#!/usr/bin/python3
"""sends get request, returns response including error codes"""

import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
