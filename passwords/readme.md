Harvester.py is a little script i wrote to help in the pulling of NTLM Hashes from HDD Images. Given that HDDs are stored in a simple tree this script will append all the Windows/System32/Config paths and dump the SYSTEM and SAM hives. PWDUMP needs to be installed for this to work as this script is a simple wrapper around the pwdump python script

pwripper.sh will call harvester.py scrape out all the useless data sort it all by unique values and output 2 files: john.lst and hashcat.lst

hashcat can be called on hashcat.lst for password recovery

john the ripper can use the john.lst file for recovery

Eventualy i will have a script grab all the plaintext passwords and save them to dictionary list after the cracking processes finishes increasing the probablity of cracking future passwords by catagorizing commonly used passwords.
