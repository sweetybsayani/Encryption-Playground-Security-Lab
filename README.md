# Encryption-Playground-Security-Lab
This lab provides a hands-on environment for exploring basic encryption and decryption techniques, allowing learners to understand their strengths and weaknesses.

# Encryption Playground Lab

## Scenario

The security team at Globomantics needs to implement secure communication channels to protect sensitive information from the Dark Kittens hacking group. As a new security engineer, you've been tasked with evaluating different encryption methods to determine which ones are appropriate for various types of data.

This lab provides a hands-on environment for exploring basic encryption and decryption techniques, allowing you to understand their strengths and weaknesses.

## Lab Overview

In this lab, you will:
1. Set up a simple encryption testing environment
2. Learn about different encryption algorithms
3. Encrypt and decrypt messages using various methods
4. Compare the security of different encryption approaches
5. Make recommendations based on your findings

## Lab Network
![network-diagram-encryption (1)](https://github.com/user-attachments/assets/3061194c-bf20-49a0-9fda-d9c1b10cf0fa)


## Prerequisites

- Linux-based system (Ubuntu, Kali Linux, etc.)
- Python 3.6 or higher
- Basic command-line knowledge

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sweetybsayani/encryption-playground.git
   cd encryption-playground
   ```

2. Run the setup script:
   ```bash
   bash setup.sh
   ```

3. The setup will install required dependencies and prepare the lab environment.

## Lab Tasks

### Task 1: Explore Basic Encryption Methods
1. Run the basic encryption tool:
   ```bash
   python3 simple_encrypt.py
   ```
2. **YOUR TASK**: Encrypt a message using Caesar cipher with different shift values
3. Observe how the encrypted text changes with different shift values

### Task 2: Test Symmetric Encryption
1. Run the symmetric encryption tool:
   ```bash
   python3 symmetric_encrypt.py
   ```
2. **YOUR TASK**: Encrypt a secret message using AES encryption
3. Decrypt the message using the provided key
4. Try decrypting with an incorrect key and observe the results

### Task 3: Experiment with Hash Functions
1. Run the hashing tool:
   ```bash
   python3 hash_generator.py
   ```
2. **YOUR TASK**: Generate hashes for the same input using different algorithms
3. Compare the output length and complexity of different hash functions
4. Try to find a pattern in how the hashes change with small changes to the input

### Task 4: Explore Public Key Encryption
1. Run the public key encryption demo:
   ```bash
   python3 public_key_demo.py
   ```
2. **YOUR TASK**: Generate a key pair and encrypt a message
3. Decrypt the message using the private key
4. Understand the difference between symmetric and asymmetric encryption

### Task 5: Evaluate Encryption Methods
1. Compare the results from the previous exercises
2. **YOUR TASK**: Complete the encryption evaluation worksheet:
   ```bash
   nano encryption_evaluation.txt
   ```
3. Make recommendations for which encryption methods would be appropriate for different types of data

## Reset the Lab

To reset the lab environment to its initial state:
```bash
bash cleanup.sh
```

## Learning Objectives

- Understand basic encryption concepts and terminology
- Learn the difference between various encryption methods
- Gain hands-on experience with encryption tools
- Develop criteria for selecting appropriate encryption for different scenarios
- Identify strengths and weaknesses of different encryption approaches

## File Structure

- `README.md` - Main instructions and scenario
- `setup.sh` - Main setup script for the environment
- `simple_encrypt.py` - Basic encryption methods (Caesar cipher, etc.)
- `symmetric_encrypt.py` - Symmetric encryption demonstration (AES)
- `hash_generator.py` - Various hashing algorithms demonstration
- `public_key_demo.py` - Public key encryption demonstration (RSA)
- `encryption_helper.py` - Helper functions for the encryption tools
- `decrypt_challenge.py` - Challenge file for advanced practice
- `cleanup.sh` - Script to reset the lab environment
- `encryption_evaluation.txt` - Worksheet for evaluating encryption methods

## Completion Criteria

You've successfully completed this lab when:
1. You've encrypted and decrypted messages using different methods
2. You understand the key differences between encryption approaches
3. You can recommend appropriate encryption methods for different scenarios
4. You've completed the encryption evaluation worksheet

Good luck exploring the world of encryption!
