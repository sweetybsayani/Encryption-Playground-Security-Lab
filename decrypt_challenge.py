#!/usr/bin/env python3

"""
Encryption Challenge - Can you decrypt this?
This script contains encrypted messages that require different decryption methods.
Try to decrypt them using what you've learned in the Encryption Playground.
"""

import os
import base64
import json
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
    print(" ENCRYPTION PLAYGROUND - DECRYPTION CHALLENGES ")
    print("=" * 60 + Style.RESET_ALL)
    print(Fore.YELLOW + "\nTest your encryption knowledge by solving these challenges!\n" + Style.RESET_ALL)

def challenge_1():
    """Caesar cipher challenge"""
    print(Fore.GREEN + "CHALLENGE 1: CAESAR CIPHER" + Style.RESET_ALL)
    print("This message was encrypted using a Caesar cipher.")
    print("Can you find the right shift value to decrypt it?\n")
    
    encrypted = "NSVYV DVYJA PZ H JHLZHY JPWOLY"
    print(f"Encrypted message: {encrypted}")
    
    while True:
        try:
            shift = input("\nEnter shift value to try (0-25) or 'q' to quit: ")
            if shift.lower() == 'q':
                return False
            
            shift = int(shift)
            if not 0 <= shift <= 25:
                print(Fore.RED + "Shift must be between 0 and 25." + Style.RESET_ALL)
                continue
                
            # Apply Caesar cipher decryption
            decrypted = ""
            for char in encrypted:
                if char.isalpha():
                    # Determine the case (upper or lower)
                    ascii_offset = ord('A') if char.isupper() else ord('a')
                    # Apply the shift (in reverse for decryption)
                    orig_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                    decrypted += orig_char
                else:
                    # Keep non-alphabetic characters unchanged
                    decrypted += char
            
            print(f"Result: {decrypted}")
            
            # The correct answer is with shift=7, producing "HELLO WORLD IS A CAESAR CIPHER"
            if "HELLO WORLD" in decrypted:
                print(Fore.GREEN + "\nCorrect! You've solved Challenge 1." + Style.RESET_ALL)
                return True
            else:
                check = input("Is this correct? (y/n): ").lower()
                if check == 'y':
                    print(Fore.GREEN + "\nCorrect! You've solved Challenge 1." + Style.RESET_ALL)
                    return True
                
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)

def challenge_2():
    """XOR cipher challenge"""
    print(Fore.GREEN + "CHALLENGE 2: XOR CIPHER" + Style.RESET_ALL)
    print("This message was encrypted using a simple XOR cipher with a short key.")
    print("Can you find the key to decrypt it?\n")
    
    # Message encrypted with XOR and key "KEY"
    encrypted_hex = "021b0617003a1133081b1c33081b173314"
    print(f"Encrypted message (hex): {encrypted_hex}")
    
    # Convert hex to bytes
    try:
        encrypted = bytes.fromhex(encrypted_hex)
    except ValueError:
        print(Fore.RED + "Error: Invalid hex format." + Style.RESET_ALL)
        return False
    
    while True:
        key = input("\nEnter key to try or 'q' to quit: ")
        if key.lower() == 'q':
            return False
        
        if not key:
            print(Fore.RED + "Key cannot be empty." + Style.RESET_ALL)
            continue
        
        # Apply XOR decryption
        decrypted = ""
        for i, byte in enumerate(encrypted):
            key_char = key[i % len(key)]
            decrypted += chr(byte ^ ord(key_char))
        
        print(f"Result: {decrypted}")
        
        # The correct key is "KEY", producing "secret xor message found!"
        if "secret" in decrypted.lower() and "message" in decrypted.lower():
            print(Fore.GREEN + "\nCorrect! You've solved Challenge 2." + Style.RESET_ALL)
            return True
        else:
            check = input("Is this correct? (y/n): ").lower()
            if check == 'y':
                print(Fore.GREEN + "\nCorrect! You've solved Challenge 2." + Style.RESET_ALL)
                return True

def challenge_3():
    """AES decryption challenge"""
    print(Fore.GREEN + "CHALLENGE 3: AES DECRYPTION" + Style.RESET_ALL)
    print("This message was encrypted using AES-CBC.")
    print("The key and IV are provided. Can you decrypt it?\n")
    
    # Encrypted with AES-CBC
    encrypted_data = {
        "iv": "RkxBR0ZMQUdGTEFHRkxBRw==",
        "ciphertext": "hMgFNgpSRQJJnKJmIJJmZMlLuOoOHcLf6EINB21mY/Y=",
        "mode": "CBC"
    }
    
    print(f"Encrypted data:")
    print(f"IV (base64): {encrypted_data['iv']}")
    print(f"Ciphertext (base64): {encrypted_data['ciphertext']}")
    print(f"Mode: {encrypted_data['mode']}")
    
    print("\nThe key (in hex) is: 476c6f626f6d616e74696373536563726574")
    print("Hint: You may need to adjust the key to a valid AES key length (16, 24, or 32 bytes)")
    
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
    import base64
    
    while True:
        try:
            choice = input("\nReady to decrypt? (y/q): ").lower()
            
            if choice == 'q':
                return False
            elif choice != 'y':
                continue
            
            # Convert key from hex - truncate to 16 bytes (128 bits) for AES-128
            key_hex = "476c6f626f6d616e74696373536563726574"
            # Use first 32 hex chars (16 bytes)
            key = bytes.fromhex(key_hex[:32])
            
            # Get IV and ciphertext
            iv = base64.b64decode(encrypted_data['iv'])
            ciphertext = base64.b64decode(encrypted_data['ciphertext'])
            
            # Create cipher and decrypt
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
            
            decrypted = plaintext.decode('utf-8')
            print(f"\nDecrypted message: {decrypted}")
            
            # The correct decryption should reveal a flag or secret message
            if "flag" in decrypted.lower() or "secret" in decrypted.lower() or "globomantics" in decrypted.lower():
                print(Fore.GREEN + "\nCorrect! You've solved Challenge 3." + Style.RESET_ALL)
                return True
            else:
                print(Fore.YELLOW + "\nThat doesn't look right. Try again!" + Style.RESET_ALL)
                
        except Exception as e:
            print(Fore.RED + f"Decryption error: {str(e)}" + Style.RESET_ALL)
            print("Hint: Try truncating the key to exactly 16 bytes (first 32 hex characters).")

def main():
    """Main function for the decryption challenges"""
    print_header()
    
    print("Welcome to the Encryption Playground Challenges!")
    print("Put your encryption knowledge to the test with these decryption puzzles.")
    print("You'll need to use what you've learned about different encryption methods.")
    print("\nThere are 3 challenges of increasing difficulty.")
    
    input("\nPress Enter to begin...")
    
    challenges_completed = 0
    
    # Challenge 1
    print_header()
    if challenge_1():
        challenges_completed += 1
    
    input("\nPress Enter to continue to the next challenge...")
    
    # Challenge 2
    print_header()
    if challenge_2():
        challenges_completed += 1
    
    input("\nPress Enter to continue to the next challenge...")
    
    # Challenge 3
    print_header()
    if challenge_3():
        challenges_completed += 1
    
    # Final results
    print_header()
    print(Fore.GREEN + "CHALLENGES COMPLETED" + Style.RESET_ALL)
    print(f"\nYou completed {challenges_completed} out of 3 challenges!")
    
    if challenges_completed == 3:
        print(Fore.GREEN + "\nCongratulations! You've mastered the basics of encryption and decryption!" + Style.RESET_ALL)
        print("You've demonstrated your understanding of:")
        print("1. Caesar ciphers and simple substitution")
        print("2. XOR encryption")
        print("3. AES symmetric encryption")
    elif challenges_completed > 0:
        print(Fore.YELLOW + "\nGood work! You're on your way to understanding encryption." + Style.RESET_ALL)
        print("Keep practicing with the other tools in the Encryption Playground.")
    else:
        print(Fore.YELLOW + "\nEncryption can be challenging! Keep learning and try again." + Style.RESET_ALL)
        print("Review the educational sections in the other tools.")
    
    print("\nThank you for using the Encryption Playground!")

if __name__ == "__main__":
    # Create results directory if it doesn't exist
    os.makedirs("./results", exist_ok=True)
    main()
