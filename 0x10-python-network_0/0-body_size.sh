#!/usr/bin/env bash
# gets body size of request response
curl $1 -I | grep Content-Length | cut -f2 -d' '
