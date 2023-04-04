#!/bin/bash
# A bash script that sends a POST requested to the passed URL
curl -s -X POST -d "email-test@gmail.com&subject-I will always be here for PLD" "$1"
