#!/bin/bash

# Connect to localhost and open a Dynamic SOCKS proxy on port 54321 -f run in background
ssh -f -N -D 54321 localhost

# Connect to remote host and set up a temporary proxy session for remote_localhost on port 6666
ssh admiral@uesfrp.no-ip.org -p 443 'export http_proxy=http://localhost:6666'

# Connect to server on port -p 443 and setup a reverse port forward
# Bind remote port 6666 to local port 54321 making the local SOCKS proxy availibe to the remote host
# Drop out to remote shell

ssh admiral@uesfrp.no-ip.org -p 443 -R6666:localhost:54321

