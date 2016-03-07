#!/usr/bin/env python
import os
import sys
sys.path.append("/usr/share/creddump/")
from framework.win32.hashdump import dump_file_hashes

datapath='/media/data/'
hive_path='/windows/system32/config'
target=["/system32/config/SAM", "/system32/config/system", "/SECURITY"]

# scrape out base path for the HDD
drives = [name for name in os.listdir(datapath) if os.path.isdir(os.path.join(datapath, name))]

# Attach "Windows/system32/config" for the extended name
# Start pulling SAM, SYSTEM, SECURITY hives for the hash scraper
for d in drives:
	base=datapath + d
	dirs = [name for name in os.listdir(base) if os.path.isdir(os.path.join(base, name))]
	for win in dirs:
		if win.lower() == 'windows':
			try:
#				print "DEBUG: SYSTEM = %s SAM = %s" % (base+'/'+win+target[1],base+'/'+win+target[0])
				dump_file_hashes(base+'/'+win+target[1], base+'/'+win+target[0])
			except IOError as e:
				print e
# Save directory name to avoid duplicates (cron tab prep)

# Output data to Database (<username>:<uid>:<LM-hash>:<NTLM-hash>:<comment>:<homedir>:)
