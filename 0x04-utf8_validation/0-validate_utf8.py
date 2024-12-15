#!/usr/bin/python3
'''
A module to determine if a data s
'''


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes of data
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Ensure the byte is within 1-byte range
        if byte > 255:
            return False

        if num_bytes == 0:
            # Check how many bytes the UTF-8 character should have
            if byte & mask1 == 0:
                continue  # 1-byte character
            mask = mask1
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            # UTF-8 characters can only be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
