#!/usr/bin/env python3

# Script Name:                  Ops 401d8 Challenge 02
# Author:                       David Prutch
# Date of latest revision:      07/11/2023
# Purpose:                      Transmit a single ICMP (ping) packet to a specific IP every two seconds.
#                               Evaluate the response as either success or failure.
#                               Assign success or failure to a status variable.
#                               For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.

# Import Libraries
# Import datetime Module directly from datetime Library
from datetime import datetime
# Import os Module
import os
# Import Time Module for sleep function
from time import sleep

# Declaration of variables
# Store selected Network IP to check status
host_ip = "192.168.0.229"

###############
# For this code you need to enter an IP for a local machine on your network into host_ip variable string
# The above IP will only work if you have a host with that specific IP
# Have the host running at the beginning of the test and shut it down during the script execution to test the system output.
###############

# Declaration of functions
# Ping selected Network IP a single time
def system_status(target_ip):
    ping = os.system(f"ping -c 1 {host_ip}")
    # Assign success or failure to a status variable
    if ping == 0:
        system_response = "up and available"
    else:
        system_response = "down/unavailable"
    # return the response
    return system_response

# Return the current datetime progressing with thie current ping check.
def current_time():
    return datetime.now()

# Main
while True:
    print(f"At {current_time()}, the system on {host_ip} is currently {system_status(host_ip)}")
    sleep(2)
# End