#!/usr/bin/env python3

"""
Symmetric Encryption Tool
This script demonstrates AES symmetric encryption with different modes
and allows users to experiment with encryption and decryption.
"""

import os
import time
import base64
import json
from getpass import getpass
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from colorama import init, Fore, Style

# Initialize colorama
init()

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the tool header"""
    clear_screen()
    print(Fore.CYAN + "=" * 60)
    print(" ENCRYPTION PLAYGROUND - SYMMETRIC ENCRYPTION ")
    print("=" * 60 + Style.RESET_ALL)
    print(Fore.YELLOW + "\nThis tool demonstrates AES symmetric encryption.\n" + Style.RESET_ALL)

def generate_key(size=16):
    """Generate a random encryption key"""
    return get_random_bytes(size)

def string_to_bytes(data):
    """Convert string to bytes if needed"""
    if isinstance(data, str):
        return data.encode('utf-8')
    return data

def bytes_to_base64(data):
    """Convert bytes to base64 string"""
    return base64.b64encode(data).decode('utf-8')

def base64_to_bytes(data):
    """Convert base64 string to bytes"""
    return base64.b64decode(data.encode('utf-8'))

def encrypt_aes_cbc(plaintext, key, iv=None):
    """Encrypt data using AES-CBC mode"""
    plaintext = string_to_bytes(plaintext)
    
    # Generate IV if not provided
    if iv is None:
        iv = get_random_bytes(16)
    
    # Create cipher and encrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    
    # Return IV and ciphertext
    return {
        'iv': bytes_to_base64(iv),
        'ciphertext': bytes_to_base64(ciphertext),
        'mode': 'CBC'
    }

def decrypt_aes_cbc(iv, ciphertext, key):
    """Decrypt data using AES-CBC mode"""
    iv = base64_to_bytes(iv)
    ciphertext = base64_to_bytes(ciphertext)
    
    # Create cipher and decrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    return plaintext.decode('utf-8')

def encrypt_aes_ecb(plaintext, key):
    """Encrypt data using AES-ECB mode (less secure, for demonstration)"""
    plaintext = string_to_bytes(plaintext)
    
    # Create cipher and encrypt
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    
    # Return ciphertext
    return {
        'ciphertext': bytes_to_base64(ciphertext),
        'mode': 'ECB'
    }

def decrypt_aes_ecb(ciphertext, key):
    """Decrypt data using AES-ECB mode"""
    ciphertext = base64_to_bytes(ciphertext)
    
    # Create cipher and decrypt
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    return plaintext.decode('utf-8')

def encrypt_file(filename, key, mode='CBC'):
    """Encrypt file content using AES"""
    try:
        with open(filename, 'r') as f:
            plaintext = f.read()
        
        if mode == 'CBC':
            result = encrypt_aes_cbc(plaintext, key)
        else:  # ECB
            result = encrypt_aes_ecb(plaintext, key)
        
        # Save the encrypted data
        output_filename = f"./encrypted_files/{os.path.basename(filename)}.enc"
        with open(output_filename, 'w') as f:
            json.dump(result, f)
        
        print(Fore.GREEN + f"\nFile encrypted and saved as {output_filename}" + Style.RESET_ALL)
        return output_filename
    
    except Exception as e:
        print(Fore.RED + f"Error encrypting file: {str(e)}" + Style.RESET_ALL)
        return None

def decrypt_file(filename, key):
    """Decrypt file content using AES"""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        mode = data.get('mode', 'CBC')
        
        if mode == 'CBC':
            plaintext = decrypt_aes_cbc(data['iv'], data['ciphertext'], key)
        else:  # ECB
            plaintext = decrypt_aes_ecb(data['ciphertext'], key)
        
        # Save the decrypted data
        output_filename = f"./results/{os.path.basename(filename)}.dec"
        with open(output_filename, 'w') as f:
            f.write(plaintext)
        
        print(Fore.GREEN + f"\nFile decrypted and saved as {output_filename}" + Style.RESET_ALL)
        return output_filename
    
    except Exception as e:
        print(Fore.RED + f"Error decrypting file: {str(e)}" + Style.RESET_ALL)
        return None

def interactive_encryption():
    """Interactive menu for encryption operations"""
    print_header()
    print(Fore.GREEN + "AES SYMMETRIC ENCRYPTION" + Style.RESET_ALL)
    print("AES is a symmetric encryption algorithm used to secure data.")
    print("The same key is used for both encryption and decryption.\n")
    
    while True:
        print(Fore.YELLOW + "\nChoose an action:" + Style.RESET_ALL)
        print("1. Generate a new encryption key")
        print("2. Encrypt a message")
        print("3. Decrypt a message")
        print("4. Encrypt a file")
        print("5. Decrypt a file")
        print("6. Compare CBC and ECB modes")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            key_size = input("\nSelect key size:\n1. 128-bit (16 bytes)\n2. 192-bit (24 bytes)\n3. 256-bit (32 bytes)\nChoice: ")
            
            if key_size == '1':
                size = 16
            elif key_size == '2':
                size = 24
            elif key_size == '3':
                size = 32
            else:
                print(Fore.RED + "Invalid choice, using 128-bit key." + Style.RESET_ALL)
                size = 16
            
            key = generate_key(size)
            key_hex = key.hex()
            
            print(Fore.GREEN + f"\nGenerated {size*8}-bit key: " + Style.RESET_ALL + key_hex)
            
            save = input("\nSave this key to a file? (y/n): ").lower()
            if save == 'y':
                filename = f"./keys/aes{size*8}_key_{int(time.time())}.txt"
                with open(filename, 'w') as f:
                    f.write(key_hex)
                print(f"Key saved to {filename}")
        
        elif choice == '2':
            method = input("\nProvide key as:\n1. Hex string\n2. Load from file\nChoice: ")
            
            if method == '1':
                key_hex = input("Enter the key (in hex): ").strip()
                try:
                    key = bytes.fromhex(key_hex)
                except ValueError:
                    print(Fore.RED + "Invalid hex format." + Style.RESET_ALL)
                    continue
            elif method == '2':
                key_file = input("Enter key filename: ").strip()
                try:
                    with open(key_file, 'r') as f:
                        key_hex = f.read().strip()
                    key = bytes.fromhex(key_hex)
                except (FileNotFoundError, ValueError) as e:
                    print(Fore.RED + f"Error loading key: {str(e)}" + Style.RESET_ALL)
                    continue
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                continue
            
            message = input("Enter the message to encrypt: ")
            mode = input("Select mode:\n1. CBC (recommended)\n2. ECB (less secure)\nChoice: ")
            
            if mode == '1' or mode == '':
                result = encrypt_aes_cbc(message, key)
                print(Fore.GREEN + "\nEncrypted with AES-CBC:" + Style.RESET_ALL)
                print(f"IV: {result['iv']}")
                print(f"Ciphertext: {result['ciphertext']}")
            elif mode == '2':
                result = encrypt_aes_ecb(message, key)
                print(Fore.GREEN + "\nEncrypted with AES-ECB:" + Style.RESET_ALL)
                print(f"Ciphertext: {result['ciphertext']}")
                print(Fore.YELLOW + "Note: ECB mode is less secure and not recommended for sensitive data." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                continue
            
            # Save the encrypted data
            output_filename = f"./results/message_{int(time.time())}.enc"
            with open(output_filename, 'w') as f:
                json.dump(result, f)
            print(f"Encryption saved to {output_filename}")
        
        elif choice == '3':
            method = input("\nProvide key as:\n1. Hex string\n2. Load from file\nChoice: ")
            
            if method == '1':
                key_hex = input("Enter the key (in hex): ").strip()
                try:
                    key = bytes.fromhex(key_hex)
                except ValueError:
                    print(Fore.RED + "Invalid hex format." + Style.RESET_ALL)
                    continue
            elif method == '2':
                key_file = input("Enter key filename: ").strip()
                try:
                    with open(key_file, 'r') as f:
                        key_hex = f.read().strip()
                    key = bytes.fromhex(key_hex)
                except (FileNotFoundError, ValueError) as e:
                    print(Fore.RED + f"Error loading key: {str(e)}" + Style.RESET_ALL)
                    continue
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                continue
            
            source = input("\nLoad encrypted data from:\n1. Enter manually\n2. Load from file\nChoice: ")
            
            if source == '1':
                mode = input("Select mode:\n1. CBC\n2. ECB\nChoice: ")
                
                if mode == '1':
                    iv = input("Enter the IV (base64): ").strip()
                    ciphertext = input("Enter the ciphertext (base64): ").strip()
                    try:
                        plaintext = decrypt_aes_cbc(iv, ciphertext, key)
                        print(Fore.GREEN + "\nDecrypted message: " + Style.RESET_ALL + plaintext)
                    except Exception as e:
                        print(Fore.RED + f"Decryption failed: {str(e)}" + Style.RESET_ALL)
                elif mode == '2':
                    ciphertext = input("Enter the ciphertext (base64): ").strip()
                    try:
                        plaintext = decrypt_aes_ecb(ciphertext, key)
                        print(Fore.GREEN + "\nDecrypted message: " + Style.RESET_ALL + plaintext)
                    except Exception as e:
                        print(Fore.RED + f"Decryption failed: {str(e)}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                    continue
            
            elif source == '2':
                filename = input("Enter filename: ").strip()
                try:
                    with open(filename, 'r') as f:
                        data = json.load(f)
                    
                    mode = data.get('mode', 'CBC')
                    
                    if mode == 'CBC':
                        plaintext = decrypt_aes_cbc(data['iv'], data['ciphertext'], key)
                    else:  # ECB
                        plaintext = decrypt_aes_ecb(data['ciphertext'], key)
                    
                    print(Fore.GREEN + "\nDecrypted message: " + Style.RESET_ALL + plaintext)
                except Exception as e:
                    print(Fore.RED + f"Decryption failed: {str(e)}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                continue
        
        elif choice == '4':
            method = input("\nProvide key as:\n1. Hex string\n2. Load from file\n3. Generate new key\nChoice: ")
            
            if method == '1':
                key_hex = input("Enter the key (in hex): ").strip()
                try:
                    key = bytes.fromhex(key_hex)
                except ValueError:
                    print(Fore.RED + "Invalid hex format." + Style.RESET_ALL)
                    continue
            elif method == '2':
                key_file = input("Enter key filename: ").strip()
                try:
                    with open(key_file, 'r') as f:
                        key_hex = f.read().strip()
                    key = bytes.fromhex(key_hex)
                except (FileNotFoundError, ValueError) as e:
                    print(Fore.RED + f"Error loading key: {str(e)}" + Style.RESET_ALL)
                    continue
            elif method == '3':
                key_size = input("Select key size:\n1. 128-bit\n2. 192-bit\n3. 256-bit\nChoice: ")
                if key_size == '1':
                    key = generate_key(16)
                elif key_size == '2':
                    key = generate_key(24)
                elif key_size == '3':
                    key = generate_key(32)
                else:
                    print(Fore.RED + "Invalid choice, using 128-bit key." + Style.RESET_ALL)
                    key = generate_key(16)
                
                key_hex = key.hex()
                print(Fore.GREEN + f"Generated key: " + Style.RESET_ALL + key_hex)
                filename = f"./keys/aes_key_{int(time.time())}.txt"
                with open(filename, 'w') as f:
                    f.write(key_hex)
                print(f"Key saved to {filename}")
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                continue
            
            # List sample files
            print("\nAvailable sample files:")
            sample_files = [f for f in os.listdir('.') if f.startswith('sample_text_')]
            for i, file in enumerate(sample_files, 1):
                print(f"{i}. {file}")
            
            file_choice = input("\nSelect file to encrypt (number) or enter filename: ")
            try:
                idx = int(file_choice) - 1
                if 0 <= idx < len(sample_files):
                    filename = sample_files[idx]
                else:
                    filename = file_choice
            except ValueError:
                filename = file_choice
            
            mode = input("Select mode:\n1. CBC (recommended)\n2. ECB (less secure)\nChoice: ")
            
            if mode == '1' or mode == '':
                encrypt_file(filename, key, 'CBC')
            elif mode == '2':
                encrypt_file(filename, key, 'ECB')
                print(Fore.YELLOW + "Note: ECB mode is less secure and not recommended for sensitive data." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                continue
        
        elif choice == '5':
            method = input("\nProvide key as:\n1. Hex string\n2. Load from file\nChoice: ")
            
            if method == '1':
                key_hex = input("Enter the key (in hex): ").strip()
                try:
                    key = bytes.fromhex(key_hex)
                except ValueError:
                    print(Fore.RED + "Invalid hex format." + Style.RESET_ALL)
                    continue
            elif method == '2':
                key_file = input("Enter key filename: ").strip()
                try:
                    with open(key_file, 'r') as f:
                        key_hex = f.read().strip()
                    key = bytes.fromhex(key_hex)
                except (FileNotFoundError, ValueError) as e:
                    print(Fore.RED + f"Error loading key: {str(e)}" + Style.RESET_ALL)
                    continue
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                continue
            
            # List encrypted files
            encrypted_files_dir = "./encrypted_files"
            if not os.path.exists(encrypted_files_dir):
                print(Fore.RED + "No encrypted files directory found." + Style.RESET_ALL)
                continue
            
            encrypted_files = [f for f in os.listdir(encrypted_files_dir) if f.endswith('.enc')]
            
            if not encrypted_files:
                print(Fore.RED + "No encrypted files found." + Style.RESET_ALL)
                continue
            
            print("\nAvailable encrypted files:")
            for i, file in enumerate(encrypted_files, 1):
                print(f"{i}. {file}")
            
            file_choice = input("\nSelect file to decrypt (number) or enter filename: ")
            try:
                idx = int(file_choice) - 1
                if 0 <= idx < len(encrypted_files):
                    filename = os.path.join(encrypted_files_dir, encrypted_files[idx])
                else:
                    filename = file_choice
                    if not os.path.exists(filename):
                        filename = os.path.join(encrypted_files_dir, filename)
            except ValueError:
                filename = file_choice
                if not os.path.exists(filename):
                    filename = os.path.join(encrypted_files_dir, filename)
            
            decrypt_file(filename, key)
        
        elif choice == '6':
            # Demonstrate the difference between CBC and ECB
            print(Fore.GREEN + "\nCOMPARING CBC AND ECB MODES" + Style.RESET_ALL)
            print("This will encrypt the same pattern multiple times to show the difference.")
            
            # Generate a key
            key = generate_key(16)
            key_hex = key.hex()
            print(Fore.YELLOW + f"Using key: {key_hex}" + Style.RESET_ALL)
            
            # Create a message with repeating patterns to highlight ECB weakness
            pattern = "AAAABBBBAAAABBBB"  # Repeating pattern
            message = pattern * 8
            
            # Encrypt with CBC
            print("\nEncrypting with CBC mode:")
            cbc_results = []
            for i in range(3):
                result = encrypt_aes_cbc(message, key)
                cbc_results.append(result['ciphertext'])
                print(f"Attempt {i+1}: {result['ciphertext'][:30]}...")
            
            # Encrypt with ECB
            print("\nEncrypting with ECB mode:")
            ecb_results = []
            for i in range(3):
                result = encrypt_aes_ecb(message, key)
                ecb_results.append(result['ciphertext'])
                print(f"Attempt {i+1}: {result['ciphertext'][:30]}...")
            
            # Analysis
            print(Fore.GREEN + "\nANALYSIS:" + Style.RESET_ALL)
            print("CBC mode produces different ciphertext each time due to the random IV.")
            print("ECB mode produces the same ciphertext for identical blocks of plaintext.")
            print("\nThis is why ECB is not recommended for encrypting real data, as it")
            print("does not hide data patterns in the ciphertext, which can leak information.")
            
            input("\nPress Enter to continue...")
        
        elif choice == '7':
            print("\nReturning to main menu...")
            break
        
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        
        input("\nPress Enter to continue...")
        print_header()

if __name__ == "__main__":
    # Create necessary directories if they don't exist
    os.makedirs("./encrypted_files", exist_ok=True)
    os.makedirs("./keys", exist_ok=True)
    os.makedirs("./results", exist_ok=True)
    
    interactive_encryption()
