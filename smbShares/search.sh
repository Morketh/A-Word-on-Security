#!/bin/bash

# Scan the entire subnet and find accessible M$ shares and display them in a table

SHARE_USER=tech
SHARE_PASSWORD=tech
IPRANGE=192.168.0.1-255

nmap -T4 -v -oA myshares --script smb-enum-shares --script-args smbuser=$SHARE_USER,smbpass=$SHARE_PASSWORD -p445 $IPRANGE

cat sharescan.nmap|grep '|\|192'|awk '/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/ { line=$0 } /\|/ { $0 = line $0}1'|grep \||grep -v -E '(smb-enum-shares|access: <none>|ADMIN\$|C\$|IPC\$|U\$|access: READ)'|awk '{ sub(/Nmap scan report for /, ""); print }'
