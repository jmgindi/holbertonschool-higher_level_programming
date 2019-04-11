#!/bin/bash
# gets body size of request response
curl $1 -sI | grep Content-Length | cut -f2 -d' '
