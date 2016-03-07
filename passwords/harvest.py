#!/usr/bin/env python
import os
import sys
sys.path.append("/usr/share/creddump/")
from framework.win32.hashdump import dump_file_hashes

datapath='/media/data/'
hive_path='/WINDOWS/system32/config'
target=["/SAM", "/system", "/SECURITY"]

# scrape out base path for the HDD
dirnames = [name for name in os.listdir(datapath) if os.path.isdir(os.path.join(datapath, name))]

# Attach "Windows/system32/config" for the extended name
# Start pulling SAM, SYSTEM, SECURITY hives for the hash scraper
for name in dirnames:
	hive=datapath + name + hive_path
	try:
#		print "DEBUG: SYSTEM = %s SAM = %s" % (hive+target[1],hive+target[0])
		dump_file_hashes(hive+target[1], hive+target[0])
	except IOError as e:
#		print e
		print ""
# Save directory name to avoid duplicates (cron tab prep)

# Output data to Database (<username>:<uid>:<LM-hash>:<NTLM-hash>:<comment>:<homedir>:)
