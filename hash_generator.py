#!/usr/bin/env python3

"""
Hash Function Tool
This script demonstrates various hash functions and their properties,
allowing users to explore how small changes affect hash outputs.
"""

import os
import time
import hashlib
from tabulate import tabulate
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
    print(" ENCRYPTION PLAYGROUND - HASH FUNCTIONS ")
    print("=" * 60 + Style.RESET_ALL)
    print(Fore.YELLOW + "\nThis tool demonstrates hash functions and their properties.\n" + Style.RESET_ALL)

def calculate_hash(text, algorithm):
    """Calculate hash of text using specified algorithm"""
    text_bytes = text.encode('utf-8')
    
    if algorithm == 'md5':
        hash_obj = hashlib.md5(text_bytes)
    elif algorithm == 'sha1':
        hash_obj = hashlib.sha1(text_bytes)
    elif algorithm == 'sha256':
        hash_obj = hashlib.sha256(text_bytes)
    elif algorithm == 'sha512':
        hash_obj = hashlib.sha512(text_bytes)
    elif algorithm == 'sha3_256':
        hash_obj = hashlib.sha3_256(text_bytes)
    elif algorithm == 'blake2b':
        hash_obj = hashlib.blake2b(text_bytes)
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    return hash_obj.hexdigest()

def compare_hashes(text):
    """Calculate and display hashes of text using different algorithms"""
    algorithms = ['md5', 'sha1', 'sha256', 'sha512', 'sha3_256', 'blake2b']
    
    results = []
    for algo in algorithms:
        start_time = time.time()
        hash_value = calculate_hash(text, algo)
        end_time = time.time()
        processing_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        results.append([
            algo.upper(),
            hash_value,
            len(hash_value) * 4,  # Each hex character represents 4 bits
            f"{processing_time:.2f} ms"
        ])
    
    return results

def avalanche_demonstration(text):
    """Demonstrate the avalanche effect by changing one character"""
    print(Fore.GREEN + "\nAVALANCHE EFFECT DEMONSTRATION" + Style.RESET_ALL)
    print("This shows how a small change in input produces a significantly different hash.\n")
    
    original_text = text
    modified_text = text[:-1] + chr(ord(text[-1]) + 1)  # Change the last character slightly
    
    print(f"Original text: {original_text}")
    print(f"Modified text: {modified_text}")
    print()
    
    # Calculate SHA-256 hashes
    original_hash = calculate_hash(original_text, 'sha256')
    modified_hash = calculate_hash(modified_text, 'sha256')
    
    print(f"Original SHA-256: {original_hash}")
    print(f"Modified SHA-256: {modified_hash}")
    
    # Count differing bits (approximate by comparing hex characters)
    diff_count = sum(1 for a, b in zip(original_hash, modified_hash) if a != b)
    diff_percentage = (diff_count / len(original_hash)) * 100
    
    print(f"\nDifferences: {diff_count} out of {len(original_hash)} hex digits ({diff_percentage:.1f}%)")
    print("\nThis demonstrates how even a tiny change in the input produces a completely")
    print("different hash output - a property called the 'avalanche effect'.")

def collision_likelihood():
    """Explain hash collision likelihood"""
    print(Fore.GREEN + "\nHASH COLLISION PROBABILITY" + Style.RESET_ALL)
    print("A hash collision occurs when two different inputs produce the same hash output.\n")
    
    algorithms = [
        ['MD5', '128 bits', '2^64', 'Vulnerable'],
        ['SHA-1', '160 bits', '2^80', 'Vulnerable'],
        ['SHA-256', '256 bits', '2^128', 'Secure'],
        ['SHA-512', '512 bits', '2^256', 'Very Secure'],
        ['SHA3-256', '256 bits', '2^128', 'Secure'],
        ['BLAKE2b', '512 bits', '2^256', 'Very Secure']
    ]
    
    print(tabulate(algorithms, headers=['Algorithm', 'Hash Size', 'Collision Resistance', 'Security Status']))
    
    print("\nBirthday Paradox and Collision Probability:")
    print("For a hash function with n bits of output, we expect to find a collision")
    print("after approximately 2^(n/2) inputs due to the birthday paradox.")
    print("\nThis is why MD5 (128 bits) is considered broken - collisions can be found")
    print("with approximately 2^64 operations, which is feasible with modern computing.")

def hash_passwords():
    """Demonstrate the use of hashes for password storage"""
    print(Fore.GREEN + "\nPASSWORD HASHING DEMONSTRATION" + Style.RESET_ALL)
    print("This demonstrates how passwords are securely stored using hash functions.\n")
    
    # Simple password hash storage (without salt for simplicity)
    password = input("Enter a password to hash: ")
    
    # Calculate hashes of the password
    hashes = compare_hashes(password)
    
    print("\nPassword Hashes:")
    for algo, hash_value, bits, time in hashes:
        print(f"{algo}: {hash_value}")
    
    print("\nIn a real system, passwords would be hashed with:")
    print("1. A salt (random value added to the password before hashing)")
    print("2. A slow hash function (like bcrypt, Argon2, or PBKDF2)")
    print("3. Multiple iterations to make brute force attacks harder")
    
    # Verification demonstration
    print("\nPassword Verification Demonstration:")
    verification = input("\nEnter the password again to verify: ")
    
    verification_hash = calculate_hash(verification, 'sha256')
    original_hash = calculate_hash(password, 'sha256')
    
    if verification_hash == original_hash:
        print(Fore.GREEN + "Password correct! Hashes match." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Password incorrect! Hashes don't match." + Style.RESET_ALL)
        print(f"Expected: {original_hash}")
        print(f"Got: {verification_hash}")

def hash_file():
    """Calculate hash of a file"""
    print(Fore.GREEN + "\nFILE HASH CALCULATION" + Style.RESET_ALL)
    print("This demonstrates how to calculate the hash of a file for integrity verification.\n")
    
    # List sample files
    print("Available sample files:")
    sample_files = [f for f in os.listdir('.') if f.startswith('sample_text_')]
    for i, file in enumerate(sample_files, 1):
        print(f"{i}. {file}")
    
    # Get file from user
    file_choice = input("\nSelect file to hash (number) or enter filename: ")
    try:
        idx = int(file_choice) - 1
        if 0 <= idx < len(sample_files):
            filename = sample_files[idx]
        else:
            filename = file_choice
    except ValueError:
        filename = file_choice
    
    # Check if file exists
    if not os.path.exists(filename):
        print(Fore.RED + f"File not found: {filename}" + Style.RESET_ALL)
        return
    
    # Get algorithm from user
    print("\nSelect hash algorithm:")
    print("1. MD5")
    print("2. SHA-1")
    print("3. SHA-256")
    print("4. SHA-512")
    print("5. All of the above")
    
    algo_choice = input("\nEnter your choice (1-5): ")
    
    # Define algorithms based on choice
    if algo_choice == '1':
        algorithms = ['md5']
    elif algo_choice == '2':
        algorithms = ['sha1']
    elif algo_choice == '3':
        algorithms = ['sha256']
    elif algo_choice == '4':
        algorithms = ['sha512']
    elif algo_choice == '5':
        algorithms = ['md5', 'sha1', 'sha256', 'sha512']
    else:
        print(Fore.RED + "Invalid choice. Using SHA-256." + Style.RESET_ALL)
        algorithms = ['sha256']
    
    # Calculate hash(es)
    print(f"\nCalculating hash(es) for file: {filename}")
    
    results = []
    for algo in algorithms:
        start_time = time.time()
        
        # Initialize hash object
        if algo == 'md5':
            hash_obj = hashlib.md5()
        elif algo == 'sha1':
            hash_obj = hashlib.sha1()
        elif algo == 'sha256':
            hash_obj = hashlib.sha256()
        elif algo == 'sha512':
            hash_obj = hashlib.sha512()
        
        # Read file in chunks to handle large files
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_obj.update(chunk)
        
        hash_value = hash_obj.hexdigest()
        end_time = time.time()
        processing_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        results.append([
            algo.upper(),
            hash_value,
            len(hash_value) * 4,  # Each hex character represents 4 bits
            f"{processing_time:.2f} ms"
        ])
    
    # Display results
    print("\nFile Hash Results:")
    print(tabulate(results, headers=['Algorithm', 'Hash Value', 'Bits', 'Time']))
    
    # Save results to file
    output_filename = f"./results/hash_{os.path.basename(filename)}_{int(time.time())}.txt"
    with open(output_filename, 'w') as f:
        f.write(f"Hash results for file: {filename}\n")
        f.write(f"Generated on: {time.ctime()}\n\n")
        f.write(tabulate(results, headers=['Algorithm', 'Hash Value', 'Bits', 'Time']))
    
    print(f"\nResults saved to {output_filename}")

def interactive_hashing():
    """Interactive menu for hash operations"""
    while True:
        print_header()
        print("Choose an operation:")
        print(Fore.YELLOW + "1. Compare hash algorithms" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Demonstrate avalanche effect" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Learn about hash collisions" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Password hashing demo" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Calculate file hash" + Style.RESET_ALL)
        print(Fore.YELLOW + "6. Exit" + Style.RESET_ALL)
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            print_header()
            print(Fore.GREEN + "HASH ALGORITHM COMPARISON" + Style.RESET_ALL)
            print("This lets you compare the output of different hash functions.\n")
            
            text = input("Enter text to hash: ")
            
            results = compare_hashes(text)
            print("\nHash Results:")
            print(tabulate(results, headers=['Algorithm', 'Hash Value', 'Bits', 'Time']))
            
            # Save results to file
            output_filename = f"./results/hash_comparison_{int(time.time())}.txt"
            with open(output_filename, 'w') as f:
                f.write(f"Hash comparison for: '{text}'\n")
                f.write(f"Generated on: {time.ctime()}\n\n")
                f.write(tabulate(results, headers=['Algorithm', 'Hash Value', 'Bits', 'Time']))
            
            print(f"\nResults saved to {output_filename}")
        
        elif choice == '2':
            print_header()
            text = input("Enter text to demonstrate avalanche effect: ")
            avalanche_demonstration(text)
        
        elif choice == '3':
            print_header()
            collision_likelihood()
        
        elif choice == '4':
            print_header()
            hash_passwords()
        
        elif choice == '5':
            print_header()
            hash_file()
        
        elif choice == '6':
            print("\nReturning to main menu...")
            break
        
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Create results directory if it doesn't exist
    os.makedirs("./results", exist_ok=True)
    interactive_hashing()
