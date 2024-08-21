#!/usr/bin/python3

"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers where each integer represents
        a byte (8 least significant bits).

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    continuation_bytes_needed = 0

    # Define bit patterns for UTF-8 encoding
    SIGNIFICANT_BIT = 1 << 7  # 10000000
    SECOND_SIGNI_BIT = 1 << 6  # 01000000

    for byte in data:
        leading_one_mask = 1 << 7

        if continuation_bytes_needed == 0:
            while leading_one_mask & byte:
                continuation_bytes_needed += 1
                leading_one_mask >>= 1

            if continuation_bytes_needed == 0:
                continue

            if continuation_bytes_needed == 1 or continuation_bytes_needed > 4:
                return False
        else:
            if not (byte & SIGNIFICANT_BIT and not (byte & SECOND_SIGNI_BIT)):
                return False

        continuation_bytes_needed -= 1

    return continuation_bytes_needed == 0
