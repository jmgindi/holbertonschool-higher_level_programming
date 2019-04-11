#!/bin/bash
# sends a GET request with a custom header variable
curl -s $1 -H "X-HolbertonSchool-User-Id: 98"
