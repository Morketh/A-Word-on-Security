#!/usr/bin/python
#
# Title: buildPassdict.py
#
# Purpose: sits in a loop and adds passwords on a speprate line of the common.dict password file
#
# Copyright (C) Andrew Malone 2016

import sys

# Open the dictionary in append mode
dict = open("common.dict","a")

# main Code Block
while True:
    try:
	print(chr(27) + "[2J") # clear screen
    	dict.write(raw_input("Add word to dictionary: "))
	dict.write('\n') # Add trailing newline to the file and then keep going
    except KeyboardInterrupt:
	print "\nKeyboardInterrupt Detected: Ending program."
        break

# Close file
dict.close()
