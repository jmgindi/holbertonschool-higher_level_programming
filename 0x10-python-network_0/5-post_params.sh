#!/bin/bash
# sends a post request with email contents and displays response body
curl -s $1 -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" 
