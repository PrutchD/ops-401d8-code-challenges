#!/usr/bin/env python3

# Script Name:                  Ops 401d8 Challenge 12
# Author:                       David Prutch
# Date of latest revision:      07/25/2023
# Purpose:                      Adding the following functionality to ops_411_Network_Security_Tool_with_Scapy_Part_1.py script
                                # User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
                                # ICMP Ping Sweep tool
                                # Prompt user for network address including CIDR block, for example “10.10.0.0/24”
                                # Careful not to populate the host bits!

                                # Create a list of all addresses in the given network
                                # Ping all addresses on the given network except for network address and broadcast address
                                # If no response, inform the user that the host is down or unresponsive.
                                # If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
                                # Otherwise, inform the user that the host is responding.
                                # Count how many hosts are online and inform the user.

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
            send_rst = sr1(IP(dst=host) / TCP(dport=port, flags="R"), verbose=False, timeout=1)
            print(f"Port {port} is OPEN.")
        elif response.getlayer(TCP).flags == 0x14:  # RST flag
            print(f"Port {port} is CLOSED.")
        else:
            print(f"Port {port} is FILTERED and silently dropped.")
    else:
        print(f"Port {port} is FILTERED and silently dropped.")

# ICMP Ping Sweep
def ping_sweep(network_address):
    print(f"Pinging hosts in the network {network_address}...")

    network = ipaddress.IPv4Network(network_address, strict=False)

    # Get the IP addresses from the network excluding the first and last addresses
    ip_addresses = list(network.hosts())[1:-1]

    online_hosts = 0

    for ip in ip_addresses:
        response = sr1(IP(dst=str(ip)) / ICMP(), verbose=False, timeout=1)

        if response is not None:
            if response.type == 0:  # ICMP Echo Reply
                online_hosts += 1
                print(f"Host {ip} is ONLINE.")
            elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
                print(f"Host {ip} is actively blocking ICMP traffic.")
            else:
                print(f"Host {ip} is responding, but with an unknown ICMP type.")
        else:
            print(f"Host {ip} is DOWN or unresponsive.")

    print(f"Total online hosts: {online_hosts}")

# Main
print("Choose a mode:")
print("1. TCP Port Range Scanner")
print("2. ICMP Ping Sweep")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    host = input("Enter the target host to scan: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    ports = range(start_port, end_port + 1)

    for port in ports:
        scan_port(host, port)

elif choice == "2":
    host = input("Enter the target host to perform ICMP Ping Sweep: ")
    network_address = input("Enter the network address (e.g., 10.10.0.0/24): ")
    ping_sweep(network_address)

else:
    print("Invalid choice. Exiting...")
# End