#!/usr/bin/python3

# Script Name:                  Ops 401d8 Challenge 45
# Author:                       David Prutch
# Date of latest revision:      09/07/2023
# Purpose:                      This script is taken from a starter template, original author unknown.
#                               Modifications:
                                # Set a specific timeout value (e.g., 5 seconds) and assigned it to the timeout variable.
                                # Prompted the user to input the host IP and port number using the input function and stored them in the hostip and portno variables, respectively.
                                # Used the socket.connect method to attempt a connection to the specified host and port.
                                # Wrapped the connection attempt in a try-except block to handle potential socket errors and determine if the port is open or closed.
                                # Added pseudocode comments to explain each section of the script for better understanding.

# Import the socket module for network communication
import socket

# Create a socket object for IPv4 and TCP communication
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout value here (e.g., 5 seconds)
timeout = 5
sockmod.settimeout(timeout)

# Collect a host IP from the user
hostip = input("Enter the host IP: ")

# Collect a port number from the user and convert it to an integer data type
portno = int(input("Enter the port number: "))

# Define a function to perform port scanning
def portScanner(portno):
    try:
        # Attempt to establish a connection to the specified host and port
        sockmod.connect((hostip, portno))
        
        # If the connection is successful, the port is open
        print("Port open")
        
        # Close the socket
        sockmod.close()
    except socket.error:
        # If an error occurs during the connection attempt, the port is closed
        print("Port closed")

# Call the portScanner function with the user-specified port number
portScanner(portno)
