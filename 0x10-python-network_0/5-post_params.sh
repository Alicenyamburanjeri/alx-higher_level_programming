#!/bin/bash
# A bash script that sends a POST requested to the passed URL
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
