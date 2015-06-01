#!/bin/bash


SCREENSHOT_DIRECTORY="screenshots/"
JSON_FILE=$1

# create directory for storing the screens if not already present
mkdir -p "$SCREENSHOT_DIRECTORY"

python ./bin/regressor.py $SCREENSHOT_DIRECTORY $JSON_FILE 2>&1

# if there are no differences, the program will exit with success
if [[ $? = 0 ]]; then
	echo "Success"
	exit 0
else 
	echo "Failure: $?"
	exit 1
fi








