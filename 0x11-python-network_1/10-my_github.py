#!/usr/bin/python3
"""uses github api to display user id based on credentials"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get("id", "None"))
