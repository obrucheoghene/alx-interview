#!/usr/bin/python3
'''UTF-8 Validation
'''


def validUTF8(data):
    '''UTF-8 Validation'''
    
    # Initialize a variable to keep track of the number of bytes left to read for the current character.
    bytes_to_read = 0

    # Iterate through the list of integers.
    for byte in data:
        # Check the two most significant bits of the current byte to determine the number of bytes in the character.
        if bytes_to_read == 0:
            if byte >> 5 == 0b110:
                bytes_to_read = 1
            elif byte >> 4 == 0b1110:
                bytes_to_read = 2
            elif byte >> 3 == 0b11110:
                bytes_to_read = 3
            elif byte >> 7 != 0:
                return False  # The most significant bit should be 0 for single-byte characters.
        else:
            if byte >> 6 != 0b10:
                return False  # Check that the byte starts with the bit pattern 10.

        # Decrease the number of bytes left to read for the current character.
        bytes_to_read -= 1

    # If we've read all bytes for each character, it's a valid UTF-8 encoding.
    return bytes_to_read == 0

# Example usage:
data = [197, 130, 1]  # This is a valid UTF-8 encoding representing a character with the code point U+0101.
print(validUTF8(data))  # Should return True
