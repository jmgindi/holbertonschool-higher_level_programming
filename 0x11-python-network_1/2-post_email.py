#!/usr/bin/python3
"""posts an email, prints response"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail_dict = {"email": sys.argv[2]}
    mail = urllib.parse.urlencode(mail_dict).encode("ascii")
    r = urllib.request.Request(url, mail)
    with urllib.request.urlopen(r) as response:
        resp = response.read()
        print(resp.decode())
