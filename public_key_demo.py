#!/usr/bin/env python3

"""
Public Key Encryption Demonstration
This script demonstrates asymmetric (public key) encryption using RSA,
allowing users to understand the difference between symmetric and asymmetric encryption.
"""

import os
import time
import base64
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
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
    print(" ENCRYPTION PLAYGROUND - PUBLIC KEY ENCRYPTION ")
    print("=" * 60 + Style.RESET_ALL)
    print(Fore.YELLOW + "\nThis tool demonstrates public key (asymmetric) encryption.\n" + Style.RESET_ALL)

def generate_key_pair(size=2048):
    """Generate an RSA key pair"""
    print(f"Generating {size}-bit RSA key pair... This may take a moment.")
    key = RSA.generate(size)
    return key

def save_key_pair(key, basename):
    """Save a key pair to files"""
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    private_key_file = f"./keys/{basename}_private.pem"
    public_key_file = f"./keys/{basename}_public.pem"
    
    with open(private_key_file, 'wb') as f:
        f.write(private_key)
    
    with open(public_key_file, 'wb') as f:
        f.write(public_key)
    
    print(f"Private key saved to: {private_key_file}")
    print(f"Public key saved to: {public_key_file}")
    
    return private_key_file, public_key_file

def load_key(key_file):
    """Load a key from a file"""
    with open(key_file, 'rb') as f:
        key_data = f.read()
    
    return RSA.import_key(key_data)

def encrypt_message(message, public_key):
    """Encrypt a message using RSA public key"""
    message_bytes = message.encode('utf-8')
    
    # Create cipher object using the public key
    cipher = PKCS1_OAEP.new(public_key)
    
    # Encrypt the message
    ciphertext = cipher.encrypt(message_bytes)
    
    # Convert to base64 for easier handling
    encoded_ciphertext = base64.b64encode(ciphertext).decode('utf-8')
    
    return encoded_ciphertext

def decrypt_message(encoded_ciphertext, private_key):
    """Decrypt a message using RSA private key"""
    # Convert from base64
    ciphertext = base64.b64decode(encoded_ciphertext.encode('utf-8'))
    
    # Create cipher object using the private key
    cipher = PKCS1_OAEP.new(private_key)
    
    # Decrypt the message
    try:
        message_bytes = cipher.decrypt(ciphertext)
        return message_bytes.decode('utf-8')
    except Exception as e:
        print(Fore.RED + f"Decryption failed: {str(e)}" + Style.RESET_ALL)
        return None

def sign_message(message, private_key):
    """Sign a message using RSA private key"""
    message_bytes = message.encode('utf-8')
    
    # Create hash of the message
    h = SHA256.new(message_bytes)
    
    # Sign the hash with the private key
    signature = pkcs1_15.new(private_key).sign(h)
    
    # Convert to base64 for easier handling
    encoded_signature = base64.b64encode(signature).decode('utf-8')
    
    return encoded_signature

def verify_signature(message, encoded_signature, public_key):
    """Verify a signature using RSA public key"""
    message_bytes = message.encode('utf-8')
    
    # Convert from base64
    signature = base64.b64decode(encoded_signature.encode('utf-8'))
    
    # Create hash of the message
    h = SHA256.new(message_bytes)
    
    # Verify the signature with the public key
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

def visual_representation():
    """Show a visual representation of the public key encryption process"""
    print(Fore.GREEN + "\nRSA ENCRYPTION VISUAL REPRESENTATION" + Style.RESET_ALL)
    print("Here's a simplified visualization of how RSA works:\n")
    
    print("1. Key Generation:")
    print("   ┌─────────────────┐")
    print("   │ Generate Primes │")
    print("   │    p and q      │")
    print("   └────────┬────────┘")
    print("            ↓")
    print("   ┌─────────────────┐")
    print("   │  Calculate n    │")
    print("   │    n = p × q    │")
    print("   └────────┬────────┘")
    print("            ↓")
    print("   ┌─────────────────┐      ┌─────────────────┐")
    print("   │ Public Key (e,n)│      │Private Key (d,n)│")
    print("   └────────┬────────┘      └────────┬────────┘")
    print("            │                        │")
    print("            │   Anyone can have      │")
    print("            │   ← ← ← ← ← ← ←        │")
    print("            │                        │")
    print("            │       Keep secret      │")
    print("            │                        │")
    
    print("\n2. Encryption and Decryption:")
    print("   ┌─────────────┐    ┌──────────────┐    ┌──────────────┐")
    print("   │   Message   │ → →│  PUBLIC KEY  │→ → │  Encrypted   │")
    print("   │     M       │    │  (e, n)      │    │   Message    │")
    print("   └─────────────┘    └──────────────┘    └───────┬──────┘")
    print("                                                  │")
    print("   ┌─────────────┐    ┌──────────────┐           │")
    print("   │   Message   │← ← │ PRIVATE KEY  │← ← ← ← ← ← ┘")
    print("   │     M       │    │   (d, n)     │")
    print("   └─────────────┘    └──────────────┘")
    
    print("\n3. Digital Signature:")
    print("   ┌─────
