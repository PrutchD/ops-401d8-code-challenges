#!/usr/bin/env python3

# Script Name:                  Ops 401d8 Challenge 06
# Author:                       David Prutch
# Date of latest revision:      07/17/2023
# Purpose:                      Prompt the user to select a mode:
                                # Encrypt a file (mode 1)
                                # Decrypt a file (mode 2)
                                # Encrypt a message (mode 3)
                                # Decrypt a message (mode 4)
                                # If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
                                # If mode 3 or 4 are selected, prompt the user to provide a cleartext string.

# Import Libraries
from cryptography.fernet import Fernet

# Define Variables
# generate key and store in a var
key = Fernet.generate_key()
# initialize var to end loop
continue_loop = True

# Define Functions
# Function to encrypt a file
def encrypt_file(file_path, key):
    # Create Fernet cipher suite using the key
    cipher_suite = Fernet(key)

    # Read the file contents
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the file data
    encrypted_data = cipher_suite.encrypt(file_data)

    # Write the encrypted data back to the file
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(file_path, key):
    # Read the encrypted file contents
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    # Create Fernet cipher suite using the key
    cipher_suite = Fernet(key)

    # Decrypt the file data
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    # Write the decrypted data back to the file
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Function to encrypt a string
def encrypt_string(plaintext, key):
    # Create Fernet cipher suite using the key
    cipher_suite = Fernet(key)

    # Encrypt the plaintext string
    ciphertext = cipher_suite.encrypt(plaintext.encode())

    # Print the encrypted ciphertext
    print("Encrypted string:")
    print(ciphertext.decode())

# Function to decrypt a string
def decrypt_string(ciphertext, key):
    # Create Fernet cipher suite using the key
    cipher_suite = Fernet(key)

    # Decrypt the ciphertext string
    decrypted_data = cipher_suite.decrypt(ciphertext.encode())

    # Print the decrypted plaintext
    print("Decrypted string:")
    print(decrypted_data.decode())

# Main 

# Begin Loop
while continue_loop == True: 
    # Display mode selection options
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")

    # Prompt user for mode selection
    mode = int(input("Enter the mode number: "))

    # Process user selection
    if mode == 1 or mode == 2:
        file_path = input("Enter the file path: ")

        if mode == 1:
            # Encrypt the file
            encrypt_file(file_path, key)
            print("File encrypted successfully.")
        else:
            # Decrypt the file
            decrypt_file(file_path, key)
            print("File decrypted successfully.")
    elif mode == 3 or mode == 4:
        text = input("Enter the text: ")

        if mode == 3:
            # Encrypt the string
            encrypt_string(text, key)
        else:
            # Decrypt the string
            decrypt_string(text, key)
    else:
        print("Invalid mode selection. Please choose a valid mode.")

    # Prompt user for continue request
    ans = input("Do you wish to continue(y/n): ")
    if ans.lower() == "n":
        continue_loop = False
# End
