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

def compare_encryption_types():
    """Compare symmetric and asymmetric encryption"""
    print(Fore.GREEN + "\nSYMMETRIC VS ASYMMETRIC ENCRYPTION" + Style.RESET_ALL)
    print("Let's compare the two main types of encryption:\n")
    
    print("SYMMETRIC ENCRYPTION:")
    print("- Uses the same key for encryption and decryption")
    print("- Examples: AES, 3DES, Blowfish")
    print("- Advantages: Fast, efficient for large data")
    print("- Disadvantages: Key distribution problem - how to securely share the key?")
    print("- Use cases: Encrypting files, database fields, secure communications after key exchange")
    
    print("\nASYMMETRIC ENCRYPTION (PUBLIC KEY):")
    print("- Uses different keys for encryption and decryption")
    print("- Examples: RSA, ECC, DSA")
    print("- Advantages: Solves key distribution problem, provides digital signatures")
    print("- Disadvantages: Much slower than symmetric, limited data size")
    print("- Use cases: Key exchange, digital signatures, secure initial communications")
    
    print("\nIN PRACTICE:")
    print("Most systems use a hybrid approach:")
    print("1. Use asymmetric encryption to securely exchange a symmetric key")
    print("2. Use the symmetric key for bulk data encryption")
    print("3. Use asymmetric encryption for digital signatures")
    print("Example: This is how HTTPS (TLS) works for secure websites")

def visual_representation():
    """Show a visual representation of the public key encryption process"""
    print(Fore.GREEN + "\nRSA ENCRYPTION VISUAL REPRESENTATION" + Style.RESET_ALL)
    print("Here's a simplified visualization of how RSA works:\n")
    
    print("1. Key Generation:")
    print("   +------------------+")
    print("   | Generate Primes  |")
    print("   |    p and q       |")
    print("   +--------+---------+")
    print("            |")
    print("   +--------+---------+")
    print("   |  Calculate n     |")
    print("   |    n = p × q     |")
    print("   +--------+---------+")
    print("            |")
    print("   +--------+---------+      +------------------+")
    print("   | Public Key (e,n) |      | Private Key (d,n)|")
    print("   +--------+---------+      +--------+---------+")
    print("            |                          |")
    print("            |   Anyone can have        |")
    print("            |   <- <- <- <- <- <-      |")
    print("            |                          |")
    print("            |       Keep secret        |")
    print("            |                          |")
    
    print("\n2. Encryption and Decryption:")
    print("   +-------------+    +--------------+    +--------------+")
    print("   |   Message   | -> |  PUBLIC KEY  |->  |  Encrypted   |")
    print("   |     M       |    |  (e, n)      |    |   Message    |")
    print("   +-------------+    +--------------+    +------+-------+")
    print("                                                 |")
    print("   +-------------+    +--------------+           |")
    print("   |   Message   |<-  | PRIVATE KEY  |<- <- <- <-+")
    print("   |     M       |    |   (d, n)     |")
    print("   +-------------+    +--------------+")
    
    print("\n3. Digital Signature:")
    print("   +-------------+    +--------------+    +--------------+")
    print("   |   Message   | -> | PRIVATE KEY  |->  |   Signature  |")
    print("   |     M       |    |   (d, n)     |    |              |")
    print("   +-------------+    +--------------+    +------+-------+")
    print("                                                 |")
    print("   +-------------+    +--------------+           |")
    print("   |  Verified?  |<-  |  PUBLIC KEY  |<- <- <- <-+")
    print("   |  (Yes/No)   |    |  (e, n)      |")
    print("   +-------------+    +--------------+")

def interactive_public_key():
    """Interactive menu for public key operations"""
    while True:
        print_header()
        print("Choose an operation:")
        print(Fore.YELLOW + "1. Generate a new key pair" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Encrypt a message" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Decrypt a message" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Create a digital signature" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Verify a digital signature" + Style.RESET_ALL)
        print(Fore.YELLOW + "6. Compare symmetric and asymmetric encryption" + Style.RESET_ALL)
        print(Fore.YELLOW + "7. Visual representation of RSA" + Style.RESET_ALL)
        print(Fore.YELLOW + "8. Exit" + Style.RESET_ALL)
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '1':
            print_header()
            print(Fore.GREEN + "GENERATE RSA KEY PAIR" + Style.RESET_ALL)
            
            # Get key size
            print("Select key size:")
            print("1. 1024 bits (faster, less secure)")
            print("2. 2048 bits (recommended)")
            print("3. 4096 bits (more secure, slower)")
            size_choice = input("\nEnter your choice (1-3): ")
            
            if size_choice == '1':
                key_size = 1024
            elif size_choice == '2' or size_choice == '':
                key_size = 2048
            elif size_choice == '3':
                key_size = 4096
            else:
                print(Fore.RED + "Invalid choice. Using 2048 bits." + Style.RESET_ALL)
                key_size = 2048
            
            # Generate key pair
            key = generate_key_pair(key_size)
            
            # Save key pair
            basename = f"rsa_{key_size}_{int(time.time())}"
            private_key_file, public_key_file = save_key_pair(key, basename)
            
            print(Fore.GREEN + "\nKey pair generated successfully!" + Style.RESET_ALL)
            print(f"Key size: {key_size} bits")
            print(f"Private key: {private_key_file}")
            print(f"Public key: {public_key_file}")
            print("\nIMPORTANT: Keep your private key secret!")
        
        elif choice == '2':
            print_header()
            print(Fore.GREEN + "ENCRYPT MESSAGE WITH PUBLIC KEY" + Style.RESET_ALL)
            
            # List available public keys
            public_keys = [f for f in os.listdir('./keys') if f.endswith('_public.pem')]
            
            if not public_keys:
                print(Fore.RED + "No public keys found. Generate a key pair first." + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            print("\nAvailable public keys:")
            for i, key_file in enumerate(public_keys, 1):
                print(f"{i}. {key_file}")
            
            # Select public key
            key_choice = input("\nSelect public key (number) or enter filename: ")
            try:
                idx = int(key_choice) - 1
                if 0 <= idx < len(public_keys):
                    key_file = os.path.join('./keys', public_keys[idx])
                else:
                    key_file = key_choice
                    if not os.path.exists(key_file):
                        key_file = os.path.join('./keys', key_file)
            except ValueError:
                key_file = key_choice
                if not os.path.exists(key_file):
                    key_file = os.path.join('./keys', key_file)
            
            # Check if file exists
            if not os.path.exists(key_file):
                print(Fore.RED + f"File not found: {key_file}" + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            # Load public key
            try:
                public_key = load_key(key_file)
            except Exception as e:
                print(Fore.RED + f"Error loading key: {str(e)}" + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            # Get message to encrypt
            message = input("\nEnter message to encrypt (max ~200 chars for 2048-bit key): ")
            
            # Check if message is too long for the key
            max_bytes = (public_key.size_in_bytes() - 42)  # 42 bytes of overhead for PKCS#1 OAEP
            if len(message.encode('utf-8')) > max_bytes:
                print(Fore.RED + f"Message too long for key size. Maximum {max_bytes} bytes." + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            # Encrypt message
            try:
                ciphertext = encrypt_message(message, public_key)
                print(Fore.GREEN + "\nEncrypted message:" + Style.RESET_ALL)
                print(ciphertext)
                
                # Save encrypted message
                output_filename = f"./results/encrypted_message_{int(time.time())}.txt"
                with open(output_filename, 'w') as f:
                    json.dump({'ciphertext': ciphertext, 'key_file': os.path.basename(key_file)}, f)
                
                print(f"\nEncrypted message saved to {output_filename}")
                print("To decrypt this message, you'll need the private key corresponding to the public key used for encryption.")
            except Exception as e:
                print(Fore.RED + f"Encryption failed: {str(e)}" + Style.RESET_ALL)
        
        elif choice == '3':
            print_header()
            print(Fore.GREEN + "DECRYPT MESSAGE WITH PRIVATE KEY" + Style.RESET_ALL)
            
            # List available private keys
            private_keys = [f for f in os.listdir('./keys') if f.endswith('_private.pem')]
            
            if not private_keys:
                print(Fore.RED + "No private keys found. Generate a key pair first." + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            print("\nAvailable private keys:")
            for i, key_file in enumerate(private_keys, 1):
                print(f"{i}. {key_file}")
            
            # Select private key
            key_choice = input("\nSelect private key (number) or enter filename: ")
            try:
                idx = int(key_choice) - 1
                if 0 <= idx < len(private_keys):
                    key_file = os.path.join('./keys', private_keys[idx])
                else:
                    key_file = key_choice
                    if not os.path.exists(key_file):
                        key_file = os.path.join('./keys', key_file)
            except ValueError:
                key_file = key_choice
                if not os.path.exists(key_file):
                    key_file = os.path.join('./keys', key_file)
            
            # Check if file exists
            if not os.path.exists(key_file):
                print(Fore.RED + f"File not found: {key_file}" + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            # Load private key
            try:
                private_key = load_key(key_file)
            except Exception as e:
                print(Fore.RED + f"Error loading key: {str(e)}" + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            # Get encrypted message
            source = input("\nLoad encrypted message from:\n1. Enter manually\n2. Load from file\nChoice: ")
            
            if source == '1':
                ciphertext = input("\nEnter encrypted message (base64): ")
            elif source == '2':
                # List encrypted files
                encrypted_files = [f for f in os.listdir('./results') if f.startswith('encrypted_message_')]
                
                if not encrypted_files:
                    print(Fore.RED + "No encrypted messages found." + Style.RESET_ALL)
                    input("\nPress Enter to continue...")
                    continue
                
                print("\nAvailable encrypted messages:")
                for i, file in enumerate(encrypted_files, 1):
                    print(f"{i}. {file}")
                
                file_choice = input("\nSelect file (number) or enter filename: ")
                try:
                    idx = int(file_choice) - 1
                    if 0 <= idx < len(encrypted_files):
                        file = os.path.join('./results', encrypted_files[idx])
                    else:
                        file = file_choice
                        if not os.path.exists(file):
                            file = os.path.join('./results', file)
                except ValueError:
                    file = file_choice
                    if not os.path.exists(file):
                        file = os.path.join('./results', file)
                
                # Check if file exists
                if not os.path.exists(file):
                    print(Fore.RED + f"File not found: {file}" + Style.RESET_ALL)
                    input("\nPress Enter to continue...")
                    continue
                
                # Load encrypted message
                try:
                    with open(file, 'r') as f:
                        data = json.load(f)
                    ciphertext = data['ciphertext']
                    print(f"Using encrypted message from {file}")
                    if 'key_file' in data:
                        print(f"This message was encrypted with {data['key_file']}")
                except Exception as e:
                    print(Fore.RED + f"Error loading file: {str(e)}" + Style.RESET_ALL)
                    input("\nPress Enter to continue...")
                    continue
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            # Decrypt message
            try:
                plaintext = decrypt_message(ciphertext, private_key)
                if plaintext:
                    print(Fore.GREEN + "\nDecrypted message:" + Style.RESET_ALL)
                    print(plaintext)
            except Exception as e:
                print(Fore.RED + f"Decryption failed: {str(e)}" + Style.RESET_ALL)
                print("This could be because you're using the wrong private key.")
        
        elif choice == '4':
            print_header()
            print(Fore.GREEN + "CREATE DIGITAL SIGNATURE" + Style.RESET_ALL)
            
            # List available private keys
            private_keys = [f for f in os.listdir('./keys') if f.endswith('_private.pem')]
            
            if not private_keys:
                print(Fore.RED + "No private keys found. Generate a key pair first." + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            print("\nAvailable private keys:")
            for i, key_file in enumerate(private_keys, 1):
                print(f"{i}. {key_file}")
            
            # Select private key
            key_choice = input("\nSelect private key (number) or enter filename: ")
            try:
                idx = int(key_choice) - 1
                if 0 <= idx < len(private_keys):
                    key_file = os.path.join('./keys', private_keys[idx])
                else:
                    key_file = key_choice
                    if not os.path.exists(key_file):
                        key_file = os.path.join('./keys', key_file)
            except ValueError:
                key_file = key_choice
                if not os.path.exists(key_file):
                    key_file = os.path.join('./keys', key_file)
            
            # Check if file exists
            if not os.path.exists(key_file):
                print(Fore.RED + f"File not found: {key_file}" + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            # Load private key
            try:
                private_key = load_key(key_file)
            except Exception as e:
                print(Fore.RED + f"Error loading key: {str(e)}" + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            # Get message to sign
            message = input("\nEnter message to sign: ")
            
            # Sign message
            try:
                signature = sign_message(message, private_key)
                print(Fore.GREEN + "\nSignature:" + Style.RESET_ALL)
                print(signature)
                
                # Save signed message
                output_filename = f"./results/signed_message_{int(time.time())}.txt"
                with open(output_filename, 'w') as f:
                    json.dump({
                        'message': message,
                        'signature': signature,
                        'key_file': os.path.basename(key_file)
                    }, f)
                
                print(f"\nSigned message saved to {output_filename}")
                print("This signature can be verified using the corresponding public key.")
            except Exception as e:
                print(Fore.RED + f"Signing failed: {str(e)}" + Style.RESET_ALL)
        
        elif choice == '5':
            print_header()
            print(Fore.GREEN + "VERIFY DIGITAL SIGNATURE" + Style.RESET_ALL)
            
            # List available public keys
            public_keys = [f for f in os.listdir('./keys') if f.endswith('_public.pem')]
            
            if not public_keys:
                print(Fore.RED + "No public keys found. Generate a key pair first." + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            print("\nAvailable public keys:")
            for i, key_file in enumerate(public_keys, 1):
                print(f"{i}. {key_file}")
            
            # Select public key
            key_choice = input("\nSelect public key (number) or enter filename: ")
            try:
                idx = int(key_choice) - 1
                if 0 <= idx < len(public_keys):
                    key_file = os.path.join('./keys', public_keys[idx])
                else:
                    key_file = key_choice
                    if not os.path.exists(key_file):
                        key_file = os.path.join('./keys', key_file)
            except ValueError:
                key_file = key_choice
                if not os.path.exists(key_file):
                    key_file = os.path.join('./keys', key_file)
            
            # Check if file exists
            if not os.path.exists(key_file):
                print(Fore.RED + f"File not found: {key_file}" + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            # Load public key
            try:
                public_key = load_key(key_file)
            except Exception as e:
                print(Fore.RED + f"Error loading key: {str(e)}" + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            # Get signed message
            source = input("\nLoad signed message from:\n1. Enter manually\n2. Load from file\nChoice: ")
            
            if source == '1':
                message = input("\nEnter the original message: ")
                signature = input("Enter the signature (base64): ")
            elif source == '2':
                # List signed files
                signed_files = [f for f in os.listdir('./results') if f.startswith('signed_message_')]
                
                if not signed_files:
                    print(Fore.RED + "No signed messages found." + Style.RESET_ALL)
                    input("\nPress Enter to continue...")
                    continue
                
                print("\nAvailable signed messages:")
                for i, file in enumerate(signed_files, 1):
                    print(f"{i}. {file}")
                
                file_choice = input("\nSelect file (number) or enter filename: ")
                try:
                    idx = int(file_choice) - 1
                    if 0 <= idx < len(signed_files):
                        file = os.path.join('./results', signed_files[idx])
                    else:
                        file = file_choice
                        if not os.path.exists(file):
                            file = os.path.join('./results', file)
                except ValueError:
                    file = file_choice
                    if not os.path.exists(file):
                        file = os.path.join('./results', file)
                
                # Check if file exists
                if not os.path.exists(file):
                    print(Fore.RED + f"File not found: {file}" + Style.RESET_ALL)
                    input("\nPress Enter to continue...")
                    continue
                
                # Load signed message
                try:
                    with open(file, 'r') as f:
                        data = json.load(f)
                    message = data['message']
                    signature = data['signature']
                    print(f"Using signed message from {file}")
                    if 'key_file' in data:
                        print(f"This message was signed with {data['key_file']}")
                        suggested_key = data['key_file'].replace('_private.pem', '_public.pem')
                        print(f"Suggested public key: {suggested_key}")
                except Exception as e:
                    print(Fore.RED + f"Error loading file: {str(e)}" + Style.RESET_ALL)
                    input("\nPress Enter to continue...")
                    continue
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                input("\nPress Enter to continue...")
                continue
            
            # Verify signature
            try:
                is_valid = verify_signature(message, signature, public_key)
                if is_valid:
                    print(Fore.GREEN + "\nSignature is valid!" + Style.RESET_ALL)
                    print("This confirms the message was signed by the owner of the corresponding private key.")
                else:
                    print(Fore.RED + "\nSignature is invalid!" + Style.RESET_ALL)
                    print("This could be because:")
                    print("1. The message was altered after signing")
                    print("2. The signature was corrupted")
                    print("3. You're using the wrong public key")
            except Exception as e:
                print(Fore.RED + f"Verification failed: {str(e)}" + Style.RESET_ALL)
        
        elif choice == '6':
            print_header()
            compare_encryption_types()
        
        elif choice == '7':
            print_header()
            visual_representation()
        
        elif choice == '8':
            print("\nReturning to main menu...")
            break
        
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Create necessary directories if they don't exist
    os.makedirs("./keys", exist_ok=True)
    os.makedirs("./results", exist_ok=True)
    
    interactive_public_key()
