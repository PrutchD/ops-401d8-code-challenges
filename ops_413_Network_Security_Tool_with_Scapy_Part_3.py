#!/usr/bin/env python3

# Script Name:                  Ops 401d8 Challenge 13
# Author:                       David Prutch
# Date of latest revision:      07/26/2023
# Purpose:                      Making modifications to ops_412_Network_Security_Tool_with_Scapy_Part_2.py as follows:
                                # Combine the two modes (port and ping) of your network scanner script.
                                # Eliminate the choice of mode selection.
                                # Continue to prompt the user for an IP address to Host_address.
                                # Move port scan to its own function.
                                # Call the port scan function if the host is responsive to ICMP echo requests.
                                # Print the output to the screen.


# Import Libraries
from scapy.all import sr1, IP, TCP, ICMP
import sys
import ipaddress

# Define Variables

# Define Functions
# TCP Port Scanner
def scan_port(host_address, port):
    response = sr1(IP(dst=host_address) / TCP(dport=port, flags="S"), verbose=False, timeout=1)

    if response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:  # SYN-ACK flag
            send_rst = sr1(IP(dst=host_address) / TCP(dport=port, flags="R"), verbose=False, timeout=1)
            print(f"Port {port} is OPEN.")
        elif response.getlayer(TCP).flags == 0x14:  # RST flag
            print(f"Port {port} is CLOSED.")
        else:
            print(f"Port {port} is FILTERED and silently dropped.")
    else:
        print(f"Port {port} is FILTERED and silently dropped.")

# ICMP Ping Sweep
def ping_sweep(host_address):
    print(f"Scanning ports on the Host_address: {host_address}")
    response = sr1(IP(dst=host_address) / ICMP(), verbose=False, timeout=1)

    if response is not None and response.type == 0:  # ICMP Echo Reply
        print(f"host {host_address} is ONLINE.")
        print("Enter the port range you want to scan: ")
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        ports = range(start_port, end_port + 1)

        for port in ports:
            scan_port(host_address, port)
    else:
        print(f"host {host_address} is DOWN or unresponsive.")

# Main
host = input("Enter the Host Address to scan: ")
ping_sweep(host)
# End