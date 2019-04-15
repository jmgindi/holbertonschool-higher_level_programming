#!/usr/bin/python3
"""gets status using requests package"""

import requests

if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type {}".format(type(r)))
    print("\t- content: {}".format(r))
