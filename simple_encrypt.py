#!/usr/bin/env python3

"""
Simple Encryption Tool
This script demonstrates basic encryption techniques like Caesar cipher
and introduces encryption concepts in a simple, interactive format.
"""

import os
import time
import string
from colorama import init, Fore, Style

# Initialize colorama
init()

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def caesar_cipher(text, shift, decrypt=False):
    """Encrypt or decrypt text using Caesar cipher"""
    if decrypt:
        shift = -shift
    
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine the case (upper or lower)
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Apply the shift
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

def xor_cipher(text, key):
    """Encrypt or decrypt text using XOR cipher"""
    result = ""
    key_length = len(key)
    
    for i, char in enumerate(text):
        # XOR the character with the corresponding key character
        key_char = key[i % key_length]
        xor_value = ord(char) ^ ord(key_char)
        result += chr(xor_value)
    
    return result

def simple_substitution(text, encrypt=True):
    """
    Simple substitution cipher - replace each letter with another
    This is a very simple implementation for demonstration
    """
    original_alphabet = string.ascii_lowercase
    cipher_alphabet = "qwertyuiopasdfghjklzxcvbnm"  # Shuffled alphabet
    
    if not encrypt:
        # Swap alphabets for decryption
        original_alphabet, cipher_alphabet = cipher_alphabet, original_alphabet
    
    translation_table = str.maketrans(original_alphabet + original_alphabet.upper(), 
                                    cipher_alphabet + cipher_alphabet.upper())
    
    return text.translate(translation_table)

def print_header():
    """Print the tool header"""
    clear_screen()
    print(Fore.CYAN + "=" * 60)
    print(" ENCRYPTION PLAYGROUND - BASIC ENCRYPTION METHODS ")
    print("=" * 60 + Style.RESET_ALL)
    print(Fore.YELLOW + "\nThis tool demonstrates simple encryption techniques.\n" + Style.RESET_ALL)

def caesar_menu():
    """Interactive Caesar cipher menu"""
    print_header()
    print(Fore.GREEN + "CAESAR CIPHER" + Style.RESET_ALL)
    print("The Caesar cipher shifts each letter by a fixed number of positions.")
    print("For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', etc.\n")
    
    while True:
        choice = input(Fore.YELLOW + "Choose an action:\n1. Encrypt a message\n2. Decrypt a message\n3. Test different shifts\n4. Back to main menu\n> " + Style.RESET_ALL)
        
        if choice == '1':
            message = input("\nEnter the message to encrypt: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if not 1 <= shift <= 25:
                    print(Fore.RED + "Shift must be between 1 and 25." + Style.RESET_ALL)
                    continue
            except ValueError:
                print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)
                continue
                
            encrypted = caesar_cipher(message, shift)
            print(Fore.GREEN + "\nEncrypted message: " + Style.RESET_ALL + encrypted)
            
            # Save result
            with open("./results/caesar_encrypted.txt", "w") as f:
                f.write(encrypted)
            print(f"Result saved to ./results/caesar_encrypted.txt\n")
            
        elif choice == '2':
            message = input("\nEnter the encrypted message: ")
            try:
                shift = int(input("Enter the shift value used for encryption (1-25): "))
                if not 1 <= shift <= 25:
                    print(Fore.RED + "Shift must be between 1 and 25." + Style.RESET_ALL)
                    continue
            except ValueError:
                print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)
                continue
                
            decrypted = caesar_cipher(message, shift, decrypt=True)
            print(Fore.GREEN + "\nDecrypted message: " + Style.RESET_ALL + decrypted + "\n")
            
        elif choice == '3':
            message = input("\nEnter a message to test: ")
            print("\nTesting all possible shifts:")
            
            for shift in range(1, 26):
                encrypted = caesar_cipher(message, shift)
                print(f"Shift {shift:2}: {encrypted}")
                time.sleep(0.1)  # Slight delay for effect
            
            print()
            
        elif choice == '4':
            return
        
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

def xor_menu():
    """Interactive XOR cipher menu"""
    print_header()
    print(Fore.GREEN + "XOR CIPHER" + Style.RESET_ALL)
    print("The XOR cipher uses the XOR operation to combine each character with a key.")
    print("The same key is used for both encryption and decryption.\n")
    
    while True:
        choice = input(Fore.YELLOW + "Choose an action:\n1. Encrypt a message\n2. Decrypt a message\n3. Back to main menu\n> " + Style.RESET_ALL)
        
        if choice == '1':
            message = input("\nEnter the message to encrypt: ")
            key = input("Enter an encryption key (password): ")
            
            if not key:
                print(Fore.RED + "Key cannot be empty." + Style.RESET_ALL)
                continue
                
            encrypted = xor_cipher(message, key)
            # Convert to hex for display (XOR can produce non-printable characters)
            hex_encrypted = ''.join(f'{ord(c):02x}' for c in encrypted)
            
            print(Fore.GREEN + "\nEncrypted message (hex): " + Style.RESET_ALL + hex_encrypted)
            
            # Save both the binary and hex versions
            with open("./results/xor_encrypted.bin", "wb") as f:
                f.write(encrypted.encode('utf-8', errors='ignore'))
            with open("./results/xor_encrypted.hex", "w") as f:
                f.write(hex_encrypted)
            
            print(f"Result saved to ./results/xor_encrypted.hex\n")
            
        elif choice == '2':
            choice = input("\nLoad from file or enter hex? (f/h): ").lower()
            
            if choice == 'f':
                try:
                    with open("./results/xor_encrypted.bin", "rb") as f:
                        encrypted = f.read().decode('utf-8', errors='ignore')
                except FileNotFoundError:
                    print(Fore.RED + "File not found. Encrypt a message first." + Style.RESET_ALL)
                    continue
            elif choice == 'h':
                hex_encrypted = input("Enter the encrypted message (in hex): ")
                try:
                    # Convert hex back to characters
                    encrypted = ''.join(chr(int(hex_encrypted[i:i+2], 16)) for i in range(0, len(hex_encrypted), 2))
                except ValueError:
                    print(Fore.RED + "Invalid hex format." + Style.RESET_ALL)
                    continue
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                continue
                
            key = input("Enter the decryption key (same as encryption key): ")
            
            if not key:
                print(Fore.RED + "Key cannot be empty." + Style.RESET_ALL)
                continue
                
            decrypted = xor_cipher(encrypted, key)
            print(Fore.GREEN + "\nDecrypted message: " + Style.RESET_ALL + decrypted + "\n")
            
        elif choice == '3':
            return
        
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

def substitution_menu():
    """Interactive substitution cipher menu"""
    print_header()
    print(Fore.GREEN + "SUBSTITUTION CIPHER" + Style.RESET_ALL)
    print("The substitution cipher replaces each letter with another letter.")
    print("This implementation uses a fixed substitution for demonstration.\n")
    
    while True:
        choice = input(Fore.YELLOW + "Choose an action:\n1. Encrypt a message\n2. Decrypt a message\n3. Back to main menu\n> " + Style.RESET_ALL)
        
        if choice == '1':
            message = input("\nEnter the message to encrypt: ")
            encrypted = simple_substitution(message)
            print(Fore.GREEN + "\nEncrypted message: " + Style.RESET_ALL + encrypted)
            
            # Save result
            with open("./results/substitution_encrypted.txt", "w") as f:
                f.write(encrypted)
            print(f"Result saved to ./results/substitution_encrypted.txt\n")
            
        elif choice == '2':
            message = input("\nEnter the encrypted message: ")
            decrypted = simple_substitution(message, encrypt=False)
            print(Fore.GREEN + "\nDecrypted message: " + Style.RESET_ALL + decrypted + "\n")
            
        elif choice == '3':
            return
        
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

def main_menu():
    """Main menu for the encryption tool"""
    while True:
        print_header()
        print("Choose an encryption method to explore:")
        print(Fore.YELLOW + "1. Caesar Cipher" + Style.RESET_ALL + " - Shift each letter by a fixed amount")
        print(Fore.YELLOW + "2. XOR Cipher" + Style.RESET_ALL + " - Use XOR operation with a key")
        print(Fore.YELLOW + "3. Substitution Cipher" + Style.RESET_ALL + " - Replace each letter with another")
        print(Fore.YELLOW + "4. Exit" + Style.RESET_ALL)
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            caesar_menu()
        elif choice == '2':
            xor_menu()
        elif choice == '3':
            substitution_menu()
        elif choice == '4':
            print("\nThank you for using the Encryption Playground!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
            time.sleep(1)

if __name__ == "__main__":
    # Create results directory if it doesn't exist
    os.makedirs("./results", exist_ok=True)
    main_menu()
