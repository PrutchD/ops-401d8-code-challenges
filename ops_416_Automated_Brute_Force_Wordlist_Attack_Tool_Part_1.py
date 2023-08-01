#!/usr/bin/env python3

# Script Name:                  Ops 401d8 Challenge 16
# Author:                       David Prutch
# Date of latest revision:      07/31/2023
# Purpose:                      Mode 1: Offensive; Dictionary Iterator

                                # Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
                                    # Add a delay between words.
                                    # Print to the screen the value of the variable.
                                    # Mode 2: Defensive; Password Recognized

                                # Accepts a user input string.
                                    # Accepts a user input word list file path.
                                    # Search the word list for the user input string.
                                    # Print to the screen whether the string appeared in the word list.

# Import Libraries
import time
from getpass import getpass

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
# Main
print("Choose a mode:")
print("1. Offensive (Dictionary Iterator)")
print("2. Defensive (Password Recognized)")

# Read the chosen mode number
mode = int(input("Enter mode number: "))

if mode == 1:
    # Call offensive_mode function
    offensive_mode()
elif mode == 2:
    # Call defensive_mode function
    defensive_mode()
else:
    # Print an error message if an invalid mode number is entered
    print("Invalid mode number. Please choose 1 or 2.")
#End