#!/usr/bin/env python3

# Script Name:                  Ops 401d8 Challenge 07
# Author:                       David Prutch
# Date of latest revision:      07/18/2023
# Purpose:                      In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:

                                # Utilize the scapy library
                                # Define host IP
                                # Define port range or specific set of ports to scan
                                # Test each port in the specified range using a for loop
                                # If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
                                # If flag 0x14 received, notify user the port is closed.
                                # If no flag is received, notify the user the port is filtered and silently dropped

# Import Libraries
from scapy.all import sr1, IP, TCP, ICMP
import sys

# Define Variables
host = "scanme.nmap.org"
ports = (22, 23)
# Define Functions
def scan_port(host_address, port):
    response = sr1(IP(dst=host) / TCP(dport=port, flags="S"), verbose=False, timeout=1)

    if response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:  # SYN-ACK flag
            send_rst = sr1(IP(dst=host) / TCP(dport=port, flags="R"), verbose=False, timeout=1)
            print(f"Port {port} is OPEN.")
        elif response.getlayer(TCP).flags == 0x14:  # RST flag
            print(f"Port {port} is CLOSED.")
        else:
            print(f"Port {port} is FILTERED and silently dropped.")
    else:
        print(f"Port {port} is FILTERED and silently dropped.")
# Main
for port in ports:
    scan_port(host, port)
# End