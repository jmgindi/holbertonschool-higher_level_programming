#!/usr/bin/python3
"""searches a letter and prints response if it is JSON formatted and
not empty"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv[1]) == 1:
        q = sys.argv[1]
    else:
        q = ""
    mydict = {'q': q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=mydict)
    if r.status_code != requests.codes.ok or len(r.text) <= 0:
        print("No result")
    else:
        try:
            resp = r.json()
            if len(resp) == 0:
                print("No result")
            else:
                r_id = resp.get("id")
                r_name = resp.get("name")
                print("[{}] {}".format(r_id, r_name))
        except ValueError:
            print("Not a valid JSON")
