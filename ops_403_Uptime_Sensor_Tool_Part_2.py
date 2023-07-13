#!/usr/bin/env python3

# Script Name:                  Ops 401d8 Challenge 03
# Author:                       David Prutch
# Date of latest revision:      07/12/2023
# Purpose:                      Ask the user for an email address and password to use for sending notifications.
#                               Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
#                               Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

# Import Libraries
# Import datetime Module directly from datetime Library
from datetime import datetime
# Import os Module
import os
# Import Time Module for sleep function
from time import sleep
# Import SMTP library to send email
import smtplib
# import getpass from getpass library to protect password
from getpass import getpass

# Declaration of variables
# Prompt user to input email, password and IP address
user_email = input("Please enter your email: ")
user_pass = getpass("Please enter your email password: ")
ip = input("Please enter the IP address you wish to monitor: ")
# Variables to compare last ping status vs current ping status
last_status = "unknown"
current_status = "unknown"

# Declaration of functions
# Return the current datetime progressing with thie current ping check.
def current_time():
    return datetime.now()
# Function to send alert email upon status change
def status_alert(sender_email_id, sender_email_id_password, prev_stat, current_stat, host_ip):
    # create session
    s = smtplib.SMTP("smtp.gmail.com", 587)
    # start tls for security - encryption
    s.starttls()
    # authentication
    s.login(sender_email_id, sender_email_id_password)
    # message to be sent
    content = f"""
    At {current_time()} the status of host {host_ip} has changed from {prev_stat} to {current_stat}
    """
    print(content)
    # content = "test message"
    # sending the email
    s.sendmail("security@nowhere.com", sender_email_id, content)
    # Terminating session
    s.quit
# Ping selected Network IP a single time
def system_status(target_ip):
    # Import Global Variables
    global last_status
    global current_status
    global user_email
    global user_pass
    global ip
    # Set value of current host status
    ping = os.system(f"ping -c 1 {ip}")
    # Set value of current status based on ping result
    if ping == 0:
        current_status = "up"
    else:
        current_status = "down"
    # Compare Current status to last status to determine change
    if current_status != last_status:
        # If change has occurred send alert email
        status_alert(user_email, user_pass, last_status, current_status, ip)
        last_status = current_status
    else:
        last_status = current_status


# Main
while True:
    system_status(ip)
    sleep(2)
# End