#!/bin/bash

# Encryption Playground Lab Cleanup Script
# This script resets the lab environment to its initial state

echo "==============================================="
echo "  Encryption Playground Lab Cleanup"
echo "  Resetting the encryption lab environment"
echo "==============================================="

# Confirm cleanup
echo "This will reset the lab environment to its initial state."
echo "All generated keys, encrypted files, and results will be deleted."
read -p "Are you sure you want to continue? (y/n): " confirm

if [ "$confirm" != "y" ]; then
    echo "Cleanup canceled."
    exit 0
fi

echo "[+] Removing encryption directories..."
rm -rf ./encrypted_files
rm -rf ./keys
rm -rf ./results

echo "[+] Setting up clean environment..."
bash setup.sh

echo "==============================================="
echo "  Cleanup Complete!"
echo "  The lab has been reset to its initial state."
echo "==============================================="
