#!/usr/bin/env python
#from __future__ import print_function
import os
import sys

datapath='/media/data/'
driver_path=['windows', 'system32', 'driverstore', 'filerepository']

# scrape out base path for the HDD
drives = [name for name in os.listdir(datapath) if os.path.isdir(os.path.join(datapath, name))]

# Attach "Windows/system32/config" for the extended name
# Start pulling SAM, SYSTEM, SECURITY hives for the hash scraper
for d in drives:
        base=datapath + d
        dirs = [name for name in os.listdir(base) if os.path.isdir(os.path.join(base, name))]
        for win in dirs:
                if win.lower() == driver_path[0]:
			dir2 = [name for name in os.listdir(base+'/'+win) if os.path.isdir(os.path.join(base+'/'+win, name))]
		        for sys in dir2:
                		if sys.lower() == driver_path[1]:
					dir3 = [name for name in os.listdir(base+'/'+win+'/'+sys) if os.path.isdir(os.path.join(base+'/'+win+'/'+sys, name))]
        		                for driv in dir3:
	                	                if driv.lower() == driver_path[2]:
							dir4 = [name for name in os.listdir(base+'/'+win+'/'+sys+'/'+driv) if os.path.isdir(os.path.join(base+'/'+win+'/'+sys+'/'+driv, name))]
                                        		for repo in dir4:
		                                                if repo.lower() == driver_path[3]:
									msg = base+'/'+win+'/'+sys+'/'+driv+'/'+repo
									print msg
#									print(msg, file=sys.stdout)
#									print("Found Drivers At: ", msg, file=sys.stderr)
