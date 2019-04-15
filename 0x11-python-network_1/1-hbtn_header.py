#!/usr/bin/python3
"""using argument as URL, sends request and displays
value of X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        info = response.info()
        print(info.get("X-Request-Id"))
