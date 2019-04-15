#!/usr/bin/python3
"""gets X-Request-Id header value"""

import requests
import sys

if __name__ == "__main__":
    head = requests.get(sys.argv[1]).headers
    print(head.get("X-Request-Id"))
