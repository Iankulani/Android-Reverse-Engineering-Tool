
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 1 6:10:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Android Reverse Engineering Tool")
print(Fore.GREEN+font)


import os

# Function to read file contents
def read_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_size = os.path.getsize(file_path)
            buffer = file.read(file_size)
        
        print(f"File read successfully: {file_path}")

        # Basic binary analysis (looking for common patterns)
        print("Searching for suspicious strings or patterns...")

        # Example pattern: searching for a string that may indicate malicious behavior
        for i in range(file_size - 4):
            if buffer[i:i+4] == b"exec":
                print(f"Suspicious pattern 'exec' found at offset {i}")
    except IOError:
        print(f"Error opening file: {file_path}")

# Function to extract basic APK metadata
def analyze_apk(apk_path):
    try:
        with open(apk_path, 'rb') as apk_file:
            # Checking for the APK magic number (ZIP format)
            buffer = apk_file.read(4)
        
        if buffer == b'\x50\x4B\x03\x04':  # Checking for 'PK\x03\x04' header
            print("Valid APK file detected.")
        else:
            print("This does not appear to be a valid APK file.")
    except IOError:
        print(f"Error opening APK file: {apk_path}")

# Main function
def main():
    file_path = input("Enter the path to the APK or binary file to analyze:")

    if file_path.endswith(".apk"):
        print("Analyzing APK file...")
        analyze_apk(file_path)
    else:
        print("Analyzing binary file...")
        read_file(file_path)

if __name__ == "__main__":
    main()
