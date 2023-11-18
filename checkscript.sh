#!/bin/bash

# Script Name: checkscript
# Author: Ryan Sundermeyer
# Date: 11/17/2023
# Description: Checks to make sure a certain file exists in a certain directory

# check to make sure script is called in correct directory
if [ -e "launch.py" ]; then
    # check for file in vision
    if [ -e "vision/vision/vision_main.py" ]; then
        echo "Check passed: vision_main.py exists in directory"
    else
        echo "Check failed: vision_main.py does not exist in directory"
    fi
else
    echo "Incorrect working directory: Missing launch.py"
fi