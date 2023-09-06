#!/usr/bin/python3

# Script Name:                  Ops 401d8 Challenge 42
# Author:                       David Prutch
# Date of latest revision:      09/06/2023
# Purpose:                      This script is taken from a starter template, original author unknown.
#                               Modifications:
                                # Added input prompt for the IP address.
                                # Added input prompt for the scan type (1 for SYN ACK Scan, 2 for UDP Scan, 3 for Custom Scan).
                                # Implemented SYN ACK Scan (Option 1):
                                    # Displayed Nmap version.
                                    # Performed a SYN ACK scan for open TCP ports in the range 1-50.
                                    # Displayed scan information, IP status, detected protocols, and open TCP ports.
                                # Implemented UDP Scan (Option 2):
                                    # Displayed Nmap version.
                                    # Performed a UDP scan for open UDP ports in the range 1-50.
                                    # Displayed scan information, IP status, detected protocols, and open UDP ports.
                                # Implemented Custom Scan (Option 3):
                                    # Prompted the user to enter a custom port range and stored it in the custom_range variable.
                                    # Displayed Nmap version.
                                    # Performed a scan for open ports in the custom range.
                                    # Displayed scan information, IP status, detected protocols, and open ports (both TCP and UDP).
                                # Handled invalid input by providing a message when the user selects an option outside the range 1-3.

# Import the nmap library
import nmap

# Create an instance of the PortScanner class from nmap
scanner = nmap.PortScanner()

# Print a welcome message
print("Nmap Automation Tool")
print("--------------------")

# Prompt the user to enter the IP address to scan
ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

# Prompt the user to select a scan type
resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Custom Scan\n""")
print("You have selected option: ", resp)

# Perform actions based on the user's choice
if resp == '1':
    # SYN ACK Scan
    # Display Nmap version
    print("Nmap Version: ", scanner.nmap_version())
    # Scan for open TCP ports in the range 1-50 using SYN ACK
    scanner.scan(ip_addr, '1-50', '-v -sS')
    # Display scan information
    print(scanner.scaninfo())
    # Display IP status
    print("Ip Status: ", scanner[ip_addr].state())
    # Display detected protocols
    print(scanner[ip_addr].all_protocols())
    # Display open TCP ports
    print("Open TCP Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    # UDP Scan
    # Display Nmap version
    print("Nmap Version: ", scanner.nmap_version())
    # Scan for open UDP ports in the range 1-50
    scanner.scan(ip_addr, '1-50', '-v -sU')
    # Display scan information
    print(scanner.scaninfo())
    # Display IP status
    print("Ip Status: ", scanner[ip_addr].state())
    # Display detected protocols
    print(scanner[ip_addr].all_protocols())
    # Display open UDP ports
    print("Open UDP Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    # Custom Scan
    # Prompt the user to enter a custom port range
    custom_range = input("Enter custom port range (e.g., 1-100): ")
    # Display Nmap version
    print("Nmap Version: ", scanner.nmap_version())
    # Scan for open ports in the custom range
    scanner.scan(ip_addr, custom_range, '-v')
    # Display scan information
    print(scanner.scaninfo())
    # Display IP status
    print("Ip Status: ", scanner[ip_addr].state())
    # Display detected protocols
    print(scanner[ip_addr].all_protocols())
    # Display open ports
    for protocol in scanner[ip_addr]:
        if protocol in ['tcp', 'udp']:
            print(f"Open {protocol.upper()} Ports: ", scanner[ip_addr][protocol].keys())
else:
    # Handle invalid input
    print("Please enter a valid option")
