#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    UTF-8 encoding.
    Args:
            data (list[int]): a list of integers
    """
    continuation_bytes = 0

    UTF8_BIT_1 = 1 << 7  # 10000000
    UTF8_BIT_2 = 1 << 6  # 01000000

    for byte in data:
     
        leading_one_mask = 1 << 7


        if continuation_bytes == 0:

            while leading_one_mask & byte:
                continuation_bytes += 1
                leading_one_mask = leading_one_mask >> 1

            if continuation_bytes == 0:
                continue

            if continuation_bytes == 1 or\
                    continuation_bytes > 4:
                return False

        else:

            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

        continuation_bytes -= 1

    if continuation_bytes == 0:
        return True
    else:
        return False
