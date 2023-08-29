#!/usr/bin/env python3

# Script Name:                  Ops 401d8 Challenge 36
# Author:                       David Prutch
# Date of latest revision:      08/28/2023
# Purpose:                      Prompts the user to type a URL or IP address.
                                # Prompts the user to type a port number.
                                # Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.
                                # Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
                                # Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.

# Import Libraries
import subprocess, socket

# Function for banner grabbing using netcat
# Attribution to Marco Vazquez for the start to this function
def netcat_banner_grabbing(target, port):
    # create a socket and a connection AF_NET = IPv4 address, SOCK_STREAM = PORT
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((target, int(port)) )   
    # Send NetCat command
    netcat_command = f"nc {target} {port}"
    socket1.sendall(netcat_command.encode())
    socket1.shutdown(socket.SHUT_WR)    
    # handle output
    output = socket1.recv(1024)
    print(output.decode())    
    # close the socket connection
    socket1.close()


# Function for banner grabbing using telnet
def telnet_banner_grabbing(target, port):
    # create a socket and a connection AF_NET = IPv4 address, SOCK_STREAM = PORT
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((target, int(port)) ) 
    # Send Telnet Command
    telnet_command = f"telnet {target} {port}"
    socket1.sendall(telnet_command.encode())
    socket1.shutdown(socket.SHUT_WR)
    # handle output
    output = socket1.recv(1024)
    print(output.decode())    
    # close the socket connection
    socket1.close()

# Function for banner grabbing using Nmap
def nmap_banner_grabbing(target):
    nmap_command = f"nmap -Pn -p 1-1024 --script=banner {target}"
    nmap_result = subprocess.run(nmap_command, shell=True, capture_output=True, text=True)
    print("\n[Nmap Banner Grabbing]")
    print(nmap_result.stdout)

# Function to get target and port inputs
def get_target_and_port():
    target = input("Enter a URL or IP address: ")
    port = input("Enter a port number: ")
    return target, port

# Main
while True:
    # Display menu options
    print("\nSelect a banner grabbing method:")
    print("1. Netcat")
    print("2. Telnet")
    print("3. Nmap")
    print("4. Exit")
    
    # Get user choice
    choice = input("Enter your choice: ")

    if choice == "1":
        target, port = get_target_and_port()
        netcat_banner_grabbing(target, port)
    elif choice == "2":
        target, port = get_target_and_port()
        telnet_banner_grabbing(target, port)
    elif choice == "3":
        target = input("Enter a URL or IP address: ")
        nmap_banner_grabbing(target)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid option.")