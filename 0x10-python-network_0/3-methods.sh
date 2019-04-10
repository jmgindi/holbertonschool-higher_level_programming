#!/usr/bin/env bash
# displays all methods the server will accept
curl -sI 0:5000/route_4 | grep Allow | cut -f2-  -d' '
