#!/bin/bash


SCREENSHOT_DIRECTORY="screenshots/"


# create directory for storing the screens if not already present
mkdir -p "$SCREENSHOT_DIRECTORY"

python ./bin/tinytester.py $SCREENSHOT_DIRECTORY 2>&1

# if there are no differences, the program will exit with success
if [[ $? = 0 ]]; then
	echo "Success"
	exit 0
else 
	echo "Failure: $?"
	exit 1
fi








