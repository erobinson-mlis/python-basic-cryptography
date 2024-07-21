# Transposition Cipher Automated Testing
# Adapted from Kubic, Cracking Codes with Python
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# Adapted by Eric Robinson (Shared under BSD License)

import random, sys, transpositionEncrypt,transpositionDecrypt

def main():
    random.seed(3) # Set the random "seed" to a static value.

    for i in range(100):     # Run 20 tests.
        # Generate random messages to test
        
        # the message will have a random length:
        message = 'ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' * random.randint(4,40)

        # Convert the message string to a list to shuffle it.
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)  # Convert the shuffled list back to a string

        print('Test #%s: "%s..."' % (i + 1, message[:150]))

        # Check all possible keys for each message:
        for key in range(1, int(len(message)/2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            # If the decryption doesn't match the original message,
            # then display an error message and quit
            if message != decrypted:
                print('Mismatch with key %s and message %s' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher automated testing passed.')

# If transposition.Test.py is run (instead of imported as a mudle), 
# then call the main() function:
if __name__ == '__main__':
    main()