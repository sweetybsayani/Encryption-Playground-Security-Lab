#!/bin/bash

# Encryption Playground Lab Setup Script
# This script sets up the encryption playground lab environment

echo "==============================================="
echo "  Encryption Playground Lab Setup"
echo "  Setting up encryption testing environment"
echo "==============================================="

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is required but not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Create directories
echo "[+] Creating lab directories..."
mkdir -p ./encrypted_files
mkdir -p ./keys
mkdir -p ./results

# Install required Python packages
echo "[+] Installing required Python packages..."
pip3 install -q pycryptodome colorama tabulate

# Create sample text files
echo "[+] Creating sample files to encrypt..."
echo "This is a TOP SECRET message from Globomantics CEO. The artificial island project is proceeding as planned." > ./sample_text_1.txt
echo "CONFIDENTIAL: The new security protocol will be implemented next week. All staff must update their credentials." > ./sample_text_2.txt
echo "Project Firewall: Latest updates include enhanced protection against DDoS attacks and improved packet filtering." > ./sample_text_3.txt

# Generate sample key file
echo "[+] Generating sample encryption keys..."
python3 -c "import os; print(os.urandom(16).hex())" > ./keys/sample_aes_key.txt
python3 -c "import os; print(os.urandom(32).hex())" > ./keys/sample_aes256_key.txt

# Create encryption evaluation worksheet
echo "[+] Creating encryption evaluation worksheet..."
cat > encryption_evaluation.txt << 'EOL'
# Encryption Methods Evaluation Worksheet

Instructions: After completing the lab exercises, fill in your evaluation of each encryption method.

## 1. Caesar Cipher
Strengths: 
Weaknesses: 
Appropriate uses: 
Security rating (1-10): 

## 2. AES Symmetric Encryption
Strengths: 
Weaknesses: 
Appropriate uses: 
Security rating (1-10): 

## 3. Hash Functions
Strengths: 
Weaknesses: 
Appropriate uses: 
Security rating (1-10): 

## 4. RSA Public Key Encryption
Strengths: 
Weaknesses: 
Appropriate uses: 
Security rating (1-10): 

## 5. Your Recommendation
For each scenario below, recommend the most appropriate encryption method:

Scenario 1 - Storing user passwords: 

Scenario 2 - Sending sensitive email: 

Scenario 3 - Secure website connection: 

Scenario 4 - Storing credit card information: 

## Additional Notes:


EOL

echo "[+] Setting execute permissions on Python scripts..."
chmod +x *.py 2>/dev/null || true

echo "==============================================="
echo "  Setup Complete!"
echo "  Start with: python3 simple_encrypt.py"
echo "==============================================="
