# Encryption Playground Lab Instructions

## Lab Overview
In this hands-on lab, you'll explore different encryption methods and understand their strengths, weaknesses, and appropriate uses. You'll be working with the Globomantics security team to evaluate encryption options for protecting sensitive communications.

## Estimated Time: 10-15 minutes

## Prerequisites
- Linux-based system (Kali Linux recommended)
- Python 3.6 or higher
- Basic knowledge of terminal commands

## Learning Objectives
- Understand different types of encryption methods
- Gain hands-on experience with encryption and decryption
- Compare symmetric and asymmetric encryption
- Explore secure hashing algorithms
- Learn when to use each encryption type

## Step-by-Step Instructions

### Part 1: Setup the Environment (1 minute)

1. Open a terminal window
2. Run the setup script:
   ```bash
   bash setup.sh
   ```
3. Verify that the setup completed successfully

### Part 2: Explore Basic Encryption Methods (3 minutes)

1. Launch the basic encryption tool:
   ```bash
   python3 simple_encrypt.py
   ```

2. From the main menu, select "1. Caesar Cipher"

3. **YOUR TASK**: Encrypt a message using the Caesar cipher
   - Choose option 1 to encrypt a message
   - Enter the message: "Globomantics Secret Plans"
   - Use a shift value of 7
   - Write down the encrypted result

4. **YOUR TASK**: Decrypt the message
   - Choose option 2 to decrypt a message
   - Enter the encrypted message you just created
   - Enter the shift value 7
   - Verify that you get the original message back

5. Return to the main menu by selecting option 4

### Part 3: Test Symmetric Encryption (3 minutes)

1. Launch the symmetric encryption tool:
   ```bash
   python3 symmetric_encrypt.py
   ```

2. **YOUR TASK**: Generate an encryption key
   - Choose option 1 from the menu
   - Select key size 2 (2048 bits)
   - Save the key to a file when prompted (answer 'y')
   - Note the filename where the key is saved

3. **YOUR TASK**: Encrypt a message
   - Choose option 2 from the menu
   - Provide the key by selecting option 2 (load from file)
   - Enter the key filename you noted earlier
   - Enter a message: "The artificial island security codes are: 9876-5432-1098"
   - Select CBC mode (option 1)
   - Note the filename where the encrypted message is saved

4. Return to the main menu by selecting option 7

### Part 4: Explore Hash Functions (3 minutes)

1. Launch the hashing tool:
   ```bash
   python3 hash_generator.py
   ```

2. **YOUR TASK**: Compare different hash algorithms
   - Choose option 1 from the menu
   - Enter the text: "Globomantics"
   - Observe the different hash outputs and their lengths
   - Note which hash algorithms produce the longest outputs

3. **YOUR TASK**: Demonstrate the avalanche effect
   - Choose option 2 from the menu
   - Enter the text: "password123"
   - Observe how a small change creates a completely different hash

4. Return to the main menu by selecting option 6

### Part 5: Explore Public Key Encryption (3 minutes)

1. Launch the public key demonstration:
   ```bash
   python3 public_key_demo.py
   ```

2. **YOUR TASK**: Generate a key pair
   - Choose option 1 from the menu
   - Select key size 2 (2048 bits)
   - Note the filenames for both the public and private keys

3. **YOUR TASK**: Encrypt and decrypt a message
   - Choose option 2 (Encrypt a message)
   - Select your public key file
   - Enter a message: "For your eyes only"
   - Note the encrypted output
   - Choose option 3 (Decrypt a message)
   - Select your private key file
   - Choose option 2 (Load from file)
   - Select the encrypted message file
   - Verify the decryption works correctly

4. **YOUR TASK**: Review the comparison of symmetric vs asymmetric encryption
   - Choose option 6 from the menu
   - Review the strengths and weaknesses of each method

5. Exit the program by selecting option 8

### Part 6: Complete the Evaluation Worksheet (2 minutes)

1. **YOUR TASK**: Complete the encryption evaluation worksheet:
   ```bash
   nano encryption_evaluation.txt
   ```

2. Fill in your observations about the strengths and weaknesses of each encryption method

3. Make recommendations for which encryption methods would be appropriate for different types of data

4. Save the file (Ctrl+O, then Enter, then Ctrl+X)

### Part 7: Test Your Knowledge (Optional)

1. **YOUR TASK**: Try the decryption challenges:
   ```bash
   python3 decrypt_challenge.py
   ```

2. Apply what you've learned to solve the encryption puzzles

### Part 8: Lab Cleanup (1 minute)

1. Reset the lab environment:
   ```bash
   bash cleanup.sh
   ```

## Completion Criteria
You have successfully completed this lab when you have:
- Encrypted and decrypted messages using Caesar cipher
- Used AES symmetric encryption to secure a message
- Generated and compared different hash functions
- Created a public/private key pair and used it for encryption
- Completed the encryption evaluation worksheet

## Additional Challenges (Optional)
- Try encrypting a file rather than just a message
- Experiment with different key sizes and observe performance differences
- Create a digital signature and verify it
- Solve all three decryption challenges
