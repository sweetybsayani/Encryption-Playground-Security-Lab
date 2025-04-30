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
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <!-- Background -->
  <rect width="800" height="600" fill="#f8f9fa" />
  
  <!-- Title -->
  <text x="400" y="50" font-family="Arial" font-size="24" text-anchor="middle" fill="#333">Encryption Playground - Lab Environment</text>
  
  <!-- User Section -->
  <rect x="50" y="120" width="180" height="120" fill="#e6f7ff" stroke="#0066cc" stroke-width="2" rx="10" />
  <text x="140" y="140" font-family="Arial" font-size="16" text-anchor="middle" fill="#0066cc">Security Engineer</text>
  <text x="140" y="160" font-family="Arial" font-size="12" text-anchor="middle" fill="#333">(Lab User)</text>
  
  <!-- User Icon -->
  <circle cx="140" cy="200" r="30" fill="#cce5ff" stroke="#0066cc" stroke-width="2" />
  <text x="140" y="205" font-family="Arial" font-size="24" text-anchor="middle" fill="#0066cc">👤</text>
  
  <!-- Center Platform -->
  <rect x="280" y="120" width="240" height="360" fill="#f0fff0" stroke="#006600" stroke-width="2" rx="10" />
  <text x="400" y="140" font-family="Arial" font-size="16" text-anchor="middle" fill="#006600">Encryption Playground</text>
  
  <!-- Tools Inside Platform -->
  <rect x="300" y="170" width="200" height="60" fill="#eeffee" stroke="#006600" stroke-width="1" rx="5" />
  <text x="400" y="200" font-family="Arial" font-size="14" text-anchor="middle" fill="#006600">Basic Encryption Tool</text>
  <text x="400" y="220" font-family="Arial" font-size="10" text-anchor="middle" fill="#006600">Caesar Cipher, XOR, etc.</text>
  
  <rect x="300" y="240" width="200" height="60" fill="#eeffee" stroke="#006600" stroke-width="1" rx="5" />
  <text x="400" y="270" font-family="Arial" font-size="14" text-anchor="middle" fill="#006600">Symmetric Encryption Tool</text>
  <text x="400" y="290" font-family="Arial" font-size="10" text-anchor="middle" fill="#006600">AES-256 Implementation</text>
  
  <rect x="300" y="310" width="200" height="60" fill="#eeffee" stroke="#006600" stroke-width="1" rx="5" />
  <text x="400" y="340" font-family="Arial" font-size="14" text-anchor="middle" fill="#006600">Hash Function Tool</text>
  <text x="400" y="360" font-family="Arial" font-size="10" text-anchor="middle" fill="#006600">SHA-256, MD5, SHA-3, etc.</text>
  
  <rect x="300" y="380" width="200" height="60" fill="#eeffee" stroke="#006600" stroke-width="1" rx="5" />
  <text x="400" y="410" font-family="Arial" font-size="14" text-anchor="middle" fill="#006600">Public Key Demo</text>
  <text x="400" y="430" font-family="Arial" font-size="10" text-anchor="middle" fill="#006600">RSA Encryption/Decryption</text>
  
  <!-- Storage Section -->
  <rect x="570" y="120" width="180" height="360" fill="#fff0f5" stroke="#990066" stroke-width="2" rx="10" />
  <text x="660" y="140" font-family="Arial" font-size="16" text-anchor="middle" fill="#990066">Storage</text>
  
  <!-- Storage Components -->
  <rect x="590" y="170" width="140" height="60" fill="#ffe6f2" stroke="#990066" stroke-width="1" rx="5" />
  <text x="660" y="195" font-family="Arial" font-size="14" text-anchor="middle" fill="#990066">Keys Directory</text>
  <text x="660" y="215" font-family="Arial" font-size="10" text-anchor="middle" fill="#990066">Public/Private Keys</text>
  
  <rect x="590" y="240" width="140" height="60" fill="#ffe6f2" stroke="#990066" stroke-width="1" rx="5" />
  <text x="660" y="265" font-family="Arial" font-size="14" text-anchor="middle" fill="#990066">Encrypted Files</text>
  <text x="660" y="285" font-family="Arial" font-size="10" text-anchor="middle" fill="#990066">Messages & Documents</text>
  
  <rect x="590" y="310" width="140" height="60" fill="#ffe6f2" stroke="#990066" stroke-width="1" rx="5" />
  <text x="660" y="335" font-family="Arial" font-size="14" text-anchor="middle" fill="#990066">Results Directory</text>
  <text x="660" y="355" font-family="Arial" font-size="10" text-anchor="middle" fill="#990066">Analysis & Reports</text>
  
  <rect x="590" y="380" width="140" height="60" fill="#ffe6f2" stroke="#990066" stroke-width="1" rx="5" />
  <text x="660" y="405" font-family="Arial" font-size="14" text-anchor="middle" fill="#990066">Sample Files</text>
  <text x="660" y="425" font-family="Arial" font-size="10" text-anchor="middle" fill="#990066">Test Documents</text>
  
  <!-- Arrows -->
  <!-- User to Platform -->
  <line x1="230" y1="180" x2="280" y2="180" stroke="#0066cc" stroke-width="2" />
  <polygon points="280,180 270,175 270,185" fill="#0066cc" />
  
  <!-- Platform to Storage -->
  <line x1="520" y1="200" x2="570" y2="200" stroke="#006600" stroke-width="2" />
  <polygon points="570,200 560,195 560,205" fill="#006600" />
  
  <line x1="520" y1="270" x2="570" y2="270" stroke="#006600" stroke-width="2" />
  <polygon points="570,270 560,265 560,275" fill="#006600" />
  
  <line x1="520" y1="340" x2="570" y2="340" stroke="#006600" stroke-width="2" />
  <polygon points="570,340 560,335 560,345" fill="#006600" />
  
  <line x1="520" y1="410" x2="570" y2="410" stroke="#006600" stroke-width="2" />
  <polygon points="570,410 560,405 560,415" fill="#006600" />
  
  <!-- Storage to Platform -->
  <line x1="570" y1="230" x2="520" y2="230" stroke="#990066" stroke-width="2" />
  <polygon points="520,230 530,225 530,235" fill="#990066" />
  
  <line x1="570" y1="300" x2="520" y2="300" stroke="#990066" stroke-width="2" />
  <polygon points="520,300 530,295 530,305" fill="#990066" />
  
  <line x1="570" y1="370" x2="520" y2="370" stroke="#990066" stroke-width="2" />
  <polygon points="520,370 530,365 530,375" fill="#990066" />
  
  <line x1="570" y1="440" x2="520" y2="440" stroke="#990066" stroke-width="2" />
  <polygon points="520,440 530,435 530,445" fill="#990066" />
  
  <!-- Legend -->
  <rect x="50" y="500" width="700" height="80" fill="#f8f9fa" stroke="#333" stroke-width="1" rx="5" />
  <text x="400" y="520" font-family="Arial" font-size="14" text-anchor="middle" fill="#333">Legend</text>
  
  <rect x="100" y="540" width="20" height="20" fill="#e6f7ff" stroke="#0066cc" stroke-width="1" />
  <text x="130" y="555" font-family="Arial" font-size="12" fill="#333" text-anchor="start">User</text>
  
  <rect x="250" y="540" width="20" height="20" fill="#f0fff0" stroke="#006600" stroke-width="1" />
  <text x="280" y="555" font-family="Arial" font-size="12" fill="#333" text-anchor="start">Encryption Tools</text>
  
  <rect x="400" y="540" width="20" height="20" fill="#fff0f5" stroke="#990066" stroke-width="1" />
  <text x="430" y="555" font-family="Arial" font-size="12" fill="#333" text-anchor="start">Storage & Files</text>
  
  <line x1="550" y1="550" x2="590" y2="550" stroke="#333" stroke-width="2" />
  <polygon points="590,550 580,545 580,555" fill="#333" />
  <text x="625" y="555" font-family="Arial" font-size="12" fill="#333" text-anchor="start">Data Flow</text>
</svg>

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
