#!/usr/bin/env python
import os
import sys
sys.path.append("/usr/share/creddump/")
from framework.win32.hashdump import dump_file_hashes

DEBUG=False

datapath='/media/data/'
SAMpath=["windows", "system32", "config"]
target=["sam", "system", "security"]

pathtmp=''

#gets a directory by name regardless of case
def getdirectory(path, dirname):
	list = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
	for d in list:
		if d.lower() == dirname:
			if DEBUG:
				print "getdirectory() d.lower() returns: %s" % (d)
			return d

# gets a name of a file regardless of case and returns it
def gethive(path, name):
	files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	for f in files:
		if f.lower() == name:
			if DEBUG:
				print "gethive() f.lower() returns: %s" % (f)
			return f

# scrape out base path for the HDD
drives = [name for name in os.listdir(datapath) if os.path.isdir(os.path.join(datapath, name))]

# Attach "Windows/system32/config" for the extended name
# Start pulling SAM, SYSTEM, SECURITY hives for the hash scraper
for d in drives:
        base=datapath + d
	pathtmp=base
	win=getdirectory(pathtmp, SAMpath[0]) # grab WINDOWS
	if win is not None:
		pathtmp=base+'/'+win
	sys=getdirectory(pathtmp, SAMpath[1]) # grab System32
	if sys is not None:
		pathtmp=base+'/'+win+'/'+sys
	con=getdirectory(pathtmp, SAMpath[2]) # grab Config
	if con is not None:
		pathtmp=base+'/'+win+'/'+sys+'/'+con
		sam = gethive(pathtmp,target[0])
		system = gethive(pathtmp,target[1])
		if sam is not None:
			if system is not None:
				try:
					if DEBUG:
						print "HIVE: SYSTEM = %s SAM = %s" % (pathtmp+'/'+system, pathtmp+'/'+sam)
			                dump_file_hashes(pathtmp+'/'+system, pathtmp+'/'+sam)
				except IOError as e:
					print e
#				        print ""

# Output data to Database (<username>:<uid>:<LM-hash>:<NTLM-hash>:<comment>:<homedir>:)
