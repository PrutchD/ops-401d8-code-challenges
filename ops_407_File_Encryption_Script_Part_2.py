# Script Name:                  Ops 401d8 Challenge 07
# Author:                       David Prutch
# Date of latest revision:      07/18/2023
# Purpose:                      Adding the following feature capabilities to script ops_406_File_Encryption_Script_Part_1.py:
                                # Recursively encrypt a single folder and all its contents.
                                # Recursively decrypt a single folder that was encrypted by this tool.
                                # Also added a function to check if key.key file exists 
                                # Uses the file if it exists
                                # creates a key and writes it to key.key file if it does not exist then uses it 

# Import Libraries
from cryptography.fernet import Fernet
import os

# Define Variables
# initialize var to end loop
continue_loop = True

# Define Functions
# Function to check for and retrieve the encryption key
def get_or_generate_key():
    key_file = 'key.key'
    key = None

    if os.path.exists(key_file):
        # Read key from file
        with open(key_file, 'rb') as file:
            key = file.read()
    else:
        # Generate new key and save it to file
        key = Fernet.generate_key()
        with open(key_file, 'wb') as file:
            file.write(key)

    return key

# Function to encrypt a file
def encrypt_file(file_path):
     # Get or generate encryption key
    key = get_or_generate_key()
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
def decrypt_file(file_path):
    # Get or generate encryption key
    key = get_or_generate_key()
    # Create Fernet cipher suite using the key
    cipher_suite = Fernet(key)

    # Read the encrypted file contents
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the file data
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    # Write the decrypted data back to the file
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Function to encrypt a string
def encrypt_string(plaintext):
    # Get or generate encryption key
    key = get_or_generate_key()
    # Create Fernet cipher suite using the key
    cipher_suite = Fernet(key)

    # Encrypt the plaintext string
    ciphertext = cipher_suite.encrypt(plaintext.encode())

    # Print the encrypted ciphertext
    print("Encrypted string:")
    print(ciphertext.decode())

# Function to decrypt a string
def decrypt_string(ciphertext):
    # Get or generate encryption key
    key = get_or_generate_key()
    # Create Fernet cipher suite using the key
    cipher_suite = Fernet(key)

    # Decrypt the ciphertext string
    decrypted_data = cipher_suite.decrypt(ciphertext.encode())

    # Print the decrypted plaintext
    print("Decrypted string:")
    print(decrypted_data.decode())

# Function to recursively encrypt files in a folder and its subfolders
def recursively_encrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path)

# Function to recursively decrypt files in a folder and its subfolders
def recursively_decrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path)

# Main 

# Begin Loop
while continue_loop == True: 
    # Display mode selection options
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Recursively encrypt a folder")
    print("6. Recursively decrypt a folder")

    # Prompt user for mode selection
    mode = int(input("Enter the mode number: "))

    # Process user selection
    if mode == 1 or mode == 2:
        file_path = input("Enter the file path: ")

        if mode == 1:
            # Encrypt the file
            encrypt_file(file_path)
            print("File encrypted successfully.")
        else:
            # Decrypt the file
            decrypt_file(file_path)
            print("File decrypted successfully.")
    elif mode == 3 or mode == 4:
        text = input("Enter the text: ")

        if mode == 3:
            # Encrypt the string
            encrypt_string(text)
        else:
            # Decrypt the string
            decrypt_string(text)
    elif mode == 5 or mode == 6:
        folder_path = input("Enter the folder path: ")
        key = get_or_generate_key()

        if mode == 5:
            recursively_encrypt_folder(folder_path)
            print("Folder recursively encrypted successfully.")
        else:
            recursively_decrypt_folder(folder_path)
            print("Folder recursively decrypted successfully.")
    else:
        print("Invalid mode selection. Please choose a valid mode.")

    # Prompt user for continue request
    ans = input("Do you wish to continue(y/n): ")
    if ans.lower() == "n":
        continue_loop = False
# End