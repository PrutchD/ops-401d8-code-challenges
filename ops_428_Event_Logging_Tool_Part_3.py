#!/usr/bin/env python3

# Script Name:                  Ops 401d8 Challenge 28
# Author:                       David Prutch
# Date of latest revision:      08/16/2023
# Purpose:                      This Script adds logging functionality to ops_426_Event_Logging_Tool_Part_2.py using the logging library
#                               Use StreamHandler and FileHandler in your Python script.
#                               FileHandler should write to a local file.
#                               StreamHandler should output to the terminal.

#Import Libraries
import logging
from logging.handlers import RotatingFileHandler
from scapy.all import sr1, IP, TCP, ICMP
import sys

# Set up logging with log rotation
log_file = 'port_scanner.log'
max_log_size = 5 * 1024 * 1024  # 5 MB

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# FileHandler to write log data to a local file
file_handler = RotatingFileHandler(filename=log_file, maxBytes=max_log_size, backupCount=5)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger('').addHandler(file_handler)

# StreamHandler to output log data to the terminal
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)  # You can set the desired log level for the terminal output
stream_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
logging.getLogger('').addHandler(stream_handler)

# Disable the default root logger StreamHandler to prevent duplicate output
logging.getLogger('').handlers = [file_handler, stream_handler]

# Define Variables
host = "scanme.nmap.org"

# Accept port range input
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))
ports = range(start_port, end_port + 1)

# Define Functions
def scan_port(host_address, port):
    try:
        response = sr1(IP(dst=host_address) / TCP(dport=port, flags="S"), verbose=False, timeout=1)

        if response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:  # SYN-ACK flag
                logging.info(f"Port {port} is OPEN.")
            elif response.getlayer(TCP).flags == 0x14:  # RST flag
                logging.info(f"Port {port} is CLOSED.")
            else:
                logging.info(f"Port {port} is FILTERED and silently dropped.")
        else:
            logging.info(f"Port {port} is FILTERED and silently dropped.")
    except Exception as e:
        logging.error(f"Error scanning port {port}: {e}")

# Main
try:
    for port in ports:
        scan_port(host, port)
except Exception as e:
    logging.error(f"An error occurred in the main program: {e}")
