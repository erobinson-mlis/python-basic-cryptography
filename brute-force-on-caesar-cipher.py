# Caesar Cipher Hacker
# Adapted from https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# by Eric Robinson (BSD Licensed)

message = input(f"Please input an encoded message to cryptanalyze: \n")
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key:
for key in range(len(SYMBOLS)):
    # It is important to set translated to the blank string so the 
    # previous iteration's value for translated is cleared:
    translated = ''

    # The rest of the program is almost the same as the Caesar program

    # Loop through each symbol in the message
    for symbol in message: 
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # handle the wraparound
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol to 'translated'
            translated = translated + SYMBOLS[translatedIndex]

        else: 
            # Append the symbol without decrypting
            translated = translated + symbol
        
    # Display decryption for each key' value
    print('Key #%s: %s' %(key, translated))